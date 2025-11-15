import numpy as np

X = np.array([[1, 2, 3],
              [4, 5, 6]])

W = np.array([[0.1, 0.2],
              [0.3, 0.4],
              [0.5, 0.6]])

b = np.array([0.1, 0.2])


Y = X @ W + b  

print("Y =\n", Y.round(6))
