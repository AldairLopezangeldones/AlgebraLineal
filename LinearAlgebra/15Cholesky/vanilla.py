def cholesky_simple(K):
    
    n = len(K)
    L = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1):
            suma = 0.0
            for k in range(j):
                suma += L[i][k] * L[j][k]
            
            if i == j:
                
                L[i][i] = (K[i][i] - suma) ** 0.5
            else:
                
                L[i][j] = (K[i][j] - suma) / L[j][j]
    
    return L

def transponer(M):
    """Transpone una matriz"""
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def multiplicar_matrices(A, B):
    """Multiplica dos matrices"""
    n = len(A)
    p = len(B[0])
    m = len(B)
    
    resultado = [[0.0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                resultado[i][j] += A[i][k] * B[k][j]
    return resultado


K = [[4, 2], [2, 5]]  # Matriz definida positiva

print("Matriz K (definida positiva):")
for fila in K:
    print(fila)

L = cholesky_simple(K)
print("\nDescomposición de Cholesky L:")
for fila in L:
    print([round(x, 6) for x in fila])


L_T = transponer(L)
K_reconstruida = multiplicar_matrices(L, L_T)


for fila in K_reconstruida:
    print([round(x, 6) for x in fila])

print("\n¿K == L * Lᵀ?", all(abs(K[i][j] - K_reconstruida[i][j]) < 1e-10 
                           for i in range(len(K)) for j in range(len(K[0]))))