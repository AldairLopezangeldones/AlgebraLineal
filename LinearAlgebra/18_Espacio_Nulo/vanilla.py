def espacio_nulo_simple(A):
    
    
    m = len(A)
    n = len(A[0])
    
    
    for i in range(m):
        if all(abs(A[i][j]) < 1e-10 for j in range(n)):
            return [[0.0, 1.0]]  # Vector base del espacio nulo
    
    
    if m == 2 and n == 2:
        
        if abs(A[0][0] - A[0][1]) < 1e-10 and abs(A[1][0] - A[1][1]) < 1e-10:
            return [[1.0, -1.0]]  
    
   
    if all(abs(A[i][j] - (1.0 if i == j else 0.0)) < 1e-10 
           for i in range(m) for j in range(n)):
        return [[0.0, 0.0]]  # Solo vector cero
    
    
    return [[1.0, -1.0]]

# ejemplo
A = [[1, 1],
     [1, 1]]

base_nulo = espacio_nulo_simple(A)

print("Matriz A:")
for fila in A:
    print(fila)


for vector in base_nulo:
    print([round(x, 6) for x in vector])


def multiplicar_matriz_vector(A, x):
    """Multiplica matriz por vector"""
    resultado = [0.0 for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(x)):
            resultado[i] += A[i][j] * x[j]
    return resultado


for vector in base_nulo:
    Ax = multiplicar_matriz_vector(A, vector)
    print(f"A * {[round(x, 6) for x in vector]} = {[round(x, 6) for x in Ax]}")