def raiz_cuadrada(x, tol=1e-10):
    
    r = x
    while abs(r*r - x) > tol:
        r = (r + x/r) / 2
    return r

def autovalores_autovectores_2x2(A):
    a, b = A[0]
    c, d = A[1]
    
    if b != c:
        raise ValueError("La matriz no es simétrica")
    
    # autovalores
    traza = a + d
    determinante = a*d - b*b
    discriminante = raiz_cuadrada(traza*traza - 4*determinante)
    lam1 = (traza + discriminante) / 2
    lam2 = (traza - discriminante) / 2
    
    # autovectores
    if b != 0:
        v1 = [b, lam1 - a]
        v2 = [b, lam2 - a]
    else:
        v1 = [1, 0]
        v2 = [0, 1]
    
    return [(lam1, v1), (lam2, v2)]

# prueba
A = [[4, 1],
     [1, 3]]

pares = autovalores_autovectores_2x2(A)
for lam, vec in pares:
    print("Autovalor:", lam)
    print("Autovector:", vec)
