import numpy as np

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])


s_coseno = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
print(s_coseno)  
