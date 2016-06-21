# -*- coding: utf-8 -*-
from Tkinter import *
def elimination(k,A,n):
    for i in range(k+1,n):
        r = A[i][k]/A[k][k]        
        for j in range(k,n):
            A[i][j] -= r*A[k][j]
    return A
    
def factoLu(A,b,n):
    arret = 0
    k =0 
    L =[ [0 for i in range(n)] for j in range(n)]
    while k!=n and arret!=1:
        L[k][k] = 1
        if A[k][k] != 0:
            for i in range(k+1,n):
                L[i][k] = A[i][k]/A[k][k]
            elimination(k,A,n)
            k = k+1
        else:
            arret = 1
    print L
    """arret == 1 and """
    if k ==n :
        result = "\nA est factorisable en LU\n"
        result += remonter(L,A,b,n)
        return result
    else:
        result = "les conditions ne sont pas reunis \n pour une factorisation LU"
        return result
    
#descente
def descente(L,b,n):
    y = []
    i = 0
    #initialisation de y
    while i<n:
        y.append(0)
        i +=1
        
    y[0] = b[0]
    for i in range(1,n):
        y[i] = b[i]
        for j in range(i-1):
            y[i] -= L[i][j]*y[j]
    return y

#remonter
def remonter(L,u,b,n):
    x = []
    #initialisation de x
    i = 0
    while i<n:
        x.append(0)
        i +=1
 
    y = descente(L,b,n)
    result = "Ce systeme a pour solution: "
    x[n-1] = y[n-1]/u[n-1][n-1]
    for i in range(n-2,0,-1):
        x[i] = y[i]
        for j in range(i+1,n):
            x[i] -= u[i][j]
        x[i] /= u[i][i] 
    for i in range(n):
        result += "\n x{} = {}".format(i+1, x[i]) 
    return result


#
def subtition_avant(L,b,n):
    z[1] = b[1]
    for i in range(1,n):
        z[i] = (b[i] - som(L,z,i))
    subtition_arriere(L,u,n,z)
