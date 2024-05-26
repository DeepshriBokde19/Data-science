import numpy as np


arr = np.array([1, 2, 3, 4, 5])


none_zero = np.all(arr != 0)

print("None of the elements are zero:", none_zero)
