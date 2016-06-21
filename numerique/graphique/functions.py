
def CreeMatCar(n):
	return [ [0.0 for j in range(n)] for i in range(n) ]

def CreerListe(n):
	return [0.0 for i in range(n)]

def recherchepivot(k,A,n):
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

def elimination(k,A,b,n):
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

def remonte(A,b,n):
	x = CreerListe(n)        
	x[n-1] = float(b[n-1])/float(A[n-1][n-1])
	for i in range(n-2,-1,-1):
		x[i] = b[i]
		for j in range(i+1,n):
			x[i] -= A[i][j]*x[j]
		x[i]/=A[i][i]
		x[i]=float(x[i])
	return x

def factCholesky(A):
	n=len(A)
	B=CreeMatCar(n)
	for j in range(n):
		B[j][j]=A[j][j]
		for k in range(j):
			B[j][j] -=B[j][k]*B[j][k]
		B[j][j]= round(sqrt(B[j][j]),2)
		for i in range(j+1,n):
			B[i][j]=A[i][j]
			for k in range(j):
				B[i][j]-=B[i][k]*B[j][k]
			B[i][j]=round(B[i][j]/B[j][j],2)
	return B

def descenteChol(L,b):
	n=len(L)
	y = CreerListe(n)        
	for i in range(n):
		y[i] = b[i] 
		for j in range(i):
			y[i] -= L[i][j]*y[j]
		y[i]/=L[i][i]
	return y


def remonteChol(B,b):
	n=len(B)
	x = CreerListe(n)       
	x[n-1] = round(b[n-1]/B[n-1][n-1],3)
	for i in range(n-2,-1,-1):
		x[i] = b[i]
		for j in range(i+1,n):
			x[i] -= B[j][i]*x[j]
		x[i]/=B[i][i]
		x[i]=round(x[i],3)
	return x



def creemat(n):
	#Cree une matrice vide de taille n
	L=[]
	for i in range(n):
		L.append([])
		for j in range(n):
			L[i].append(0)
	return L

def recopiemat(A):
	#Recopie la matrice A pour eviter des problemes de pointeurs
	B=creemat(len(A))
	for i in range(len(A)):
		for j in range(len(A)):
			B[i][j]=A[i][j]
					
			
	return B

def echangeligne(A,i,j):
	#Operation elementaire, echange des lignes i et j de la matrice A 
	#modifiee par pointeur, la fonction ne retourne donc rien
	"""
	Attention, indexage a partir de 0 (ligne 1 = ligne 0)
	"""
	I=A[i]
	J=A[j]
	A[i]=J
	A[j]=I

def transvection(A,i,j,mu):
	#Operation elementaire, transvection des lignes i et j de la matrice
	#A avec un coeficient multiplicateur de mu
	for k in range(len(A)):
		A[i][k]+=mu*A[j][k]

def pivotpartiel(A,j0):
	#Recherche de pivots partiels en commencant au rang j0 de la matrice A
	#La fonction renvoi l index du pivot suivant 
	pivot=A[j0][j0]
	index=j0
	for k in range(j0+1,len(A)):
		if pivot<=abs(A[k][j0]):
			pivot=abs(A[k][j0])
			index=k
	return index

def identite(n):
	#Cree une matrice identite de taille n
	A=creemat(n)
	for i in range(n):
		A[i][i]=1
	return A

def eliminationLU(k,A,n):
	i=k+1
	while i < n:
		r = A[i][k]/A[k][k]
		j=k
		while j < n:
			A[i][j] -= r*A[k][j]
			A[i][j]=round(A[i][j],2)
			j+=1
		i+=1
	return A