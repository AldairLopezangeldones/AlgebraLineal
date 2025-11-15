
def prod_punto(u, v):
    total = 0
    for i in range(len(u)):
        total += u[i] * v[i]
    return total

print(prod_punto([1,2,3],[4,5,6]))
