import pandas as pd

df = pd.DataFrame({'A': ['a', 'a', 'b', 'b', 'c', 'c'], 'T': ['yes', 'no', 'yes', 'no', 'yes', 'no'], 'V': [4, 2, 5, 2, 7, 3]})
df1 = df.pivot(index = 'A', columns = 'T', values = 'V')

print(df1)