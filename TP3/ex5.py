import numpy as np

import numpy.random as rg

a = np.floor(10 * rg.random((3, 15)))

c = np.hsplit(a, 3)

d = np.hsplit(a, (3, 4))
print(c)
print(d)