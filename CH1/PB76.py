import pandas as pd
df = pd.DataFrame({
 "Dept":["IT","IT","HR","HR","Finance","Finance"],
 "Employee":["A","B","C","D","E","F"],
 "City":["X","X","Y","Z","X","Y"]
})
# 1. Number of unique cities per department
unique_cities = df.groupby("Dept")["City"].nunique()
print(unique_cities)
# 2. One random employee per department
random_emp = df.groupby("Dept").apply(lambda x: x.sample(1))
print(random_emp)