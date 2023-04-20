import numpy as np
import random
rg = np.random.default_rng(1)
a = np.floor(10 * rg.random((3, 4)))
print(a)
print(a.shape)
print(a.reshape(6, 2))