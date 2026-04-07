import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("https://raw.githubusercontent.com/kavit88/Data-Sets/main/temperatures.csv")
sns.boxplot(data)
plt.show()