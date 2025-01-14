'''from flask import Flask, request, jsonify
from flask_cors import CORS
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.get_json()
    playerone = data.get('variable')
    print(playerone)
    playertwo = data.get('secondvariable')
    print(playertwo)

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

    #Creating Variables to Compare Basic Statistics
    gp_one = int(df_one.iloc[0]['GP'])
    gp_two = int(df_two.iloc[0]['GP'])

    one_ppg = float(round(df_one.iloc[0]['PTS'] / gp_one, 2))  # Points per Game
    two_ppg = float(round(df_two.iloc[0]['PTS'] / gp_two, 2))

    one_rpg = float(round(df_one.iloc[0]['REB'] / gp_one, 2))  # Rebounds per Game
    two_rpg = float(round(df_two.iloc[0]['REB'] / gp_two, 2))

    one_apg = float(round(df_one.iloc[0]['AST'] / gp_one, 2))  # Assists Per Game
    two_apg = float(round(df_two.iloc[0]['AST'] / gp_two, 2))

    one_spg = float(round(df_one.iloc[0]['STL'] / gp_one, 2))  # Steals Per Game
    two_spg = float(round(df_two.iloc[0]['STL'] / gp_two, 2))

    one_bpg = float(round(df_one.iloc[0]['BLK'] / gp_one, 2))  # Blocks Per Game
    two_bpg = float(round(df_two.iloc[0]['BLK'] / gp_two, 2))

    one_mpg = float(round(df_one.iloc[0]['MIN'] / gp_one, 2))  # Minutes Per Game
    two_mpg = float(round(df_two.iloc[0]['MIN'] / gp_two, 2))
'''
    #Comparing which player has higher
    # ppg = 0
    # rpg = 0
    # apg = 0
    # bpg = 0
    # spg = 0
    # mpg = 0
    # gp = 0
    # player_ppg  = ''
    # player_rpg = ''
    # player_apg = ''
    # player_bpg = ''
    # player_spg = ''
    # player_mpg = ''
    # player_gp = ''

    # # Points per Game
    # if one_ppg > two_ppg:
    #     ppg += one_ppg
    #     player_ppg = playerone
    # elif one_ppg < two_ppg:
    #     ppg += two_ppg
    #     player_ppg = playertwo
    # # Rebounds per Game
    # if one_rpg > two_rpg:
    #     rpg += one_rpg
    #     player_rpg = playerone
    # elif one_rpg < two_rpg:
    #     rpg += two_rpg
    #     player_rpg = playertwo
    # # Assists per Game
    # if one_apg > two_apg:
    #     apg += one_apg
    #     player_apg = playerone
    # elif one_apg < two_apg:
    #     apg += two_apg
    #     player_apg = playertwo
    # # Blocks per Game
    # if one_bpg > two_bpg:
    #     bpg += one_bpg
    #     player_bpg = playerone
    # elif one_bpg < two_bpg:
    #     bpg += two_bpg
    #     player_bpg = playertwo
    # # Steals per Game
    # if one_spg > two_spg:
    #     spg += one_spg
    #     player_spg = playerone
    # elif one_spg < two_spg:
    #     spg += two_spg
    #     player_spg = playertwo
    # # Minutes per Game
    # if one_mpg > two_mpg:
    #     mpg += one_mpg
    #     player_mpg = playerone
    # elif one_mpg < two_mpg:
    #     mpg += two_mpg
    #     player_mpg = playertwo
    # # Games Played
    # if gp_one > gp_two:
    #     gp += gp_one
    #     player_gp = playerone
    # elif gp_one < gp_two:
    #     gp += gp_two
    #     player_gp = playertwo

    # print(f'{player_ppg} has the higher points per game with: {ppg}')
    # print(f'{player_rpg} has the higher rebounds per game with: {rpg}')
    # print(f'{player_apg} has the higher assists per game with: {apg}')
    # print(f'{player_bpg} has the higher blocks per game with: {bpg}')
    # print(f'{player_spg} has the higher steals per game with: {spg}')
    # print(f'{player_mpg} has the higher minutes per game with: {mpg}')
    # print(f'{player_gp} has the higher games played with: {gp}')
'''
    return jsonify({'Player One': playerone,
                    'PPG1': one_ppg,
                    'APG': one_apg,
                    'RPG': one_rpg,
                    'FG1': 50,
                    'SPG1': one_spg,
                    'BPG1': one_bpg,
                    'MP1': one_mpg,
                    'GP1': gp_one}, 
                   {"Player Two": playertwo,                    
                    'PPG1': two_ppg,
                    'APG': two_apg,
                    'RPG': two_rpg,
                    'FG1': 50,
                    'SPG1': two_spg,
                    'BPG1': two_bpg,
                    'MP1': two_mpg,
                    'GP1': gp_two,
                   })

if __name__ == '__main__':
    app.run(debug=True)
'''

