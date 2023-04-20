import numpy as np

import numpy.random as rg

a = np.floor(10 * rg.random((2, 2)))

b = np.floor(10 * rg.random((2, 2)))

c = np.vstack((a, b))

print(c)


