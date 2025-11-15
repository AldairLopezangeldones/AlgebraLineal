
def vector_prom(vectores):
    m = len(vectores)
    n = len(vectores[0])
    promedio = [0]*n

    for vec in vectores:
        for j in range(n):
            promedio[j] += vec[j]

    return [x/m for x in promedio]

print(vector_prom([[1,2],[3,4],[5,6]]))
