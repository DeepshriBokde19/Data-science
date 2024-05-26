import numpy as np


arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([4, 3, 2, 1])


greater = np.greater(arr1, arr2)
greater_equal = np.greater_equal(arr1, arr2)
less = np.less(arr1, arr2)
less_equal = np.less_equal(arr1, arr2)


print("Greater:\n", greater)
print("Greater Equal:\n", greater_equal)
print("Less:\n", less)
print("Less Equal:\n", less_equal)
