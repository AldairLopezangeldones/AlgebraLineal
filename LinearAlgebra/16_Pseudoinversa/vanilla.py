def pseudoinversa_simple(X):
  
    
    def transponer(M):
        return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    
    
    def multiplicar_matrices(A, B):
        resultado = [[0.0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    resultado[i][j] += A[i][k] * B[k][j]
        return resultado
    
    
    def invertir_2x2(M):
        a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
        determinante = a * d - b * c
        if abs(determinante) < 1e-10:
            return [[1, 0], [0, 1]]  # Aproximacion si es singular
        return [[d/determinante, -b/determinante], [-c/determinante, a/determinante]]
    
    X_T = transponer(X)
    X_T_X = multiplicar_matrices(X_T, X)
    inv_X_T_X = invertir_2x2(X_T_X)
    X_plus = multiplicar_matrices(inv_X_T_X, X_T)
    
    return X_plus


X = [[10, 2],
     [1, 3],
     [4, 7]]  # Matriz 3x2

print("Matriz X (3x2):")
for fila in X:
    print(fila)

X_plus = pseudoinversa_simple(X)


for fila in X_plus:
    print([round(x, 6) for x in fila])


def multiplicar_matrices_simple(A, B):
    """Multiplicación simplificada"""
    resultado = [[0.0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                resultado[i][j] += A[i][k] * B[k][j]
    return resultado

I_aproximada = multiplicar_matrices_simple(X_plus, X)

for fila in I_aproximada:
    print([round(x, 6) for x in fila])