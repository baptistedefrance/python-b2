import pandas as pd
import numpy as np

s = pd.Series([1, 5, 3, 9,np.nan])
s[s < 5] = 99
s[np.isnan(s)] = 100
print(s)