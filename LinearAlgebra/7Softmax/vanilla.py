
def solve(x):
    e = 2.718281828
    ex = [e**xi for xi in x]
    s = sum(ex)
    return [v/s for v in ex]

print(solve([1,2,3]))
