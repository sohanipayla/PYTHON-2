import pandas as pd
df = pd.read_csv("auto-mpg.csv")
print(df.head())
# Remove mpg and cylinders columns
df = df.drop(['mpg', 'cylinders'], axis=1)
print("\nDataFrame after removing columns:")
print(df.head())