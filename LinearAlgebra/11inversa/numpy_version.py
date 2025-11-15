import numpy as np  

A2 = np.array([[12, 10],
               [18, 9]])

try:
    inv2 = np.linalg.inv(A2)
    print("Inversa 2x2:\n", inv2)
except np.linalg.LinAlgError:
    print("No invertible")


A3 = np.array([[2, 1, 3],
               [1, 0, 2],
               [3, 4, 1]])

try:
    inv3 = np.linalg.inv(A3)
    print("Inversa 3x3:\n", inv3)
except np.linalg.LinAlgError:
    print("No invertible")
