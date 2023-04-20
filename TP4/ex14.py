import pandas as pd
import numpy as np
df = pd.DataFrame({'A':[0, 1, 5], 'B':[2, 3, 6]}, index = ['a', 'b', 'c'])

#print(df['B'])
print(df.at['c', 'B'])
#print(df.loc['a'])
#df.at['c', 'B'] = 96
#print(df)
#print(df['A'])
c = df['A']