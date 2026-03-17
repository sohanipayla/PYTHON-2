import pandas as pd
import matplotlib.pyplot as plt

# 1. Convert CSV into DataFrame
df = pd.read_csv("spotify.csv")

# 2. Display basic information
print("DataFrame Info:")
print(df.info())

# 3. Display basic statistics
print("\nStatistics:")
print(df.describe())

# 4. Correlation table and comment
print("\nCorrelation Table:")
corr = df.corr()
print(corr)

print("\nComment:")
print("Danceability and Energy usually show positive correlation (higher danceability tends to have higher energy).")

# 5. First five rows
print("\nFirst 5 rows:")
print(df.head())

# 6. Last five rows
print("\nLast 5 rows:")
print(df.tail())

# 7. Rows between 15 to 39
print("\nRows 15 to 39:")
print(df.iloc[15:40])

# 8. Last five rows and last five columns
print("\nLast 5 rows and last 5 columns:")
print(df.iloc[-5:, -5:])

# 9. Shape of DataFrame
print("\nShape of DataFrame:")
print(df.shape)

# 10. Sum of NULL values
print("\nNull values in each column:")
print(df.isna().sum())

# 11. Remove first 3 columns
df1 = df.iloc[:, 3:]

# 12. Remove first 10 rows
df2 = df1.iloc[10:]

# 13. Find outliers for popularity (IQR method)
Q1 = df2['popularity'].quantile(0.25)
Q3 = df2['popularity'].quantile(0.75)
IQR = Q3 - Q1

outliers_popularity = df2[(df2['popularity'] < Q1 - 1.5*IQR) | (df2['popularity'] > Q3 + 1.5*IQR)]

print("\nOutliers in popularity column:")
print(outliers_popularity)

# 14. Remove outliers for energy
Q1 = df2['energy'].quantile(0.25)
Q3 = df2['energy'].quantile(0.75)
IQR = Q3 - Q1

df_no_outliers = df2[(df2['energy'] >= Q1 - 1.5*IQR) & (df2['energy'] <= Q3 + 1.5*IQR)]

print("\nDataFrame after removing energy outliers:")
print(df_no_outliers)

# 15. Cross tabulation between time_signature and track_genre
print("\nCross Tabulation:")
print(pd.crosstab(df['time_signature'], df['track_genre']))
