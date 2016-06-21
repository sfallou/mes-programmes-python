#!/usr/bin/python

######################## CREATION DE FONCTIONS OPERANDES ######################
def creemat(n):
	#Cree une matrice vide de taille n
	L=[]
	for i in range(n):
		L.append([])
		for j in range(n):
			L[i].append(0)
	return L
	
def affichemat(A,n):
	#Affiche la matrice A rentree sous forme de liste
	for i in range(n):
		print(A[i])
		

def recopiemat(A):
	#Recopie la matrice A pour eviter des problemes de pointeurs
	B=creemat(len(A))
	for i in range(len(A)):
		for j in range(len(A)):
			B[i][j]=A[i][j]
					
			
	return B

def creevect(n):
	#Creation d un vecteur colonne de taille n
	V=[]
	for i in range(n):
		V.append([0])
	return V

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
	
	
##################### RESOLUTION D'UN SYSTEME ################################# 
def resolutionsysteme(A,y):
	#Resout l equation AX=Y par pivot de gauss
	#Triangularisation
	n=len(A)
	for i in range(n-1):
		index_pivot=pivotpartiel(A,i)
		echangeligne(A,i,index_pivot)
		echangeligne(y,i,index_pivot)
		for k in range(i+1,n):
			mu =float(A[k][i])/float(A[i][i])
			transvection(A,k,i,-mu)
			y[k]-=mu*y[i]
	x=creevect(n)
	for i in range(n-1,-1,-1):
		for k in range(i+1,n):
			y[i]-=A[i][k]*x[k]
		x[i]=float(y[i])/float(A[i][i])
	return x
######################## Saisie d'une Matrice#################################
def saisiemat(n):
	L = creemat(n)
	for i in range(n):
		for j in range(n):
			L[i][j] = int(input("donner un element : "))
	return L
	
############################# INVERSION #######################################
def inversion(A):
	#Calcul l inverse de la matrice A 
	A0=recopiemat(A)
	n=len(A0)
	I=identite(n)	
	for i in range(n-1):			#triangularisation de la matrice
		index_pivot=pivotpartiel(A0,i)
		echangeligne(A0,i,index_pivot)
		echangeligne(I,i,index_pivot)
		for k in range(i+1,n):
			mu = float(A0[k][i])/float(A0[i][i])
			transvection(A0,k,i,-mu)
			transvection(I,k,i,-mu)
	for i in range(n):			#coef diagonaux a 1
		mu=A0[i][i]
		for j in range(n):
			if(mu!=0):
				A0[i][j]=float(A0[i][j])/float(mu)
				I[i][j]=float(I[i][j])/float(mu)
	for i in range(1,n):			#annulation des autres coef
		for j in range(n-i):
			mu=A0[j][n-i]
			transvection(I,j,n-i,-mu)
	return I

