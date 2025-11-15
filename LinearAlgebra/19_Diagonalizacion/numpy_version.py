import numpy as np

A = np.array([[6, 1],
              [2, 3]])

autovalores, autovectores = np.linalg.eig(A)

D = np.diag(autovalores)
P = autovectores


A_reconstruida = P @ D @ np.linalg.inv(P)
es_diagonalizable = np.allclose(A, A_reconstruida)

print("A es diagonalizable:", es_diagonalizable)
print("Matriz P (autovectores):\n", P)
print("Matriz D (diagonal):\n", D)
