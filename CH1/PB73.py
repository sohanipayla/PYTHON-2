import pandas as pd
df = pd.DataFrame({
 "Dept":["IT","IT","HR","HR","Finance","Finance"],
 "Salary":[50000,70000,40000,60000,80000,75000]
})
# Group by Dept and calculate mean, median, max
result = df.groupby("Dept")["Salary"].agg(["mean","median","max"])
print(result)