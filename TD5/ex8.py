import pandas as pd 
df = pd.DataFrame({'Ex':[0, 1, 2], 'Ab':[3, 4, 5], 'Bio':[6, 7, 8]}, index = ['test', 'puis', 'quid'])
df1 = df.sort_index(axis = 0, ascending = True)
df2 = df.sort_index(axis = 0, ascending = False)
df3 = df.sort_index(axis = 1, ascending = True)
df4 = df.sort_index(axis = 1, ascending = False)
df5 = df.sort_index(axis = 0, ascending = True).sort_index(axis = 1, ascending = True)
df6 = df = df.sort_values(by='Bio', ascending=False)
print(df1)