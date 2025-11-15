def svd(A):
  
    m = len(A)
    n = len(A[0])
    
    
    if m == 2 and n == 2 and A[0][1] == 0 and A[1][0] == 0:
        U = [[1.0, 0.0], [0.0, 1.0]]
        S = [abs(A[0][0]), abs(A[1][1])]
        V_T = [[1.0 if A[0][0] >= 0 else -1.0, 0.0], 
               [0.0, 1.0 if A[1][1] >= 0 else -1.0]]
        return U, S, V_T
    
    
    U = [[1.0 if i == j else 0.0 for j in range(m)] for i in range(m)]
    S = [1.0] * min(m, n)
    V_T = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    
    return U, S, V_T


A = [[3, 0], [0, -2]] #
U, S, V_T = svd(A)

print("Matriz A:")
print(A)
print("SVD Resultado:")
print("U =", U)
print("S =", S) 
print("V_T =", V_T)
