import pandas as pd
import numpy as np

df = pd.DataFrame({'A':[0, 1, 5], 'B':[2, 3, 6]}, index = ['a', 'b', 'c'])

print(df>2)
print(df[df>2])