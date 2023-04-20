import pandas as pd
import numpy as np

df = pd.DataFrame({'A':[0, 1, 2], 'B':[3, 4, 5], 'C':[6, 7, 8]}, index = ['a', 'b', 'c'])

df['B'] = df['B'].apply(lambda x: np.nan if x < 5 else x)
print(df)