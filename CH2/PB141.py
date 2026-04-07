import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("https://raw.githubusercontent.com/kavit88/Data-Sets/main/house_data.csv")
# Lot size vs Price
sns.scatterplot(data=data, x='LotSize', y='Price')
plt.title("Lot Size vs Price")
plt.show()
# Square footage vs Price
sns.scatterplot(data=data, x='SqFt', y='Price')
plt.title("Square Footage vs Price")
plt.show()