import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Create DataFrame
df = pd.DataFrame({
"Math":[78,85,90,66,88],
"Science":[80,82,89,70,85],
"English":[75,88,92,60,84],
"Computer":[90,91,95,72,89]
}, index=["S1","S2","S3","S4","S5"])
# Plot Heatmap
sns.heatmap(
df,
annot=True, cmap="coolwarm",linewidths=1, linecolor="black", cbar=True)
plt.title("Student Marks Heatmap")
plt.show()