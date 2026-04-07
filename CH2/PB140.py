import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("https://raw.githubusercontent.com/kavit88/Data-Sets/main/car_data.csv")
# Horsepower vs Price
sns.scatterplot(data=data, x='Horsepower', y='Price')
plt.show()
# Mileage vs Price
sns.scatterplot(data=data, x='Mileage', y='Price')
plt.show()
# Weight vs Price
sns.scatterplot(data=data, x='Weight', y='Price')
plt.show()