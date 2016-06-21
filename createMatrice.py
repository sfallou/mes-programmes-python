# -*- coding: utf-8 -*-

#fonction de creation d'une matrice de type (n,p)
# avec initialisation d'une valeur X
def creer_matrice(n, p, X) :
	A = n * [None]
	for i in range(n) :
		A[i ] = p * [X]
	return A

Mat=list()
Mat=creer_matrice(2,3,12)
print("La matrice A est:")
print(Mat)

#Fonction qui permet de copier une matrice A
#dans une matrice B
def copie_matrice(A) :
	n = len(A)
	B = n * [None]
	for i in range(n) :
		B[i ] = A[i ]
	return B

Mat2=list()
Mat2=copie_matrice(Mat)
print("la matrice B est:")
print(Mat2)

#Fonction qui renvoit la dimension de la matrice
def dimensions(A) :
	n=len(A)
	p=len(A[0])
	return n,p

k,l=dimensions(Mat2)
print(k)
print(l)

#Fonction qui renvoit la transposée d'une matrice
def transpose(A) :
	n, p = dimensions(A)
	B = creer_matrice(p, n, None)
	for j in range(p) :
		for i in range(n) :
			B[j ] [ i ] = A[i ] [ j ]
	return B

print(transpose(Mat2))

#Fonction qui calcule l'inverse d'une matrice