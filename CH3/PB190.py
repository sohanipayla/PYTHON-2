import pandas as pd
data = {
    'area': [1200, 1500, 1800, 2000],
    'price': [1800000, 2500000, 3200000, 2900000]
}
df = pd.DataFrame(data)
def categorize_price(price):
    if price > 3000000:
        return 'High'
    elif price < 2000000:
        return 'Low'
    else:
        return 'Medium'
df['price_category'] = df['price'].apply(categorize_price)
print(df)