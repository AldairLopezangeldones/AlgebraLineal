import numpy as np

x = np.array([6, 3, 5])

ex = np.exp(x)
softmax = ex / np.sum(ex)
print(softmax)
