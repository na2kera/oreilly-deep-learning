import numpy as np

x = np.array([1, 2, 3])
print(x)

y = np.array([4, 5, 6])
print(y)

print(x + y)

A = np.array([[1, 2], [3, 4]])
print(A)
print(A.shape)
print(A.dtype)

B = np.array([[3, 0], [0, 6]])

print(A + B)

A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
print(A * B)