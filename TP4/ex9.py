import pandas as pd
import numpy as np


s = pd.Series([1, 2, 3, np.nan])

print(s.isna())