import numpy as np

A = np.array([[1, 1],
              [1, 2],
              [1, 3]])
b = np.array([1, 2, 2])


x_sol = np.linalg.lstsq(A, b, rcond=None)[0]
print("Solución de mínimos cuadrados:", x_sol)


b_aproximado = A @ x_sol
print("b aproximado:", b_aproximado)
print("b original:   ", b)
