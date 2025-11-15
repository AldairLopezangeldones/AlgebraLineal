import numpy as np

X = np.array([[10, 2],
              [1, 3],
              [4, 7]])

print("Matriz X:\n", X)


X_plus = np.linalg.pinv(X)
print(X_plus)


I_aproximada = X_plus @ X
print(I_aproximada)
