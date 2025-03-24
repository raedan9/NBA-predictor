import pandas as pd
import pickle

with open("C:/Users/raeda/NBA-predictor/14-23.pkl", "rb") as f:  # Open in read-binary mode
    df = pickle.load(f)

df = df.rename(columns={"Unnamed: 5": "Home/Away", "Unnamed: 7": "W/L", "Unnamed: 8": "OT"})

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
#df = df[["G", "Date Time", "Team", "Opponent", "W/L", "Tm", "Opp", "W", "L"]]

df = df.sort_values(by="Date Time")

print(df)
print(type(df.iat[2, 1]))
print(df.iat[2, 1])
#df["Home/Away"] = df["Home/Away"].str.replace("@", "A")
#df["Home/Away"] = df["Home/Away"].fillna("H")
#print(df.loc[df["W/L"] == "L"])


