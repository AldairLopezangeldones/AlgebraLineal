def forma_cuadratica_simple(A, x, b):
    
    n = len(x)
    
    
    def valor_f(A, x, b):
        
        xAx = 0.0
        for i in range(n):
            for j in range(n):
                xAx += x[i] * A[i][j] * x[j]
        
        
        bTx = 0.0
        for i in range(n):
            bTx += b[i] * x[i]
        
        return 0.5 * xAx - bTx
    
    
    def gradiente(A, x, b):
        grad = [0.0] * n
        for i in range(n):
           
            Ax_i = 0.0
            for j in range(n):
                Ax_i += A[i][j] * x[j]
            grad[i] = Ax_i - b[i]
        return grad
    
    
    def hessiana(A):
        return A
    
    f = valor_f(A, x, b)
    grad_f = gradiente(A, x, b)
    hess_f = hessiana(A)
    
    return f, grad_f, hess_f


A = [[2, 1],
     [1, 3]] 

x = [1, 2]   
b = [1, 1]    

f, grad, hess = forma_cuadratica_simple(A, x, b)

print("Matriz A:")
for fila in A:
    print(fila)
print(f"\nVector x: {x}")
print(f"Vector b: {b}")

print(f"= {f:.6f}")

print(f"funcion {[round(g, 6) for g in grad]}")


for fila in hess:
    print([round(h, 6) for h in fila])