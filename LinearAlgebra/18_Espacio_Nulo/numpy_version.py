import numpy as np

A = np.array([[1, 1],
              [1, 1]])


U, S, Vt = np.linalg.svd(A)
tolerancia = 1e-10
n = A.shape[1]


null_mask = (S <= tolerancia)
if not np.any(null_mask):
    null_space = Vt[S.size:].T  
else:
    null_space = Vt[-(n - np.sum(S > tolerancia)):].T

null_space = Vt[1:] 
print("Base del espacio nulo:")
print(null_space)


for v in null_space:
    print("A * v =", A @ v)
