import pandas as pd
data = {
    "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
    "B": [50, 40, 40, 30, 50],
    "C": [True, False, False, False, True]
}
df = pd.DataFrame(data)
print(df)
df = df.drop_duplicates()
df = df.reset_index(drop=True)
print(df)