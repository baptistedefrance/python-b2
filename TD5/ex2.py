import pandas as pd

df = pd.DataFrame({'A':[0, 1, 2], 'B':[3, 4, 5], 'C':[6, 7, 8]}, index = ['a', 'b', 'c'])
df.columns = ['D', 'G', 'H']
df.rename(columns = {'D': 'A'}, inplace = True)
df.rename(index = {'b': 'm'}, inplace = True)
df.reindex(columns = ['G', 'H', 'A'], index=['c', 'a', 'm'])
print(df.iloc[2,1])
print(df)