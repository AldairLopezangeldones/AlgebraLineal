import numpy as np

A = np.array([[4, 1],
              [1, 3]])


autovalores, autovectores = np.linalg.eigh(A)

print("Autovalores:", autovalores)
print("Autovectores:\n", autovectores)
