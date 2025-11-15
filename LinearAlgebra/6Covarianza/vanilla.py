
def matriz_covarianza(vectores):
    m = len(vectores)
    n = len(vectores[0])
    promedio = [sum(v[i] for v in vectores)/m for i in range(n)]

    cov = [[0]*n for _ in range(n)]

    for v in vectores:
        diff = [v[i]-promedio[i] for i in range(n)]
        for i in range(n):
            for j in range(n):
                cov[i][j] += diff[i]*diff[j]

    return [[cov[i][j]/m for j in range(n)] for i in range(n)]

print(matriz_covarianza([[1,2],[3,4],[5,6]]))
