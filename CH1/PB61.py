import pandas as pd

# 1. Convert CSV file into DataFrame
df = pd.read_csv("heights_weights.csv")

# Display first rows
print("First 5 Rows:")
print(df.head())

# 2. Basic information (memory & data types)
print("\nDataFrame Info:")
print(df.info())

# 3. Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# 4. Correlation table
print("\nCorrelation Table:")
corr = df.corr()
print(corr)

# Comment on correlation
print("\nComment:")
print("Height and Weight show positive correlation (as height increases, weight also increases).")

# 5. Check outliers
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR)))

print(outliers.sum())
