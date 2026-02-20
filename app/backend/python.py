from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
import pandas as pd
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={r"/process_data": {"origins": ["http://localhost:5173", "http://127.0.0.1:5173"]}})

@app.route('/process_data', methods=['POST', 'OPTIONS'])
@cross_origin(origins=["http://localhost:5173", "http://127.0.0.1:5173"])
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

    season_one = f'{user_input_season_one - 1}-{str(user_input_season_one)[-2:]}'
    season_two = f'{user_input_season_two - 1}-{str(user_input_season_two)[-2:]}'

    season_one_row = df_one[df_one['SEASON_ID'] == season_one]
    season_two_row = df_two[df_two['SEASON_ID'] == season_two]

    # Check if the rows are empty
    if season_one_row.empty or season_two_row.empty:
        return jsonify({'error': f'Season data not found for {season_one} or {season_two}.'})

    # Get the values for the statistics
    gp_one = int(season_one_row['GP'].values[0])
    gp_two = int(season_two_row['GP'].values[0])

    one_ppg = float(round(season_one_row['PTS'].values[0] / gp_one, 2))
    two_ppg = float(round(season_two_row['PTS'].values[0] / gp_two, 2))

    one_rpg = float(round(season_one_row['REB'].values[0] / gp_one, 2))
    two_rpg = float(round(season_two_row['REB'].values[0] / gp_two, 2))

    one_apg = float(round(season_one_row['AST'].values[0] / gp_one, 2))
    two_apg = float(round(season_two_row['AST'].values[0] / gp_two, 2))

    one_spg = float(round(season_one_row['STL'].values[0] / gp_one, 2))
    two_spg = float(round(season_two_row['STL'].values[0] / gp_two, 2))

    one_bpg = float(round(season_one_row['BLK'].values[0] / gp_one, 2))
    two_bpg = float(round(season_two_row['BLK'].values[0] / gp_two, 2))

    one_mpg = float(round(season_one_row['MIN'].values[0] / gp_one, 2))
    two_mpg = float(round(season_two_row['MIN'].values[0] / gp_two, 2))

    one_fg = float(round(season_one_row['FG_PCT'].values[0] * 100, 2))
    two_fg = float(round(season_two_row['FG_PCT'].values[0] * 100, 2))

    one_szn = season_one_row['SEASON_ID'].values[0]
    two_szn = season_two_row['SEASON_ID'].values[0]


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
