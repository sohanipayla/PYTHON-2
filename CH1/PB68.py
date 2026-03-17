import pandas as pd
data = {
 "EmpID":[101,102,103,104,105],
 "Dept":["IT","HR","IT","Finance","HR"],
 "Salary":[60000,45000,80000,75000,50000],
 "Age":[25,32,29,41,28]
}
df = pd.DataFrame(data)
# Sort by Dept (Ascending) and Salary (Descending)
df1 = df.sort_values(by=['Dept','Salary'], ascending=[True, False])
# Sort index in descending order
df2 = df1.sort_index(ascending=False)
print(df2)