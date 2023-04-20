import pandas as pd

df = pd.DataFrame({'A':[0, 1, 2], 'B':[3, 4, 5], 'C':[6, 7, 8]}, index = ['a', 'b', 'c'])
print(df)
df['E'] = pd.Series([1, 0, 1], index = ['a1', 'a2', 'a3'])
df['D'] = 0
df.insert(0, 'F', [1, 2, 3])
print(df)