def transformacion_lineal_simple(X, W, b):
    
    def multiplicar_matrices(A, B):
        filas_A = len(A)
        columnas_A = len(A[0])
        columnas_B = len(B[0])
        
        resultado = [[0.0 for _ in range(columnas_B)] for _ in range(filas_A)]
        
        for i in range(filas_A):
            for j in range(columnas_B):
                for k in range(columnas_A):
                    resultado[i][j] += A[i][k] * B[k][j]
        return resultado
    
    
    Y = multiplicar_matrices(X, W)
    
    
    for i in range(len(Y)):
        for j in range(len(Y[0])):
            Y[i][j] += b[j]
    
    return Y


X = [[1, 2, 3],
     [4, 5, 6]]

W = [[0.1, 0.2],
     [0.3, 0.4],
     [0.5, 0.6]]

b = [0.1, 0.2]

Y = transformacion_lineal_simple(X, W, b)


for fila in Y:
    print([round(x, 6) for x in fila])