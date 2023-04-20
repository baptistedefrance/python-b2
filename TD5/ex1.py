import pandas as pd

df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5], 'C': [6, 7, 8], 'D': [9, 10, 11]})
df.columns = pd.MultiIndex(levels = [['x', 'y'], ['X', 'Y']], codes = [[0, 0, 1, 1], [0, 1, 0, 1]])
print(df)
print(df.columns)
print(df.groupby(axis = 1, level = 0).sum())
df.columns = ['/'.join(x) for x in df.columns.values]
print(df)

