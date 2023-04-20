import numpy as np
a = np.arange(1, 6)
a.shape = (1, np.size(a))
print(a)
a.shape = (np.size(a),1)
print(a)
