import pandas as pd
import numpy as np

s = pd.Series([1, 4, 3],['z', 'a', 'n'])

s2=s.apply(lambda x: 2 * x + 1)

print(s2)

