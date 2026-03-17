import pandas as pd
df = pd.DataFrame({
 "Team":["A","A","A","B","B"],
 "Runs":[50,70,80,40,60]
})
# Calculate range (max - min) using apply
result = df.groupby("Team")["Runs"].apply(lambda x: x.max() - x.min())
print(result)