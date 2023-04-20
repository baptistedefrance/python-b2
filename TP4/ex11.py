import pandas as pd
import numpy as np

s = pd.Series([10, 20, 30])

cd = s.to_frame(name = 'A')

print(cd)