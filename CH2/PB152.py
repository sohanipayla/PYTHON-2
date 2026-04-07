import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
corr = pd.DataFrame({
"Height":[150,160,170,180,175],
"Weight":[50,60,65,75,70],
"Age":[20,22,25,30,28],
"BMI":[22,24,23,26,25]
}).corr()

sns.heatmap(corr, cmap="YlGnBu", annot=True)
plt.title("Correlation Heatmap")
plt.show()