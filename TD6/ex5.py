import pandas as pd

df = pd.DataFrame({'A': ['a', 'b', 'b'], 'B': ['yes', 'no', 'no'], 'val1': [4, 2, 5], 'val2': [7, 8, 10], 'val3': [9, 3, 15]})
print(df.melt(id_vars = ['A', 'B'], var_name = 'myParam', value_name = 'myValue'))