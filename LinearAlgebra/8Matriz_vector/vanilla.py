
def prod_matriz_vector(A, x):
    m = len(A)
    n = len(A[0])
    y = [0]*m

    for i in range(m):
        for j in range(n):
            y[i] += A[i][j]*x[j]

    return y

print(prod_matriz_vector([[1,2],[3,4]], [5,6]))
