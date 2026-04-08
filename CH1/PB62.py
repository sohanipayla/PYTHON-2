import pandas as pd
df = pd.read_csv("ipl-matches.csv")
df.info()

# 1. Matches in superover
super_over_matches = df[df["SuperOver"] == "Y"]
print(super_over_matches)

# 2. CSK wins at Kolkata
csk_kolkata = df[(df["WinningTeam"] == "Chennai Super Kings") & (df["City"] == "Kolkata")]
print(len(csk_kolkata))

# 3. Dhoni POTM vs Mumbai Indians
dhoni_mi = df[(df["Player_of_Match"] == "MS Dhoni") & 
              ((df["Team1"] == "Mumbai Indians") | (df["Team2"] == "Mumbai Indians"))]

print(len(dhoni_mi))

# 4. GT won toss, elected to bat, and won match
gt_matches = df[(df["TossWinner"] == "Gujarat Titans") &
                (df["TossDecision"] == "bat") &
                (df["WinningTeam"] == "Gujarat Titans")]

print(gt_matches)

# 5. All matches won by Gujarat Titans
gt_wins = df[df["WinningTeam"] == "Gujarat Titans"]
print(gt_wins)
