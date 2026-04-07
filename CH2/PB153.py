import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
"Dept":["IT","IT","HR","HR","Finance","Finance"],
"Salary":[50000,70000,40000,60000,80000,75000],
"Gender":["M","F","M","F","M","F"]
})
sns.boxplot(x="Dept", y="Salary", hue="Gender", data=df)
plt.title("Salary Distribution by Department and Gender")
plt.show()