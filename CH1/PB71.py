import pandas as pd
df1 = pd.DataFrame({
 "ID":[1,2,3],
 "Name":["A","B","C"]
})
df2 = pd.DataFrame({
 "ID":[2,3,4],
 "Marks":[80,90,70]
})
# Concatenate row-wise 
df = pd.concat([df1, df2], axis=0)
# Count total missing values
print("Total Missing Values:", df.isna().sum().sum())
# Sort by ID
df = df.sort_values(by="ID")
print(df)