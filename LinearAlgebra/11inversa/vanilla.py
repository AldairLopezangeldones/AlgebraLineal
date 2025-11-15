
def inversa(A):
    n = len(A)
    if n == 2:
        det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
        if det == 0: return None
        inv = 1/det
        return [[ A[1][1]*inv, -A[0][1]*inv],
                [-A[1][0]*inv,  A[0][0]*inv]]
    elif n == 3:
        a,b,c = A[0]; d,e,f = A[1]; g,h,i = A[2]
        det = a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
        if det == 0: return None
        adj = [[ e*i-f*h, -(b*i-c*h),  b*f-c*e],
               [-(d*i-f*g), a*i-c*g, -(a*f-c*d)],
               [ d*h-e*g, -(a*h-b*g), a*e-b*d]]
        return [[adj[r][c]/det for c in range(3)] for r in range(3)]
    else:
        raise NotImplementedError("Solo 2x2 y 3x3")

#Probando 
A2 = [[12,10],[18,9]]
inv2 = inversa(A2)
print("=", inv2 if inv2 else "No invertible")

A3 = [[2,1,3],[1,0,2],[3,4,1]]
inv3 = inversa(A3)
print("=", inv3 if inv3 else "No invertible")

