import pandas as pd
import numpy as np

df['Age_Group'] = np.where(df['age'] < 30, 'Young',
                    np.where(df['age'] <= 60, 'Middle-aged', 'Elderly'))

print(df)
