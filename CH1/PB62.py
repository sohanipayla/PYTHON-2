import pandas as pd
df = pd.read_csv('ipl-matches.csv')
df

# 1. Matches in superover
s=df[df['SuperOver'] == 'Y']
print(s)

# 2. CSK wins at Kolkata
csk=df[(df['WinningTeam'] == 'Chennai Super Kings') & (df['City'] == 'Kolkata')]
print(csk.shape[0])

# 3. Dhoni POTM vs Mumbai Indians
mi=df[(df['Player_of_Match'] == 'MS Dhoni') & ((df['Team1'] == 'Mumbai Indians') | (df['Team2'] == 'Mumbai Indians'))]
print(mi.shape[0])

# 4. GT won toss, elected to bat, and won match
gt=df[(df['TossWinner'] == 'Gujarat Titans') & (df['TossDecision'] == 'bat') & (df['WinningTeam'] == 'Gujarat Titans')]
gt

# 5. All matches won by Gujarat Titans
all_gt=df[df['WinningTeam'] == 'Gujarat Titans']
all_gt