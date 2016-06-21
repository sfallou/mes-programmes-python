# -*- coding: utf-8 -*-
from Tkinter import *
from math import *
from time import *
import tkMessageBox

global ordreMat
global matA
global matB
global y
matA=list()
matB=list()

def Apropos():
	Aproposfen = Tk()
	Aproposfen.configure(bg="white")
        s="Cette application a été réalisée dans le cadre \n du module de Calcul numérique. Ce module \n a été dispensé par le Docteur Samuel OUYA\n à l'école Supérieure Polytechnique de Dakar (Sénégal)."
        Labelapro = Label(Aproposfen, text=s,bg="white", font=("Arial", 12, "bold"))
        Boutonqt = Button(Aproposfen, text="Quitter", font=("Arial", 12, "bold"), fg='white', bg='red', command=Aproposfen.destroy)
        Labelapro.grid(row=0, column=0, padx=5, pady=5)
        Boutonqt.grid(row=2, column=0, padx=5, pady=5)
        Aproposfen.mainloop()

def erreur(info):
	faffiche=Frame(fsortie, borderwidth=1, bg="azure")
	faffiche.place(relx=0,rely=0.4,relwidth=1, relheight=0.6)
	faffichetext=Frame(faffiche, borderwidth=1, bg="azure")
	faffichetext.place(relx=0,rely=0,relwidth=1, relheight=0.2)
	Label(faffichetext,text=info,foreground="red", font="arial 14 bold", bg="azure").pack(anchor=CENTER)
	# boutons recommencer, quitter et apropos
	fafficheBut=Frame(faffiche, borderwidth=1, bg="azure")
	fafficheBut.place(relx=0,rely=0.8,relwidth=1, relheight=0.2)
	Button(fafficheBut,text="Recommencer",bg="white",fg="green",activebackground='yellow',font="arial 12 bold",width="15", command=recommencer).place(relx=0.45,rely=0.0)
	Button(fafficheBut,text="Apropos",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command =Apropos).place(relx=0.72,rely=0.0)	
	Button(fafficheBut,text="Quitter",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command =quitter).place(relx=0.85,rely=0.0)

def afficheGauss():
	global resX
	ordre=int(ordreMat.get())
	faffiche=Frame(fsortie, borderwidth=1, bg="azure")
	faffiche.place(relx=0,rely=0.4,relwidth=1, relheight=0.6)
	faffichetext=Frame(faffiche, borderwidth=1, bg="azure")
	faffichetext.place(relx=0,rely=0,relwidth=1, relheight=0.2)
	fafficheMat=Frame(faffiche, borderwidth=1, bg="azure")
	fafficheMat.place(relx=0,rely=0.2,relwidth=1, relheight=0.6)
	fafficheMatcontenu=Frame(fafficheMat, borderwidth=1, background="azure")
	fafficheMatcontenu.pack(fill=Y,pady=10)
	Label(faffichetext,text="La solution obtenue par la méthode Gauss est:",foreground="blue", font="arial 14 bold", bg="azure").pack(anchor=CENTER)	
	for i in range(ordre):	
		Label(fafficheMatcontenu,text=round(resX[i],2),foreground="red", font="arial 12 bold",pady=0, background="azure",justify=CENTER).grid(padx=5, pady=5, row=i,column=1)
	#Creation des canvas de parentheses
        parA1 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        parA1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="[", font=("Arial", 24*ordre))
        parA2 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        parA2.create_text(5*ordre, 13*ordre, anchor=CENTER, text="]", font=("Arial", 24*ordre))
	parA1.grid(row=0, column=0, rowspan=ordre)
        parA2.grid(row=0, column=2, rowspan=ordre)
	# boutons recommencer, quitter et apropos 
	fafficheBut=Frame(faffiche, borderwidth=1, bg="azure")
	fafficheBut.place(relx=0,rely=0.8,relwidth=1, relheight=0.2)
	Button(fafficheBut,text="Recommencer",bg="white",fg="green",activebackground='yellow',font="arial 12 bold",width="15", command=recommencer).place(relx=0.45,rely=0.0)	
	Button(fafficheBut,text="Apropos",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command =Apropos).place(relx=0.72,rely=0.0)	
	Button(fafficheBut,text="Quitter",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command =fenetre.destroy).place(relx=0.85,rely=0.0)

def afficheLu():
	global resXLu
	ordre=int(ordreMat.get())
	faffiche=Frame(fsortie, borderwidth=1, bg="azure")
	faffiche.place(relx=0,rely=0.4,relwidth=1, relheight=0.6)
	faffichetext=Frame(faffiche, borderwidth=1, bg="azure")
	faffichetext.place(relx=0,rely=0,relwidth=1, relheight=0.2)
	fafficheMat=Frame(faffiche, borderwidth=1, bg="azure")
	fafficheMat.place(relx=0,rely=0.2,relwidth=1, relheight=0.8)
	fafficheMatcontenu=Frame(fafficheMat, borderwidth=1, background="azure")
	fafficheMatcontenu.pack(fill=Y,pady=10)
	Label(faffichetext,text="La solution obtenue par la factorisation LU est:",foreground="blue", font="arial 14 bold", bg="azure").pack(anchor=CENTER)	
	for i in range(ordre):	
		Label(fafficheMatcontenu,text=round(resXLu[i],2),foreground="red", font="arial 12 bold",pady=0, background="azure",justify=CENTER).grid(padx=5, pady=5, row=i,column=1)
	#Creation des canvas de parentheses
        parA1 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        parA1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="[", font=("Arial", 24*ordre))
        parA2 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        parA2.create_text(5*ordre, 13*ordre, anchor=CENTER, text="]", font=("Arial", 24*ordre))
	parA1.grid(row=0, column=0, rowspan=ordre)
        parA2.grid(row=0, column=2, rowspan=ordre)
	# boutons recommencer, quitter et apropos 
	fafficheBut=Frame(faffiche, borderwidth=1, bg="azure")
	fafficheBut.place(relx=0,rely=0.8,relwidth=1, relheight=0.2)
	Button(fafficheBut,text="Recommencer",bg="white",fg="green",activebackground='yellow',font="arial 12 bold",width="15", command=recommencer).place(relx=0.45,rely=0.0)	
	Button(fafficheBut,text="Apropos",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command =Apropos).place(relx=0.72,rely=0.0)	
	Button(fafficheBut,text="Quitter",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command =fenetre.destroy).place(relx=0.85,rely=0.0)

def afficheCholeski():
	global resXCh
	ordre=int(ordreMat.get())	
	faffiche=Frame(fsortie, borderwidth=1, bg="azure")
	faffiche.place(relx=0,rely=0.4,relwidth=1, relheight=0.6)
	faffichetext=Frame(faffiche, borderwidth=1, bg="azure")
	faffichetext.place(relx=0,rely=0,relwidth=1, relheight=0.2)
	fafficheMat=Frame(faffiche, borderwidth=1, bg="azure")
	fafficheMat.place(relx=0,rely=0.2,relwidth=1, relheight=0.8)
	fafficheMatcontenu=Frame(fafficheMat, borderwidth=1, background="azure")
	fafficheMatcontenu.pack(fill=Y,pady=10)
	Label(faffichetext,text="La solution obtenue par la factorisation Cholesky est:",foreground="blue", font="arial 14 bold", bg="azure").pack(anchor=CENTER)	
	for i in range(ordre):	
		Label(fafficheMatcontenu,text=round(resXCh[i],2),foreground="red", font="arial 12 bold",pady=0, background="azure",justify=CENTER).grid(padx=5, pady=5, row=i,column=1)
	#Creation des canvas de parentheses
        parA1 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        parA1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="[", font=("Arial", 24*ordre))
        parA2 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        parA2.create_text(5*ordre, 13*ordre, anchor=CENTER, text="]", font=("Arial", 24*ordre))
	parA1.grid(row=0, column=0, rowspan=ordre)
        parA2.grid(row=0, column=2, rowspan=ordre)
	# boutons recommencer, quitter et apropos 
	fafficheBut=Frame(faffiche, borderwidth=1, bg="azure")
	fafficheBut.place(relx=0,rely=0.8,relwidth=1, relheight=0.2)
	Button(fafficheBut,text="Recommencer",bg="white",fg="green",activebackground='yellow',font="arial 12 bold",width="15", command=recommencer).place(relx=0.45,rely=0.0)	
	Button(fafficheBut,text="Apropos",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command =Apropos).place(relx=0.72,rely=0.0)	
	Button(fafficheBut,text="Quitter",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command =fenetre.destroy).place(relx=0.85,rely=0.0)


def afficheInverse():
	global I
	ordre=int(ordreMat.get())
	faffiche=Frame(fsortie, borderwidth=1, bg="azure")
	faffiche.place(relx=0,rely=0.4,relwidth=1, relheight=0.6)
	faffichetext=Frame(faffiche, borderwidth=1, bg="azure")
	faffichetext.place(relx=0,rely=0,relwidth=1, relheight=0.2)
	fafficheMat=Frame(faffiche, borderwidth=1, bg="azure")
	fafficheMat.place(relx=0,rely=0.2,relwidth=1, relheight=0.8)
	fafficheMatcontenu=Frame(fafficheMat, borderwidth=1, background="azure")
	fafficheMatcontenu.pack(fill=Y,pady=10)
	Label(faffichetext,text="L'inverse de la matrice est :",foreground="blue", font="arial 14 bold", bg="azure").pack(anchor=CENTER)	
	for i in range(ordre):
		for j in range(ordre):		
			Label(fafficheMatcontenu,text=round(I[i][j],2),foreground="red", font="arial 12 bold",pady=0, background="azure",justify=CENTER).grid(padx=5, pady=5, row=i,column=j+1)
	#Creation des canvas de parentheses
        parA1 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        parA1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="[", font=("Arial", 24*ordre))
        parA2 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        parA2.create_text(5*ordre, 13*ordre, anchor=CENTER, text="]", font=("Arial", 24*ordre))
	parA1.grid(row=0, column=0, rowspan=ordre)
        parA2.grid(row=0, column=ordre+1, rowspan=ordre)
	# boutons recommencer, quitter et apropos 
	fafficheBut=Frame(faffiche, borderwidth=1, bg="azure")
	fafficheBut.place(relx=0,rely=0.8,relwidth=1, relheight=0.2)
	Button(fafficheBut,text="Recommencer",bg="white",fg="green",activebackground='yellow',font="arial 12 bold",width="15", command=recommencer).place(relx=0.45,rely=0.0)	
	Button(fafficheBut,text="Apropos",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command =Apropos).place(relx=0.72,rely=0.0)	
	Button(fafficheBut,text="Quitter",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command =fenetre.destroy).place(relx=0.85,rely=0.0)

def recommencer():
	global fsortie
	fsortie.destroy()
	del(matA[:]) # permet de vider la liste matA
	del(matB[:])
	global ordreMat	
	ordreMat=0
	fsortie=Frame(fcontenu, borderwidth=1, background="azure")
	Frame(fcontenu, borderwidth=1,background="indian red").place(relx=0,rely=0,relwidth=0.02,relheight=1)
	Frame(fcontenu, borderwidth=1, background="indian red").place(relx=0.98,rely=0,relwidth=0.02, relheight=1)
	fentree.place(relx=0.02,rely=0,relwidth=0.4, relheight=1)
	fsortie.place(relx=0.44,rely=0,relwidth=0.56, relheight=1)
	Label(fentree,text="Entrez la taille de la matrice:", foreground="blue", font="arial 14 bold", bg="azure").grid(row=0 ,column=0,ipadx=40)
	ordreMat=Entry(fentree,font="arial 16 ", width=5)
	ordreMat.grid(padx=20, pady=20, row=0 ,column=1)
	bu1=Button(fentree,text="valider",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command = menu)
	bu1.place(relx=0.4,rely=0.2)


def recuperer1():
	ordre=int(ordreMat.get())
	try:
		for i in range(ordre):
			for j in range(ordre):
				matA[i][j]=int(matA[i][j].get())
	except:
		tkMessageBox.showinfo('Erreur Matrice',"veuillez entrer des valeurs entieres")
def recuperer2():
	ordre=int(ordreMat.get())
	try:
		for i in range(ordre):
			matB[i]=int(matB[i].get())
			for j in range(ordre):
				matA[i][j]=int(matA[i][j].get())
	except:
		tkMessageBox.showinfo('Erreur Matrice',"veuillez entrer des valeurs entieres")

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

def beforeGauss():
	saisieMatrice2(1)
	
def beforeLu():
	saisieMatrice2(2)

def beforeCholeski():
	saisieMatrice2(3)

def beforeInverse():
	saisieMatrice1()


def Gauss():
	global matA
	global matB
	recuperer2()
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
		afficheGauss()
	else:
		# no unique solution
		info ="""Ce systeme n'admet pas de solution unique"""
		erreur(info)
		return 0

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
	recuperer2()
	A = matA
        b = matB
        n = len(matA)
	try:	
		L=factLU(A,n)
		global resXLu
		if L!=0:
			y=descente(L,b,n)			
			resXLu=remonte(A,y,n)
        		afficheLu()
	except:
		info="Ce systeme ne peut pas etre résolu par la méthode LU"		
		erreur(info)


def Choleski():
	global matA
	global matB
	recuperer2()
	A=matA
	b=matB
	n=len(matA)
	B=list()
	global resXCh
	try:
		B=factCholesky(A)
		y=descenteChol(B,b)
		resXCh=remonteChol(B,y)
        	afficheCholeski()
	except:
		info="Ce systeme ne peut pas etre résolu par la méthode Cholesky"		
		erreur(info)

def Inverse():
	global matA
	recuperer1()
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
		afficheInverse()
	except:
		info="Cette matrice n'est pas inversible"		
		erreur(info)


def menu():	
	global fsaisie
	fsaisie=Frame(fentree, borderwidth=1, bg="azure")
	fsaisie.place(relx=0,rely=0.3,relwidth=1, relheight=0.7)
	Button(fsaisie,text='GAUSS',bg="cyan",activebackground="yellow",fg="red",font="arial 12 bold",pady=20,command=beforeGauss).place(relx=0.05,rely=0.1,relwidth=0.43)
	Button(fsaisie,text='LU',bg="cyan",activebackground="yellow",fg="red",font="arial 12 bold",pady=20,command=beforeLu).place(relx=0.52,rely=0.1,relwidth=0.43)
	Button(fsaisie,text='CHOLESKI',bg="cyan",activebackground="yellow",fg="red",font="arial 12 bold",pady=20,command=beforeCholeski).place(relx=0.05,rely=0.5,relwidth=0.43)
	Button(fsaisie,text='INVERSE',bg="cyan",activebackground="yellow",fg="red",font="arial 12 bold",pady=20,command=beforeInverse).place(relx=0.52,rely=0.5,relwidth=0.43)


def saisieMatrice1():	
	fsortie1=Frame(fsortie, borderwidth=1, background="azure")
	fsortie1.place(relx=0.0,rely=0,relwidth=1, relheight=0.4)
	fsortie1contenu=Frame(fsortie1, borderwidth=1, background="azure")
	fsortie1contenu.pack(fill=Y,pady=10)	

	ordre=int(ordreMat.get())
	if ordre<=0:		
		tkMessageBox.showinfo('Erreur de taille',"La taille de la matrice doit est etre positive")
	else:
		for i in range(ordre):
			matcol=list()
			for j in range(ordre):
		    		p=Entry(fsortie1contenu,width=5,relief='raised',justify=CENTER)
		    		p.insert(0,'(%s;%s)' % (i,j))
		    		p.grid(row=i,column=j+1,padx=5, pady=5)
		    		matcol.append(p)
			matA.append(matcol)
		#Creation des canvas de parentheses
        	parA1 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        	parA1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="[", font=("Arial", 24*ordre))
        	parA2 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        	parA2.create_text(5*ordre, 13*ordre, anchor=CENTER, text="]", font=("Arial", 24*ordre))
		parA1.grid(row=0, column=0, rowspan=ordre)
        	parA2.grid(row=0, column=ordre+1, rowspan=ordre)
		
		Button(fsortie1,text="calculer",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command=Inverse).place(relx=0.4,rely=0.8)
		

def saisieMatrice2(z):	
	fsortie1=Frame(fsortie, borderwidth=1, background="azure")
	fsortie1.place(relx=0.0,rely=0,relwidth=1, relheight=0.4)
	fsortie1contenu=Frame(fsortie1, borderwidth=1, background="azure")
	fsortie1contenu.pack(fill=Y,pady=10)
	
	ordre=int(ordreMat.get())
	if ordre<=0:
		tkMessageBox.showinfo('Erreur de taille',"La taille de la matrice doit est etre positive")
	else:
		for i in range(ordre):
			matcol=list()
			for j in range(ordre):
		    		p=Entry(fsortie1contenu,width=5,relief='raised',justify=CENTER)
		    		p.insert(0,'(%s;%s)' % (i,j))
		    		p.grid(row=i,column=j+1,padx=5, pady=5)
		    		matcol.append(p)
			matA.append(matcol)
		for i in range(ordre):
		    	p=Entry(fsortie1contenu,width=5,relief='raised',justify=CENTER)
		    	p.insert(0,'(%s)' % (i))
		    	p.grid(row=i,column=ordre+7, padx=5, pady=5)
		    	matB.append(p)
		
		#Crearion des labels X
		xlabel = list()
        	texteX = list()
		for i in range(ordre):
            		xlabel.append([])
            		texteX.append([])
        	for i in range(ordre):
            		texteX[i] = StringVar()
            		texteX[i].set("x"+str(i+1))
            		xlabel[i] = Label(fsortie1contenu, textvariable=texteX[i], bg='azure',highlightbackground='azure',font=("Arial", 14, "bold"))
			xlabel[i].grid(row=i, column=ordre+3)
		#Creation des canvas de parentheses
        	parA1 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        	parA1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="[", font=("Arial", 24*ordre))
        	parA2 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        	parA2.create_text(5*ordre, 13*ordre, anchor=CENTER, text="]", font=("Arial", 24*ordre))
 
        	parX1 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        	parX1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="[", font=("Arial", 24*ordre))
        	parX2 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        	parX2.create_text(5*ordre, 13*ordre, anchor=CENTER, text="]", font=("Arial", 24*ordre))
        
        	parB1 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        	parB1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="[", font=("Arial", 24*ordre))
        	parB2 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='azure',highlightbackground='azure')
        	parB2.create_text(5*ordre, 13*ordre, anchor=CENTER, text="]", font=("Arial", 24*ordre))

        	#canvas Egalité
        	egalite = Canvas(fsortie1contenu, width=20, height=30*ordre, bg='azure',highlightbackground='azure')
        	egalite.create_text(21, 15*ordre, anchor=CENTER, text="=", font=("Arial", 20*ordre))	

		parA1.grid(row=0, column=0, rowspan=ordre)
        	parA2.grid(row=0, column=ordre+1, rowspan=ordre)
		parX1.grid(row=0, column=ordre+2, rowspan=ordre)
        	parX2.grid(row=0, column=ordre+4, rowspan=ordre)
        	egalite.grid(row=0, column=ordre+5, rowspan=ordre)
        	parB1.grid(row=0, column=ordre+6, rowspan=ordre)
        	parB2.grid(row=0, column=ordre+8, rowspan=ordre)	
		

		choix=int(z)
		if (choix==1):
			Button(fsortie1,text="calculer",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command= Gauss).place(relx=0.4,rely=0.8)
		elif (choix==2):
			Button(fsortie1,text="calculer",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command= Lu).place(relx=0.4,rely=0.8)
		elif (choix==3):
			Button(fsortie1,text="calculer",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command= Choleski).place(relx=0.4,rely=0.8)
		
            
fenetre = Tk()
fenetre.title("Calcul Numerique")
fenetre.geometry("1200x600")
fenetre.configure(background = "azure")

### Ajout de la bannière ###
can1 = Canvas(fenetre, width =1200, height=150, bg='white')
photo = PhotoImage(file ='logo.gif')
item = can1.create_image(600,75, image = photo)
can1.pack()

### interface graphique ###
fcontenu=Frame(fenetre, borderwidth=1)
fcontenu.pack(expand="yes",fill="both")
fcontenu.configure(background="cyan")
fentree=Frame(fcontenu, borderwidth=1, background="azure") 
fsortie=Frame(fcontenu, borderwidth=1, background="azure")
Frame(fcontenu, borderwidth=1,background="indian red").place(relx=0,rely=0,relwidth=0.02,relheight=1)
Frame(fcontenu, borderwidth=1, background="indian red").place(relx=0.98,rely=0,relwidth=0.02, relheight=1)
fentree.place(relx=0.02,rely=0,relwidth=0.4, relheight=1)
fsortie.place(relx=0.44,rely=0,relwidth=0.56, relheight=1)
Label(fentree,text="Entrez la taille de la matrice:", foreground="blue", font="arial 14 bold", bg="azure").grid(row=0 ,column=0,ipadx=40)
ordreMat=Entry(fentree,font="arial 16 ", width=5)
ordreMat.grid(padx=20, pady=20, row=0 ,column=1)
bu1=Button(fentree,text="valider",bg="white",fg="red",activebackground='yellow',font="arial 12 bold",width="5",command = menu)
bu1.place(relx=0.4,rely=0.2)

fenetre.mainloop()

