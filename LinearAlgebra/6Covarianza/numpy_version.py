import numpy as np

vectores = np.array([[1, 2],
                     [3, 4],
                     [5, 6]])


cov_matrix = np.cov(vectores, rowvar=False, bias=True)
print(cov_matrix)
