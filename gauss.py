import math as m
import time
n=0

#############################################
#Fonctions pour la resolution par Gauss
def recherchepivot(k,A):
	i=k
	while i!=n and A[i][k]==0:
		i+=1
	if i!=n:
		return i
	else:
		return -1


def permutation(i0,i,A,b):
    A[i],A[i0] = A[i0],A[i]
    b[i],b[i0] = b[i0],b[i]
    return A,b

def elimination(k,A,b):
	i=k+1
	while i < n:
		r = A[i][k]/A[k][k]
		b[i] -= r*b[k]
		j=k
		while j < n:
			A[i][j]= round(A[i][j] - r*A[k][j],2)
			j+=1
		i+=1
	return A,b

def remonte(A,b):
	x = CreerListe(n)        
	x[n-1] = round(b[n-1]/A[n-1][n-1],3)
	for i in range(n-2,-1,-1):
		x[i] = b[i]
		for j in range(i+1,n):
			x[i] -= A[i][j]*x[j]
		x[i]/=A[i][i]
		x[i]=round(x[i],3)
	return x


def solveSystGauss(A,b):
	global n
	n=len(A)
	t1=time.time()
	k = 0
	arret = 0
	while k!=n and arret!=1:
		i0 = recherchepivot(k,A)
		if i0 == -1:
			arret = 1
		else:
			if i0 == k:
				A,b = elimination(k,A,b)
				k+=1
			else: 
				A,b = permutation(i0,k,A,b)
				A,b = elimination(k,A,b)
				k+=1
	if k==n and A[n-1][n-1]!=0:
		# equation solutions
		x = remonte(A,b)  
		t2=time.time()
		t=t2-t1
		return x,t*1000000
	else:
		# no unique solution
		#print("Ce systeme n'admet pas de solution unique")
		return 0

Matr=[[2,2],[2,2]]
vec=[1,1]

res=solveSystGauss(Matr,vec)
print(Matr)
print(vec)
#print(res)