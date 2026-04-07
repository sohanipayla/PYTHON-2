import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1)
df = pd.read_csv("https://raw.githubusercontent.com/kavit88/Data-Sets/main/heights_weights.csv")
print(df.head())
print()

# 2)
df.info()
print()

# 3)
df.describe()
print()

# 4)
corr = df.corr(numeric_only=True)
print(corr)
print()

plt.figure(figsize=(8,4))
sns.boxplot(data=df[["Height","Weight"]])
plt.title("Boxplot of Height and Weight")
plt.show()
print()

# 5)
Q1=df[["Height","Weight"]].quantile(0.25)
Q3 = df[["Height","Weight"]].quantile(0.75)

IQR = Q3 - Q1

df_clean = df[~((df[["Height","Weight"]] < (Q1 - 1.5 * IQR)) |
(df[["Height","Weight"]] > (Q3 + 1.5 * IQR))).any(axis=1)]

plt.figure(figsize=(8,4))
sns.boxplot(data=df_clean[["Height","Weight"]])
plt.title("Boxplot After Removing Outliers")
plt.show()
print()

# 6)
sns.scatterplot(x="Height", y="Weight", data=df)
plt.title("Weight vs Height")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()