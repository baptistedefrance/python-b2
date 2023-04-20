import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [9, 8, 7]})

print(df.apply(lambda x: x + 1))
print(df.apply(lambda x: x.max()))