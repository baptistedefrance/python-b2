import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [np.nan, 20, 30], 'C': [7, 6, 5], 'D': [np.nan, np.nan, np.nan]})

#df.dropna(how = 'all', axis = 0)
#print(df)
df.dropna(how = 'all', axis = 1, inplace=True)
print(df)