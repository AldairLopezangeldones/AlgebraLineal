
def pro_punto(u, v):
    return sum(u[i]*v[i] for i in range(len(u)))

def norma(x):
    return sum(xi*xi for xi in x)**0.5

def s_coseno(u, v):
    return pro_punto(u,v) / (norma(u)*norma(v))

print(s_coseno([1,2,3],[4,5,6]))
