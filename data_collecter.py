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

combined_df = pd.DataFrame()
teams_done = {}

for team in nba_teams.keys():

    url = "https://www.basketball-reference.com/teams/" + team + "/2024_games.html"
    print(url)
    tables = pd.read_html(url)
    df = tables[0]
    
    df = df.drop(df[df["Tm"] == "Tm"].index)
    df = df[:82]
    df.insert(6, "Team", nba_teams[team])

    teams_done[team] = nba_teams[team]

    for team in teams_done.keys():
        df = df.drop(df[df["Opponent"] == nba_teams[team]].index)    

    combined_df = pd.concat([combined_df, df])
    time.sleep(4)
    if team == "BRK":
        break
    
print(combined_df)
combined_df.to_pickle("C:/Users/raeda/23-24.pkl")

#df = df[["Unnamed: 5", "Opponent", "Unnamed: 7", "Tm", "Opp", "W", "L"]]
#df = df.rename(columns={"Unnamed: 5": "Home/Away", "Unnamed: 7": "W/L"})

#df["Home/Away"] = df["Home/Away"].str.replace("@", "A")
#df["Home/Away"] = df["Home/Away"].fillna("H")
#print(df.loc[df["W/L"] == "L"])

