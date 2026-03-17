import pandas as pd
df = pd.DataFrame({
 "Dept":["IT","IT","HR","HR","Finance","Finance"],
 "Employee":["A","B","C","D","E","F"],
 "Experience":[2,5,3,7,4,6]
})
# 1. Number of employees per department
count_emp = df.groupby("Dept").size()
print(count_emp)
# 2. Employee with highest experience (using sorting)
top_emp = df.sort_values(by=["Dept","Experience"], ascending=[True, False]).groupby("Dept").nth(0)
print(top_emp)