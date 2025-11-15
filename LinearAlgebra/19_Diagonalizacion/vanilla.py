def diagonalizable_simple(A):
    
    n = len(A)
    
    
    es_diagonal = True
    for i in range(n):
        for j in range(n):
            if i != j and abs(A[i][j]) > 1e-10:
                es_diagonal = False
                break
    
    if es_diagonal:
        P = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
        D = [[A[i][j] if i == j else 0.0 for j in range(n)] for i in range(n)]
        return True, P, D
    
    
    if n == 2 and A[0][1] == A[1][0]:
        # Autovalores aproximados
        traza = A[0][0] + A[1][1]
        determinante = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        
        lambda1 = (traza + (traza**2 - 4*determinante)**0.5) / 2
        lambda2 = (traza - (traza**2 - 4*determinante)**0.5) / 2
        
        D = [[lambda1, 0.0], [0.0, lambda2]]
        
        
        if abs(A[0][1]) > 1e-10:
            P = [[1.0, 1.0], 
                 [(lambda1 - A[0][0])/A[0][1], (lambda2 - A[0][0])/A[0][1]]]
        else:
            P = [[1.0, 0.0], [0.0, 1.0]]
            
        return True, P, D
    
    
    return False, [], []


A = [[6, 1],
     [2, 3]]

es_diag, P, D = diagonalizable_simple(A)

print("Matriz A:")
for fila in A:
    print(fila)

if es_diag:
    print(" A es diagonalizable")
    print("\nMatriz P:")
    for fila in P:
        print([round(x, 6) for x in fila])
    print("\nMatriz D (diagonal):")
    for fila in D:
        print([round(x, 6) for x in fila])
else:
    print("✗ A no es diagonalizable")
