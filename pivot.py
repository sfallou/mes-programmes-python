# -*- coding: utf-8 -*-

def recherchepivot(k,A,n):
    i = k
    while i != n and A[i][k] == 0:
        i+=1
    if i != n:
        return i
    else:
        return -1

def permutation(i0,i,A,b,n):
    A[i],A[i0] = A[i0],A[i]
    b[i],b[i0] = b[i0],b[i]
    return A,b

def elimination(k,A,b, n):
    i=k+1
    while i < n:
        r = A[i][k]/A[k][k]		
        b[i] -= r*b[k]
        j=k
        while j < n:
            A[i][j] -= r*A[k][j]
            j+=1
        i+=1	
    return A,b

def remonte(A,b, n):
    x = []
    i = 0
    while i<n:
        x.append(0)
        i+=1		
    x[n-1] = b[n-1]/A[n-1][n-1]
    i = n-2
    while i>=0:    
        x[i] = b[i]			
        j = i+1
        while j<n:
            x[i] -= A[i][j]*x[j]
            j+=1			
        x[i]/=A[i][i]
        i-=1
    return x

def Resolution(A, b, n):
	k = 0
	arret = 0
	while k!=n and arret!=1:
		i0 = recherchepivot(k,A,n)
		if i0 == -1:
			arret = 1
		else:
			if i0 == k:
				A,b = elimination(k,A,b, n)
				k+=1
			else:
				A,b = permutation(i0,k,A,b, n)
				A,b = elimination(k,A,b,n)
				k+=
		if k==n and A[n-1][n-1]!=0:
		# equation solutions
			x = remonte(A,b)
			result = "Ce système admet pour solution :"
			for i in range(n):
				result += "\n x{} = {}".format(i+1, x[i])*
		else:
		# no unique solution
			result = "Ce système n'admet pas de solution unique"
	
	print(result)
