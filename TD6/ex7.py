import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5],'C': [6, 7, 8], 'D': [9, 10, 11]})

print(df.groupby('A').agg(min_B = ('B', min), max_B = ('B', 'max'), median_D = ('D', np.median)))