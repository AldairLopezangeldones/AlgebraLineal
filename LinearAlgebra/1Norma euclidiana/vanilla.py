
def solve(x):
    s = 0
    for xi in x:
        s += xi * xi
    return s ** 0.5

print(solve([3, 4]))
