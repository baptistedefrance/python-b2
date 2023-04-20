import pandas as pd

df1 = pd.DataFrame({'A': [9, 50], 'B': [51, 92]}, index = [1, 2]) 
df2 = pd.DataFrame({'A': [64, 77], 'B': [24, 93]}, index = [1, 2])

print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], ignore_index = True))
df3 = pd.concat([df1, df2], keys = ['a', 'b'])



