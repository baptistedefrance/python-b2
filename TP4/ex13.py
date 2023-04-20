import pandas as pd
import numpy as np

s1 = pd.Series([2, 3, 4], index = ['a', 'b', 'c'])

s2 = pd.Series([6, 7, 8], index = ['b', 'a', 'd'])

df = pd.DataFrame({'col1': s1, 'col2': s2})

print(df)