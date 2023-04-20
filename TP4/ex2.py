import pandas as pd
import numpy as np
s = pd.Series(['a', 'b', 'c'])
print(s.replace({'a': 'A', 'b': 'B', 'c': 'C'}))

