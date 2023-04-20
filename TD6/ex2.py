import pandas as pd

df1 = pd.DataFrame({'A': [3, 5], 'B': [1, 2]}) 
df2 = pd.DataFrame({'A': [6, 7], 'C': [4, 9]})

pd.concat([df1, df2], axis = 1)

pd.merge(df1, df2)

pd.merge(df1, df2, how = 'outer')

df1.join(df2)

df1.join(df2, how = 'outer')

