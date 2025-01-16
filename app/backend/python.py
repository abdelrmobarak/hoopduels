from flask import Flask, request, jsonify
from flask_cors import CORS
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
import pandas as pd
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.get_json()
    playerone = data.get('variable')
    print(playerone)
    playertwo = data.get('secondvariable')
    print(playertwo)
    yearone = int(data.get('yearvar'))
    print(yearone)
    yeartwo = int(data.get('secondyearvar'))
    print(yeartwo)

    nba_players = players.get_players()

    pd.options.display.max_rows=1000
    pd.options.display.max_columns=1000

    id_number_one = 0
    for player in nba_players:
        if player['full_name'].upper() == playerone.upper():
            id_number_one = player['id']
    career_one = playercareerstats.PlayerCareerStats(player_id=(id_number_one))
    df_one = (career_one.get_data_frames()[0])

    #Player Two Stats
    id_number_two = 0

    for player in nba_players:
        if player['full_name'].upper() == playertwo.upper():
            id_number_two = player['id']
    career_two = playercareerstats.PlayerCareerStats(player_id=(id_number_two))
    df_two = (career_two.get_data_frames()[0])



    #Checking if player was on two teams in a season, then dropping the extra rows
    rows_to_drop_one = []
    tot_row_two = df_one[df_one['TEAM_ABBREVIATION'] == 'TOT']
    if not tot_row_two.empty:
        index_one = tot_row_two.index[0]
        rows_to_drop_one.extend([index_one - 1, index_one - 2])
    else:
        print("No rows found for TOT in df_one")

    totwo_row = df_one[df_one['TEAM_ABBREVIATION'] == '2TM']
    if not totwo_row.empty:
        index_one_totwo = totwo_row.index[0]
        rows_to_drop_one.extend([index_one_totwo - 1, index_one_totwo - 2])
    else:
        print("No rows found for 2TM in df_one")

    if rows_to_drop_one:
        df_one.drop(rows_to_drop_one, inplace=True, errors='ignore')

    rows_to_drop_two = []
    tot_row_two = df_two[df_two['TEAM_ABBREVIATION'] == 'TOT']
    if not tot_row_two.empty:
        index_two = tot_row_two.index[0]
        rows_to_drop_two.extend([index_two - 1, index_two - 2])
    else:
        print("No rows found for TOT in df_two")

    totwo_row_two = df_two[df_two['TEAM_ABBREVIATION'] == '2TM']
    if not totwo_row_two.empty:
        index_two_totwo = totwo_row_two.index[0]
        rows_to_drop_two.extend([index_two_totwo - 1, index_two_totwo - 2])
    else:
        print("No rows found for 2TM in df_two")

    if rows_to_drop_two:
        df_two.drop(rows_to_drop_two, inplace=True, errors='ignore')

    #Debugging checks
    print(df_one)
    print(df_two)




    year = datetime.now().year
    user_input_season_one = yearone
    user_input_season_two = yeartwo

    season_one = (year - user_input_season_one + 1) * -1
    season_two = (year - user_input_season_two + 1) * -1
    print(season_one)
    print(season_two)

    #Creating Variables to Compare Basic Statistics
    gp_one = int(df_one.iloc[season_one]['GP'])
    gp_two = int(df_two.iloc[season_two]['GP'])

    one_ppg = float(round(df_one.iloc[season_one]['PTS'] / gp_one, 2))  # Points per Game
    two_ppg = float(round(df_two.iloc[season_two]['PTS'] / gp_two, 2))

    one_rpg = float(round(df_one.iloc[season_one]['REB'] / gp_one, 2))  # Rebounds per Game
    two_rpg = float(round(df_two.iloc[season_two]['REB'] / gp_two, 2))

    one_apg = float(round(df_one.iloc[season_one]['AST'] / gp_one, 2))  # Assists Per Game
    two_apg = float(round(df_two.iloc[season_two]['AST'] / gp_two, 2))

    one_spg = float(round(df_one.iloc[season_one]['STL'] / gp_one, 2))  # Steals Per Game
    two_spg = float(round(df_two.iloc[season_two]['STL'] / gp_two, 2))

    one_bpg = float(round(df_one.iloc[season_one]['BLK'] / gp_one, 2))  # Blocks Per Game
    two_bpg = float(round(df_two.iloc[season_two]['BLK'] / gp_two, 2))

    one_mpg = float(round(df_one.iloc[season_one]['MIN'] / gp_one, 2))  # Minutes Per Game
    two_mpg = float(round(df_two.iloc[season_two]['MIN'] / gp_two, 2))

    one_fg = float(round(df_one.iloc[season_one]['FG_PCT']*100,2)) #FG%
    two_fg = float(round(df_two.iloc[season_two]['FG_PCT']*100,2))

    one_szn = df_one.iloc[season_one]['SEASON_ID']
    two_szn = df_two.iloc[season_two]['SEASON_ID']

    return jsonify({'Player One': playerone,
                    'PPG1': one_ppg,
                    'APG1': one_apg,
                    'RPG1': one_rpg,
                    'FG1': one_fg,
                    'SPG1': one_spg,
                    'BPG1': one_bpg,
                    'MP1': one_mpg,
                    'GP1': gp_one,
                    'SZN1': one_szn}, 
                   {"Player Two": playertwo,                    
                    'PPG2': two_ppg,
                    'APG2': two_apg,
                    'RPG2': two_rpg,
                    'FG2': two_fg,
                    'SPG2': two_spg,
                    'BPG2': two_bpg,
                    'MP2': two_mpg,
                    'GP2': gp_two,
                    'SZN2': two_szn})

if __name__ == '__main__':
    app.run(debug=True)
