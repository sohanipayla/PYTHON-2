import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('https://raw.githubusercontent.com/kavit88/Data-Sets/main/student_scores.csv')
corr=df[['Maths','Science','English']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Student Scores')
plt.show()