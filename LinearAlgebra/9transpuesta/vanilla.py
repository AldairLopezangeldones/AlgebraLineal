
def transpuesta(A):
    m = len(A)
    n = len(A[0])
    T = [[0]*m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            T[j][i] = A[i][j]

    return T

print(transpuesta([[12,9],[10,5]]))
