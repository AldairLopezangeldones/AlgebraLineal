import numpy as np

A = np.array([[5, 10],
              [7, 4]])
B = np.array([[1, 1],
              [1, 1]])


norma_f = np.linalg.norm(A - B)
print(norma_f)  
