import pandas as pd
df = pd.DataFrame({
    'income': [25000, 40000, 75000, 60000, 20000]
})
def categorize_income(income):
    if income < 30000:
        return 'Low'
    elif income > 70000:
        return 'High'
    else:
        return 'Medium'
df['income_group'] = df['income'].apply(categorize_income)
print(df)