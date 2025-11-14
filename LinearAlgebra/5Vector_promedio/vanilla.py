
def solve(vectors):
    m = len(vectors)
    n = len(vectors[0])
    mean = [0]*n

    for vec in vectors:
        for j in range(n):
            mean[j] += vec[j]

    return [x/m for x in mean]

print(solve([[1,2],[3,4],[5,6]]))
