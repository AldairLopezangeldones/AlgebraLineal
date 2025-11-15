def minimos_cuadrados_simple(A, b):
    
    
    def transponer(M):
        return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    
    # multiplica matriz
    def multiplicar_matrices(A, B):
        resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    resultado[i][j] += A[i][k] * B[k][j]
        return resultado
    
    
    def invertir_2x2(M):
        a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
        determinante = a*d - b*c
        if determinante == 0:
            return [[1, 0], [0, 1]]  # Pseudoinversa aproximada
        return [[d/determinante, -b/determinante], [-c/determinante, a/determinante]]
    
    A_T = transponer(A)
    A_T_A = multiplicar_matrices(A_T, A)
    A_T_b = multiplicar_matrices(A_T, [[bi] for bi in b])
    
   
    inv_A_T_A = invertir_2x2(A_T_A)
    
    
    x_estrella = multiplicar_matrices(inv_A_T_A, A_T_b)
    
    return [x[0] for x in x_estrella]


A = [[1, 1], [1, 2], [1, 3]]  
b = [1, 2, 2]                 

x_sol = minimos_cuadrados_simple(A, b)

print("A =", A)
print("b =", b)
print("\nSolución de mínimos cuadrados:")
print(" =", [round(x, 6) for x in x_sol])



def Ax(A, x):
    return [A[i][0]*x[0] + A[i][1]*x[1] for i in range(len(A))]

b_aproximado = Ax(A, x_sol)
print("=", [round(val, 6) for val in b_aproximado])
print("b   =", b)