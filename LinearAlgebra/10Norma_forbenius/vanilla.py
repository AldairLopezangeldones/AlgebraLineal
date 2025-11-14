
def solve(A, B):
    total = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            diff = A[i][j]-B[i][j]
            total += diff*diff
    return total**0.5

print(solve([[1,2],[3,4]], [[1,1],[1,1]]))
