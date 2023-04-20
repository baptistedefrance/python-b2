import numpy as np

tab = np.array([[10,20,30],
                [40,50,60]])

a = np.array([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(np.size(tab))
print(np.shape(tab))
print(np.size(a))

a.shape = (3,4)
print(a)



