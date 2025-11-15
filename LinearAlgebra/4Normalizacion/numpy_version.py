import numpy as np

x = np.array([3, 4, 10])

x_normalizado = x / np.linalg.norm(x)
print(x_normalizado)
