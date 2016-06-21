#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#### Multi Threading ####


from Tkinter import *
from math import *
from time import *
import socket, sys, threading
import pickle

global ordreMat
global matA
global matB
matA=list()
matB=list()

host = 'localhost'
port = 9090



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


def Gauss():
	global matA
	global matB
	A = matA
        b = matB
        n = len(matA)
	k = 0
	arret = 0
	while k!=n and arret!=1:
		i0 = recherchepivot(k,A,n)
		if i0 == -1:
			arret = 1
		else:
			if i0 == k:
				A,b = elimination(k,A,b,n)
				k+=1
			else: 
				A,b = permutation(i0,k,A,b)
				A,b = elimination(k,A,b,n)
				k+=1
	if k==n and A[n-1][n-1]!=0:	
		# equation solutions
		global resX		
		resX = remonte(A,b,n)  
		resultat = 'O' + ';' + pickle.dumps(resX)
		connexion.send(resultat)
	else:
		# no unique solution
		info ="""Ce systeme n'admet pas de solution unique"""
		erreur= 'N' +';'+info
		connexion.send(erreur)
		

def factLU(A,n):
	k=0
	arret=0
	L=CreeMatCar(n)
	while k!=n and arret!=1:
		L[k][k]=1
		if A[k][k] !=0:
			for i in range(k+1,n):
				L[i][k]=round(A[i][k]/A[k][k],2)
			A=eliminationLU(k,A,n)
			k+=1
		else:
			arret=1
	if arret==0 and A[n-1][n-1]!=0:	
		return L
	else:
		print("Les conditions ne sont pas reunies")
		return 0

def descente(L,b,n):
	y = CreerListe(n)        
	for i in range(n):
		y[i] = b[i] 
		for j in range(i):
			y[i] -= L[i][j]*y[j]
	return y

def Lu():
	global matA
	global matB
	A = matA
        b = matB
        n = len(matA)
	try:	
		L=factLU(A,n)
		global resXLu
		if L!=0:
			y=descente(L,b,n)			
			resXLu=remonte(A,y,n)
			resultat = 'O' + ';' + pickle.dumps(resXLu)
			connexion.send(resultat)
        		
	except:
		info="Ce systeme ne peut pas etre résolu par la méthode LU"
		erreur= 'N' + info		
		connexion.send(erreur)


def Choleski():
	global matA
	global matB
	A=matA
	b=matB
	n=len(matA)
	B=list()
	global resXCh
	try:
		B=factCholesky(A)
		y=descenteChol(B,b)
		resXCh=remonteChol(B,y)
        	resultat = 'O' + ';' + pickle.dumps(resXCh)
		connexion.send(resultat)
	except:
		info="Ce systeme ne peut pas etre résolu par la méthode Cholesky"		
		erreur='N' + info
		connexion.send(erreur)

def Inverse():
	global matA
	A=matA
	n=len(matA)	
	try:
		A0=recopiemat(A)
		global I
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
		resultat = 'O' + ';' + pickle.dumps(I)
		connexion.send(resultat)
	except:
		info="Cette matrice n'est pas inversible"		
		erreur= 'N' + info
		connexion.send(erreur)


class ThreadClient(threading.Thread):
 ###dérivation d'un objet thread pour gérer la connexion avec un client###
    	def __init__(self, conn):
		threading.Thread.__init__(self)
        	self.connexion = conn
        
    	def run(self):
# Dialogue avec le client :
        	nom = self.getName()        # Chaque thread possède un nom
		global ordreMat
		global matA
		global matB
        	while 1:
            		msg = self.connexion.recv(1024)
			if msg=='0':
		                break
			variables = msg.split(":")
			if variables[0] == 'gauss':
				matA=pickle.loads(variables[1])
				matB=pickle.loads(variables[2])
		       		Gauss()
		       	
			elif variables[0]== 'lu':
				matA=pickle.loads(variables[1])
				matB=pickle.loads(variables[2])
		       		Lu()
			elif variables[0]== 'choleski':
				matA=pickle.loads(variables[1])
				matB=pickle.loads(variables[2])
		       		Choleski()
			elif variables[0]== 'inverse' :
				matA=pickle.loads(variables[1])
		       		Inverse()
			#else:			
				#resultat = 'N'+';'+'Erreur entree :verifiez les donnees svp !'
				#connexion.send(resultat)
                    
# Fermeture de la connexion :
		self.connexion.close()      # couper la connexion côté serveur
        	del conn_client[nom]        # supprimer son entrée dans le dictionnaire
        	print "Client %s déconnecté." % nom
# Le thread se termine ici    

# Initialisation du serveur - Mise en place du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	mySocket.bind((host, port))
except socket.error:
	print "La liaison du socket à l'adresse choisie a échoué."
	sys.exit()
print "Serveur prêt, en attente de requêtes ...  "
print "écoute sur le port {}".format(port)
mySocket.listen(5)

# Attente et prise en charge des connexions demandées par les clients :
conn_client = {}                # dictionnaire des connexions clients
while 1:    
	connexion, adresse = mySocket.accept()
# Créer un nouvel objet thread pour gérer la connexion :
	th = ThreadClient(connexion)
	th.start()
# Mémoriser la connexion dans le dictionnaire : 
	it = th.getName()        # identifiant du thread
	conn_client[it] = connexion
	print "Client %s connecté, adresse IP %s, port %s." %\
           (it, adresse[0], adresse[1])




