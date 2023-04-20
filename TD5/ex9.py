import pandas as pd
import numpy as np
df = pd.DataFrame({'A':[-0.12345, 1.32165], 'B':[4.46287, -3.98764]})
df = df.applymap(lambda x: round(abs(x), 2))
print(df)