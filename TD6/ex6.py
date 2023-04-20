import pandas as pd

df = pd.DataFrame({'A': ['a', 'b', 'a', 'a', 'b'], 'B': [8, 4, 5, 10, 8], 'C': ['x', 'x', 'y', 'y', 'x'], 'D': [0, 1, 2, 3, 4]})
print(df.groupby('A'))
print(df.groupby(['A', 'C']).sum().reset_index())