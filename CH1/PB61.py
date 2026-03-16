import pandas as pd
import matplotlib.pyplot as plt

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

# 5. Check outliers using boxplot
df[['Height','Weight']].boxplot()
plt.title("Boxplot for Height and Weight (Outlier Detection)")
plt.show()