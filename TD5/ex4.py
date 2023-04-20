import pandas as pd

df = pd.DataFrame({'A':[0, 1, 2], 'B':[3, 4, 5], 'C':[6, 7, 8]}, index = ['a', 'b', 'c'])

del df['A']
df.drop(['a', 'c'], inplace = True)

df = pd.DataFrame({'A':[0, 1, 2], 'B':[3, 4, 5], 'C':[6, 7, 8]}, index = ['a', 'b', 'c'])
s = df.pop('B')
print(df)
print(s)