#from Accueil import *
#from LU import *

def som(b,x,i,n):
   s = 0
   for k in range(i+1,n):
       s += b[i][k]*x[k]

def affich_r(x,n):
    for i in range(n):
        print "x["+i+1+"] = "+x[i]
        print

def gauss(b,n):
    m = MatriceNulle(n)
    for i in range(n-1):
        for j in range(n-1):
            m[j][i] = b[j][i]/b[i][i]
            for k in range(n+1):
                b[j][k] = b[j][k] - m[i][j]*b[i][k]
    x= [0 for i in range(n)]
    x[n] = b[n][n+1]/b[n][n]
    for i in range(n-1,0,-1):
        x[i] = (b[i][n+1] - som(b,x,i,n))/b[i][i]
    
    affich_r(x,n)


