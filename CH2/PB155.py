import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
"StudyHours":[2,3,5,6,8],
"Marks":[50,60,75,85,95],
"Gender":["M","F","M","F","M"]
})
df["Grade"] = np.where(df["Marks"] >= 80, "A",
np.where(df["Marks"] >= 60, "B", "C"))
sns.scatterplot(x="StudyHours", y="Marks",
hue="Grade", style="Gender", data=df)
plt.title("Study Hours vs Marks")
plt.show()