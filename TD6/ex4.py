import pandas as pd

df = pd.DataFrame({'A': [5, 4, 1], 'B': [8, 9, 6]})
print(df.stack())
print(df)
df.rename(columns = {'A':'C', 'B' : 'D'}, inplace = True)
df2 = df.stack().reset_index(level = 1)

print(df2.columns)
print(df2)