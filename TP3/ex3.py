import numpy as np

a = np.arange(40)

b = a.reshape(2,2,-1)

print(b.shape)

