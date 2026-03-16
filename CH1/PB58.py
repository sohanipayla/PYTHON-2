import pandas as pd
data = {
    'sales': [50000, 52000, 49000, 72000, 67000, 65000, 67000, 200000],
    'expenses': [42000, 43000, 42000, 39000, 39000, 50000, 45000, 100000]
}
df = pd.DataFrame(data)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
Low=Q1-(1.5*IQR)
High=Q3+(1.5*IQR)
df_clean = df[(df< Low) | (df > High)]
print(df_clean)