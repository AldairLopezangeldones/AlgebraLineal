import numpy as np

vectores = np.array([[1, 2],
                     [3, 4],
                     [5, 6]])


promedio = np.mean(vectores, axis=0)
print(promedio)
