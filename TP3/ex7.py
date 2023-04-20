import numpy as np

a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])

unique_values = np.unique(a)

unique_values, indices_list = np.unique(a, return_index=True)

print(unique_values)

print(indices_list)