import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)       # [1 2 3 4]
print(type(arr)) # <class 'numpy.ndarray'>
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
# [[1 2 3]
#  [4 5 6]]
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)  # (2, 3)
print(arr.size)   # 6
print(arr.ndim)   # 2
print(arr.dtype)  # data type (e.g., int32)
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)  # (2, 3)
print(arr.size)   # 6
print(arr.ndim)   # 2
print(arr.dtype)  # data type (e.g., int32)
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)   # [5 7 9]
print(a - b)   # [-3 -3 -3]
print(a * b)   # [4 10 18]
print(a / b)   # [0.25 0.4 0.5]
print(a ** 2)  # [1 4 9]
