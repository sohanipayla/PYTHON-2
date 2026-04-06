import pandas as pd
import numpy as np

df['Income_Group'] = np.where(df['income'] < 30000, 'Low',
                       np.where(df['income'] <= 70000, 'Medium', 'High'))

print(df)
