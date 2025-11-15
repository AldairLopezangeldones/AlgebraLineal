import numpy as np

A = np.array([[3, 0],
              [0, -2]])


U, S, V_T = np.linalg.svd(A, full_matrices=True)

print("Matriz A:\n", A)
print("U =\n", U)
print("S =", S)
print("V_T =\n", V_T)
