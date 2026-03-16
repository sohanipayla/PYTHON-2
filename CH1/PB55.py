import pandas as pd
import numpy as np
data = {
    'name': ['William','Emma','Sofia','Markus','Edward','Thomas','Ethan',np.nan,'Arun','Anika','Paulo'],
    'region': [np.nan,'North','East',np.nan,'West','West','South',np.nan,'West','East','South'],
    'sales': [50000,52000,np.nan,np.nan,42000,72000,49000,np.nan,67000,65000,67000],
    'expenses': [42000,43000,np.nan,np.nan,38000,39000,42000,np.nan,39000,50000,45000]
}
df = pd.DataFrame(data)
print(df)
df_clean = df.dropna()
print(df_clean)