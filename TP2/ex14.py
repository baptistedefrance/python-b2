import numpy as np
x = np.arange(0, 1000, 100)
print(x[(x > 200) & (x < 800)])
