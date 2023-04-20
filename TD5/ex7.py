import pandas as pd
df = pd.DataFrame({'A':[1, 4, 7], 'B':[2, 5, 8], 'C':[3, 6, 9]}, index = ['a', 'b', 'c'])
df.add(df['A'], axis = 0)
df.add(df.iloc[0], axis = 1)
print(df - df.mean())
print(df.sub(df.mean(axis = 1), axis = 0))
print(df)
