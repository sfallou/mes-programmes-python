###################################################################
##################################################Premier Semestre
#!/usr/bin/python3
# -*-coding:Utf-8 -*

#fonction de creation d'une matrice de type (n,p)
# avec initialisation d'une valeur X
def creer_matrice(n, p, X) :
  A = n * [None]
  for i in range(n) :
    A[i ] = p * [X]
  return A

def CreerListe(n):
    return [0.0 for i in range(n)]

def identite1(identite,ligne,colonne) :
    i,j=0,0
    while i<ligne :
        matligne = list()
        while j <colonne :
            if i==j :
                matligne.append(1)
            else :
                matligne.append(0)
            j=j+1
        identite.append(matligne)
        i=i+1
        j=0
    return identite

def recherchePivot(matrice,k,ligne) :
    i=k
    while i < ligne:
        if matrice[i][k]!= 0 :
            return i
        i=i+1
    return -1


def permutation1(matrice,matId,k,pivot) :
    mat=list()
    mat.append(matrice[k])
    matrice[k] = matrice[pivot]
    matrice[pivot]= mat[0]
    mat=list()
    mat.append(matId[k])
    matId[k] = matId[pivot]
    matId[pivot] =  mat[0]
    return matrice,matId

def elimination1(matrice,identite,pivot,ligne,colonne ) :
    i=0
    while i < ligne :
       j=0
       if i!=pivot and matrice[i][pivot]!=0 :
           a=float(matrice[i][pivot])/float(matrice[pivot][pivot])
           while j < colonne:
                matrice[i][j]= matrice[i][j] - (matrice[pivot][j]*a)
                identite[i][j]= identite[i][j] - (identite[pivot][j]* a)
                j+=1
       i=i+1
    return matrice,identite

def remonte1(matrice,matId,ligne, colonne ) :
    pivot,i=0,0
    while pivot<ligne :
        b=matrice[pivot][pivot]
        while i<colonne:
            a=matrice[pivot][i]
            d=matId[pivot][i]
            matrice[pivot][i]= float(a) / float(b)
            matId[pivot][i]= float(d) / float(b)
            matId[pivot][i]=format(matId[pivot][i],'.2f')
            i+=1
        pivot+=1
        i=0
    return matrice,matId

def inverser(matrice,ligne,colonne):
    matriceIdentite = list()
    matriceIdentite =identite1(matriceIdentite,ligne,colonne)
    k=0
    arret = 1
    while k<ligne and arret == 1 :
        pivot=recherchePivot(matrice,k,ligne)
        if pivot==k :
            matrice,matriceIdentite =elimination1(matrice,matriceIdentite,pivot,ligne,colonne)
            k=k+1
        else :
            if pivot==-1 :
                arret = 0
            else :
                matrice,matriceIdentite = permutation1(matrice,matriceIdentite,k,pivot)
                pivot = k
                matrice,matriceIdentite =elimination1(matrice,matriceIdentite,pivot,ligne,colonne)
                k=k+1
    if arret==1 and matrice[ligne-1][colonne-1]!=0 :
            matrice,matriceIdentite = remonte1(matrice,matriceIdentite,ligne,colonne)
    else :
            matriceIdentite.append(-1) 
    return matriceIdentite

#Fonction qui permet de copier une matrice A
#dans une matrice B
def copie_matrice(A) :
  n = len(A)
  B = n * [None]
  for i in range(n) :
    B[i ] = A[i ]
  return B

#Fonction qui renvoit la dimension de la matrice
def dimensions(A) :
  n=len(A)
  p=len(A[0])
  return n,p
def permutation1(matrice,matId,k,pivot) :
    mat=list()
    mat.append(matrice[k])
    matrice[k] = matrice[pivot]
    matrice[pivot]= mat[0]
    mat=list()
    mat.append(matId[k])
    matId[k] = matId[pivot]
    matId[pivot] =  mat[0]
    return matrice,matId

def elimination1(matrice,identite,pivot,ligne,colonne ) :
    i=0
    while i < ligne :
       j=0
       if i!=pivot and matrice[i][pivot]!=0 :
           a=float(matrice[i][pivot])/float(matrice[pivot][pivot])
           while j < colonne:
                matrice[i][j]= matrice[i][j] - (matrice[pivot][j]*a)
                identite[i][j]= identite[i][j] - (identite[pivot][j]* a)
                j+=1
       i=i+1
    return matrice,identite

def remonte1(matrice,matId,ligne, colonne ) :
    pivot,i=0,0
    while pivot<ligne :
        b=matrice[pivot][pivot]
        while i<colonne:
            a=matrice[pivot][i]
            d=matId[pivot][i]
            matrice[pivot][i]= float(a) / float(b)
            matId[pivot][i]= float(d) / float(b)
            matId[pivot][i]=format(matId[pivot][i],'.2f')
            i+=1
        pivot+=1
        i=0
    return matrice,matId


"""Fonction qui cree une matrice carre et linitialise a la matrice nulle"""
def CreeMatCar(n):
	return [ [0.0 for j in range(0,n)] for i in range(0,n) ]

"""Fonction qui cree une matrice identite"""
def CreeMatId(n):
	I=CreeMatCar(n)
	for i in range(0,n):
		I[i][i]=1.0
	return I

"""Fonction qui remplit une matrice"""
def FillMat(M):
	print("Donnez les elements de votre matrice")
	i=0
	while i<len(M):
		print("Elements de la ",i+1," eme ligne")	
		j=0
		while j< len(M):
			M[i][j]=float(input("element "+str(j+1)+": "))
			j+=1
		i+=1
		

"""Fonction qui copie une matrice ds une autre matrice"""
def CopyMatr(A):
	n=len(A)
	B=CreeMatCar(n)
	for i in range(0,n):
		for j in range(0,n):
			B[i][j]=A[i][j]
	return B



"""Fonction qui calcule le produit de deux matrices"""
def ProdMat(A,B):
	n=len(A)
	AB=CreeMatCar(n)           #initialisation de AB que la fonction va renvoyer
	for i in range(0,n):              #Parcours des lignes
		for j in range(0,n):    #Parcours des colonnes
			AB[i][j]=0   #Initialisation de AB[i][j]
			for k in range(0,n):      #Variable k qui va nous permettre de fai#Variable k qui va nous permettre de faire la somme des lignes et des colonnesre la somme des lignes et des colonnes
				AB[i][j]+=(A[i][k])*(B[k][j])
	return AB	

"""Fonction qui permute deux colonnes d une matrice"""
def PermCol(M,j,i):
	for k in range(len(M)-1,-1,-1):
		(M[k][j],M[k][i])=(M[k][i],M[k][j])

"""Fonction qui calcule la difference A- aI"""
def DiffMatI(A,a):
	n=len(A)
	B=CreeMatCar(n)
	for i in range(0,n):
		for j in range(0,n):
			if i!=j:
				B[i][j]=A[i][j]
			else:
				B[i][j]=A[i][j]-float(a)
	return B

"""Fonction qui calcule la somme des diagonales"""
def Trace(A):
	n=len(A)
	t=0
	for j in range(0,n):
		t+= A[j][j]
	return t
			
"""Fonction qui calcule le produit des diagonales"""
def ProdDiag(M):
	j=0
	p=1
	while j<len(M):			
		p=p*M[j][j]
		j+=1	
	return p

"""Fonction qui triangule une matrice carre--triangulaire superieure--"""
def Triangule(M):
	sign=1
	n=len(M) -1
	for i in range(n,0,-1):#A partir de  la derniere jusqua la 2eme ligne 
		for j in range(0,i):#Mij=0 si j<i
			if M[i][j+1] !=0.0:#Si c'est nulle, jai qu'a faire une permutation pour avoir 0
				q=(M[i][j])/(M[i][j+1]) 
				if q!=0.0:#Si c'est nulle, pas besoin de le rendre nulle
					for k in range(n,-1,-1):#A chaque combinaison, c'est les elements de toute la colonne qui doivent changer
						M[k][j]= M[k][j] - q*M[k][j+1]
			else:
				PermCol(M,j+1,j)
				sign=sign*(-1)#le determinant est multipli par -1 si on permute deux colonnes de la matrice
	return M,sign

"""Fonction qui calcule le determinant une matrice carre"""
def Determinant(M):
	(Mtriang,sign)=Triangule(M)
	return round(sign*ProdDiag(Mtriang),2)


"""Fonction qui calcule les coefficients du polynome caracteristique"""				
def PolyCarac(A):
	n=len(A)
	l=list()
	if n%2==0:
		l.append(1)
	else:
		l.append(-1)
	Bi=CreeMatId(n)
	for i in range(1,n+1):
		Ai=ProdMat(A,Bi)
		a=round((1/i)*Trace(Ai),2)
		if i != n:
			l.append(a)
		Bi=DiffMatI(Ai,a)
		
	return l

"""Fonction qui met dans une chaine le polynome caracteristique"""
def ChaiPoly(l,n):
	car="?^"
	chai=" "
	i=n
	for el in l:
		if el<0:
			if i==n:
				chai= chai + " "+str(el) +car +str(i)			
			if i>1 and i<n:	
				chai= chai+ " " +str(el) +car +str(i)
			if i==1:
				chai= chai +" " + str(el) + "?  "
			if i==0:
				chai=chai +" " + str(el)
		if el>0:
			if i==n:
				chai= chai + str(el) +car +str(i)			
			if i>1 and i<n:		
				chai= chai+ "+  " + str(el) +car +str(i) 
			if i==1:
				chai= chai + "+  "+ str(el) + "? "
			if i==0:
				chai=chai + "+  " +str(el)
		i-=1
	return chai

def ChaiPolyWakh(l,n):
	car="t a la puissance"
	chai=" "
	i=n
	for el in l:
		if el<0:
			if i==n:
				chai= chai + "moins "+str(el) +car +str(i)			
			if i>1 and i<n:	
				chai= chai+ "moins " +str(el) +car +str(i)
			if i==1:
				chai= chai +" moins" + str(el) + "t  "
			if i==0:
				chai=chai +"moins " + str(el)
		if el>0:
			if i==n:
				chai= chai + str(el) +car +str(i)			
			if i>1 and i<n:		
				chai= chai+ "+  " + str(el) +car +str(i) 
			if i==1:
				chai= chai + "+  "+ str(el) + "t "
			if i==0:
				chai=chai + "+  " +str(el)
		i-=1
	return chai		

###################################################################
###################################################deuxieme Semestre
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
	t1=time.clock()
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
		t2=time.clock()
		t=t2-t1
	else:
		# no unique solution
		x="Ce systeme n'admet pas de solution unique"
        t=0
	return x,t


##########################################################
#Fonctions pour la resolution par LU
def eliminationLU(k,A):
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

def descente(L,b):
	y = CreerListe(n)        
	for i in range(n):
		y[i] = b[i] 
		for j in range(i):
			y[i] -= L[i][j]*y[j]
	return y


#mm remonte que Gauss
"""def remonte(A,b):
	n=len(A)
	x = CreerListe(n)       
	x[n-1] = b[n-1]/A[n-1][n-1]
	for i in range(n-2,-1,-1):
		x[i] = b[i]
		for j in range(i+1,n):
			x[i] -= A[i][j]*x[j]
		x[i]/=A[i][i]
	return x"""


def factLU(A):
	global n
	n=len(A)
	k=0
	arret=0
	L=CreeMatCar(n)
	while k!=n and arret!=1:
		L[k][k]=1
		if A[k][k] !=0:
			for i in range(k+1,n):
				L[i][k]=round(A[i][k]/A[k][k],2)
			A=eliminationLU(k,A)
			k+=1
		else:
			arret=1
	if arret==0 and A[n-1][n-1]!=0:
		return L
	else:
		print("Les conditions ne sont pas reunies")
		return 0

def solveSystLU(A,b):
	t1=time.clock()
	L=factLU(A)
	if L!=0:
		y=descente(L,b)
		x=remonte(A,y)
		t2=time.clock()
		t=t2-t1
		#print("La solution de votre systeme est \n",x)
		return x,L,t
	else:
		#print("Ce systeme ne peut pas etre resolu par la methode LU")
		return 0



####################################################################
#Fonctions Pour la resolution par Cholesky
def factCholesky(A):
	n=len(A)
	B=CreeMatCar(n)
	for j in range(n):
		B[j][j]=A[j][j]
		for k in range(j):
			B[j][j] -=B[j][k]*B[j][k]
		B[j][j]= round(m.sqrt(B[j][j]),2)
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

def solveSystCholesky(A,b):
	t1=time.time()
	B=factCholesky(A)
	y=descenteChol(B,b)
	x=remonteChol(B,y)
	t2=time.time()
	t=t2-t1
	print(x)
	return x,B,t
	
#######################################################

def multiply(m1, m2):
    m = [] 
    if len(m1[0]) != len(m2): 
        return False 
    for i in range(len(m1)): 
        ligne = [] 
        for j in range(len(m2[0])): 
            for k in range(len(m1[0])): 
                element = m1[i][j] * m2[i][j] 
                element = element + m1[i][k] * m2[k][i] 
        ligne.append(element) 
    m.append(ligne) 
    return m