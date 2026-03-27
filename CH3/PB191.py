import pandas as pd
df = pd.DataFrame({
    'age': [22, 35, 61, 45, 28]
})
def categorize_age(age):
    if age < 30:
        return 'Young'
    elif age > 60:
        return 'Elderly'
    else:
        return 'Middle-aged'
df['age_group'] = df['age'].apply(categorize_age)
print(df)