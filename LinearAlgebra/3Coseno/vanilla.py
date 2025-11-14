
def dot(u, v):
    return sum(u[i]*v[i] for i in range(len(u)))

def norm(x):
    return sum(xi*xi for xi in x)**0.5

def solve(u, v):
    return dot(u,v) / (norm(u)*norm(v))

print(solve([1,2,3],[4,5,6]))
