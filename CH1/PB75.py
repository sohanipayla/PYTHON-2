import pandas as pd
df = pd.DataFrame({
 "Salary":[20000,22000,21000,25000,24000,300000]
})
# Calculate Q1, Q3 and IQR
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1
# Detect outliers
outliers = df[(df["Salary"] < Q1 - 1.5*IQR) | (df["Salary"] > Q3 + 1.5*IQR)]
print("Outliers:")
print(outliers)
# Remove outliers
df_clean = df[(df["Salary"] >= Q1 - 1.5*IQR) & (df["Salary"] <= Q3 + 1.5*IQR)]
print("\nCleaned Data:")
print(df_clean)