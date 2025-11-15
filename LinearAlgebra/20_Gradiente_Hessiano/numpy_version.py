import numpy as np

A = np.array([[2, 1],
              [1, 3]])
x = np.array([1, 2])
b = np.array([1, 1])

f = 0.5 * x.T @ A @ x - b.T @ x


grad = A @ x - b


hess = A  

print(" =", f)
print("gradiente =", grad)
print("hessiana:\n", hess)
