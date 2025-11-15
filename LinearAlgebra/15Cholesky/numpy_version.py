import numpy as np

K = np.array([[4, 2],
              [2, 5]])


L = np.linalg.cholesky(K)
print("Matriz L (Cholesky):\n", L)

K_reconstruida = L @ L.T
print("K reconstruida:\n", K_reconstruida)

print("¿K == L * Lᵀ?", np.allclose(K, K_reconstruida))
