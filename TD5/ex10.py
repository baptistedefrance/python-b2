import pandas as pd

df = pd.DataFrame({'A': [1.1, 2.7, 5.3], 'B': [2, 10, 9], 'C': [3.3, 5.4, 1.5], 'D': [4, 7, 15]}, index = ['a1', 'a2', 'a3'])
result = df.idxmin(axis=1)
result2 = df.idxmin(axis=0)

print(result)
print(df)
print(df.quantile(0.9))
print(df.quantile([0.25, 0.5, 0.75]))
print(df.cumsum())
print(df.cumsum(axis = 1))
