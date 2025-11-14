
def solve(vectors):
    m = len(vectors)
    n = len(vectors[0])
    mean = [sum(v[i] for v in vectors)/m for i in range(n)]

    cov = [[0]*n for _ in range(n)]

    for v in vectors:
        diff = [v[i]-mean[i] for i in range(n)]
        for i in range(n):
            for j in range(n):
                cov[i][j] += diff[i]*diff[j]

    return [[cov[i][j]/m for j in range(n)] for i in range(n)]

print(solve([[1,2],[3,4],[5,6]]))
