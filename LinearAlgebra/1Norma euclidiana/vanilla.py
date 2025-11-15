
def norma_ecludiana(x):
    s = 0
    for xi in x:
        s += xi * xi
    return s ** 0.5

print(norma_ecludiana([5, 12, 5])) 
