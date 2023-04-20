import pandas as pd
import numpy as np
s = pd.Series([1, 2, 5, 7], index = ['a', 'b', 'c', 'd'])
print(s.reindex(['c', 'b', 'a', 'e']))

print(s)
