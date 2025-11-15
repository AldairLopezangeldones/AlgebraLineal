
def normali_vector(x):
    norm = sum(xi*xi for xi in x)**0.5
    return [xi/norm for xi in x]

print(normali_vector([3,4,10]))
