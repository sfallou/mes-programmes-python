from math import *
def iteratif(A, b, n,error):
    d = b
    x = initVect(n)
    t = initVect(n)
    r = diff(b,prodMat(A,d,n),n)
    while float(norme(r,n)*norme(r,n) ) > error :
        t = float(produitScal(r,d,n)/produitScal(produitMat(A,d, n),d, n) )
        x =sommeVect(x,produitVectScal(d,t,n), n)
        r = diff(r,produitVectScal(prodMat(A,d,n), t, n),n)
    #resultat
    result ="le resultat vaut: "
    for i in range(n):
        result += "\n x{} = {}".format(i+1, x[i])
    return result
    
#somme de 2 vecteurs
def sommeVect(a,b,n):
    s =initVect(n)
    for i in range(n):
        s[i] = a[i] + b[i]
    return s

#produit d'un vecteur et d'un scalaire
def prodVectScal(a,t,n):
    p =initVect(n)
    for i in range(n):
        p[i] = t*a[i]
    return p

#initialisation d'une matrice
def initMat(n):
    m = [ [0 for i in range(n)] for j in range(n)]
    return m

#initialisation d'un vecteur
def initVect(n):
    d = []
    i = 0
    while i<n:
        d.append(0)
        i+=1
    return d
    
#diffrence de 2 vecteurs
def diff(A,B,n):
    d = initVect(n)
    for i in range(n):
        d[i] = A[i]-B[i]
    
    return d

#produit scalaires de 2 vecteurs
def prodScal(a,b,n):
    p=0
    for i in range(n):
        p +=a[i]*b[i] 
    return p

#produit d'une matrice et d'un vecteur
def prodMat(A, b,n):
    p = initVect(n)
    for i in range(n):
        p[i] =0
        for j in range(n):
            p[i] += A[i][j]*b[i]
    
    return p
#norme d'un vecteur
def norme(A,n):
    norme=0
    for i in range(n):
        norme += A[i]*A[i]
    return sqrt(norme)
