import pandas as pd
import numpy as np

s = pd.Series(['a', 'b', 'c'])

print(s.isin(['a', 'c', 'x']))

