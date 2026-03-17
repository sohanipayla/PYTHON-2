import pandas as pd
students = pd.DataFrame({
 "ID":[1,2,3,4],
 "Name":["A","B","C","D"]
})
marks = pd.DataFrame({
 "ID":[2,3,5],
 "Score":[85,90,75]
})
# Outer merge with indicator
df = pd.merge(students, marks, on="ID", how="outer", indicator=True)
print(df)
# Count values from indicator column
print("\nCounts:")
print(df["_merge"].value_counts())