import pandas as pd
import numpy as np

s1 = pd.Series([1, 2, 3], ['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], ['a', 'd', 'c'])

print((s1 + s2).dropna())