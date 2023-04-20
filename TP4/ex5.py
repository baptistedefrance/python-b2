import pandas as pd
import numpy as np

s = pd.Series([2, 5, 7, 3], index = ['e', 'b', 'c', 'd'])

s = s.loc[sorted(s.index)]

print(s)