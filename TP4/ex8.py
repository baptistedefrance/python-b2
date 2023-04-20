import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, 3, 5, 2, 8, 3, 1, 7, 4, 2, 3, 6, 3])

s2 = s.value_counts()

print(s2)