import pandas as pd
import pickle

with open("C:/Users/raeda/NBA-predictor/14-23.pkl", "rb") as f:
    df = pickle.load(f)

df = df.rename(columns={"Unnamed: 5": "Home/Away", "Unnamed: 7": "W/L", "Unnamed: 8": "OT"})

df.loc[df["Opponent"] == "Charlotte Bobcats", "Opponent"] = "Charlotte Hornets"

df["Date Time"] = df["Date"] + " " + df["Start (ET)"]

def time_converter(input):

    if input[-1] == "p":
        if input[-6].isdigit():
            if input[-6:-4] == "12":
                out = input[:-1]
            else:
                hour = int(input[-6:-4])
                new = hour + 12
                out = input[:-6] + str(new) + input[-4:-1]
        else:
            hour = int(input[-5])
            new = hour + 12
            out = input[:-5] + str(new) + input[-4:-1]
    else: out = input  
    return out

df["Date Time"] = pd.to_datetime(df["Date Time"].apply(time_converter), format="%a, %b %d, %Y %H:%M")

df["Tm"] = df["Tm"].apply(int)
df["Opp"] = df["Opp"].apply(int)
df["W"] = df["W"].apply(int)
df["L"] = df["L"].apply(int)

df = df[["Season", "G", "Date Time", "Team", "Opponent", "W/L", "Tm", "Opp", "W", "L"]]

df.insert(10, "OW", 0)
df.insert(11, "OL", 0)

df = df.sort_values(by="Date Time")

df = df.reset_index()

nba_teams_def = {
    "Atlanta Hawks": (0, 0),
    "Boston Celtics": (0, 0),
    "Brooklyn Nets": (0, 0),
    "Charlotte Hornets": (0, 0),
    "Chicago Bulls": (0, 0),
    "Cleveland Cavaliers": (0, 0),
    "Dallas Mavericks": (0, 0),
    "Denver Nuggets": (0, 0),
    "Detroit Pistons": (0, 0),
    "Golden State Warriors": (0, 0),
    "Houston Rockets": (0, 0),
    "Indiana Pacers": (0, 0),
    "Los Angeles Clippers": (0, 0),
    "Los Angeles Lakers": (0, 0),
    "Memphis Grizzlies": (0, 0),
    "Miami Heat": (0, 0),
    "Milwaukee Bucks": (0, 0),
    "Minnesota Timberwolves": (0, 0),
    "New Orleans Pelicans": (0, 0),
    "New York Knicks": (0, 0),
    "Oklahoma City Thunder": (0, 0),
    "Orlando Magic": (0, 0),
    "Philadelphia 76ers": (0, 0),
    "Phoenix Suns": (0, 0),
    "Portland Trail Blazers": (0, 0),
    "Sacramento Kings": (0, 0),
    "San Antonio Spurs": (0, 0),
    "Toronto Raptors": (0, 0),
    "Utah Jazz": (0, 0),
    "Washington Wizards": (0, 0),
}

nba_teams = nba_teams_def.copy()

season = 0

for index, row in df.iterrows():

    if season != row["Season"]:
        nba_teams = nba_teams_def.copy()
        season += 1

    nba_teams[row["Team"]] = (row["W"], row["L"])

    WL = nba_teams[row["Opponent"]]

    if row["W/L"] == "W":  
        nba_teams[row["Opponent"]] = (WL[0], WL[1] + 1)
    else:
        nba_teams[row["Opponent"]] = (WL[0] + 1, WL[1])

    df.at[index, "OW"] = nba_teams[row["Opponent"]][0]
    df.at[index, "OL"] = nba_teams[row["Opponent"]][1]

    #if df.loc[index, "OW"] + df.loc[index, "OL"] == 82 and row["Season"] == 9:
        #print(row["Season"], row["Opponent"], df.loc[index, "OW"], df.loc[index, "OL"])

    #if row["W"] + row["L"] == 82 and row["Season"] == 9:
        #print(row["Season"], row["Team"], row["W"], row["L"])


df = df[["Season", "G", "Date Time", "Team", "Opponent", "W/L", "Tm", "Opp", "W", "L"]]

df.to_pickle("C:/Users/raeda/NBA-predictor/Processed_Data.pkl")