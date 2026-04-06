import pandas as pd
import numpy as np

# Sample DataFrame (already given in question)
# df = pd.read_csv("your_file.csv")

df['Category'] = np.where(df['price'] > 3000000, 'High',
                  np.where(df['price'] < 2000000, 'Low', 'Medium'))

print(df)
