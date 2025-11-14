
def solve(u, v):
    total = 0
    for i in range(len(u)):
        total += u[i] * v[i]
    return total

print(solve([1,2,3],[4,5,6]))
