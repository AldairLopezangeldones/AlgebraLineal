
def solve(x):
    norm = sum(xi*xi for xi in x)**0.5
    return [xi/norm for xi in x]

print(solve([3,4]))
