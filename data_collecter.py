import pandas as pd
import time

nba_teams = {
    "ATL": "Atlanta Hawks",
    "BOS": "Boston Celtics",
    "BRK": "Brooklyn Nets",
    "CHO": "Charlotte Hornets",
    "CHI": "Chicago Bulls",
    "CLE": "Cleveland Cavaliers",
    "DAL": "Dallas Mavericks",
    "DEN": "Denver Nuggets",
    "DET": "Detroit Pistons",
    "GSW": "Golden State Warriors",
    "HOU": "Houston Rockets",
    "IND": "Indiana Pacers",
    "LAC": "Los Angeles Clippers",
    "LAL": "Los Angeles Lakers",
    "MEM": "Memphis Grizzlies",
    "MIA": "Miami Heat",
    "MIL": "Milwaukee Bucks",
    "MIN": "Minnesota Timberwolves",
    "NOP": "New Orleans Pelicans",
    "NYK": "New York Knicks",
    "OKC": "Oklahoma City Thunder",
    "ORL": "Orlando Magic",
    "PHI": "Philadelphia 76ers",
    "PHO": "Phoenix Suns",
    "POR": "Portland Trail Blazers",
    "SAC": "Sacramento Kings",
    "SAS": "San Antonio Spurs",
    "TOR": "Toronto Raptors",
    "UTA": "Utah Jazz",
    "WAS": "Washington Wizards"
}

final_df = pd.DataFrame()

for i in range(10):

    combined_df = pd.DataFrame()
    teams_done = {}

    for team in nba_teams.keys():

        url = "https://www.basketball-reference.com/teams/" + team + "/" + str(2014 + i) + "_games.html"

        if i == 0 and team == "CHO":
            url = "https://www.basketball-reference.com/teams/CHA/2014_games.html"

        print(url)
        tables = pd.read_html(url)
        df = tables[0]
    
        df = df.drop(df[df["Tm"] == "Tm"].index)
        df = df.drop(df[df["Notes"] == "Play-In Game"].index)   

        df.insert(0, "Season", i)
        df.insert(6, "Team", nba_teams[team])

        print(df)
        
        teams_done[team] = nba_teams[team]

        for team_done in teams_done.keys():

            if i == 0 and team_done == "CHO":

                df = df.drop(df[df["Opponent"] == "Charlotte Bobcats"].index)

            else:

                df = df.drop(df[df["Opponent"] == nba_teams[team_done]].index)   

        combined_df = pd.concat([combined_df, df])
        time.sleep(3.5)

    print(len(combined_df))
    final_df = pd.concat([final_df, combined_df])
    
print(final_df)
#13/14 season to 22/23
final_df.to_pickle("C:/Users/raeda/NBA-predictor/14-23.pkl")