import pandas as pd
df = pd.DataFrame({
 "Employee":["A","B","C","D","E"],
 "Dept":["IT","HR","IT","Finance","HR"],
 "Salary":[50000,40000,70000,80000,45000]
})
# Group by Dept and calculate total & average salary
result = df.groupby("Dept")["Salary"].agg(["sum","mean"])
print(result)
# Filter departments where average salary > 50000
filtered = result[result["mean"] > 50000]
print(filtered)