#!/usr/bin/python2.7
# -*-coding:Utf-8 -*


from Tkinter import *
from tkMessageBox import *

global lamda
global mu
global nb

def factoriel(n):
	res=1
	n=n+1
	for i in range(1,n):
		res=res*i
	return res


def puissance(p,n):
	res=1
	for i in range(n):
		res=res*p
	return res


def calcul_po():  #
	po1=0
	theta=float(lamda.get())/float(mu.get())
	for i in range(int(nb.get())+1):
		po1=po1+puissance(theta,i)/factoriel(i)
	po2=puissance(theta,int(nb.get())+1)/(factoriel(int(nb.get()))*(int(nb.get())-theta))	
		
	po=1/(po1+po2)	
	return po
	
def calcul_nu():  #Le nombre moyen de clients dans la file d'attente
	theta=float(lamda.get())/float(mu.get())
	m1=puissance(theta,int(nb.get())+1)*calcul_po()
	m2=int(nb.get())*factoriel(int(nb.get()))*puissance(1-theta/int(nb.get()),2)	
	m=m1/m2
	return m

def calcul_n():  #Le nombre moyen de cloients dans le systemes
	theta=float(lamda.get())/float(mu.get())
	n1=calcul_nu()+theta
	return n1

def calcul_t(): #Temps moyen d'attente
	theta=float(lamda.get())/float(mu.get())
	tf=calcul_nu()/float(lamda.get())	
	return tf

def traitement():
	theta=float(lamda.get())/float(mu.get())
	nbs=int(nb.get())
	rho=int(nbs-theta)
	if theta<1:
		nu=calcul_nu()
		tf=calcul_t()
		n=calcul_n()
		lfsortie=LabelFrame(fsortie,text="Les sorties",font="arial 12 bold italic",labelanchor = N)
		lfsortie.pack(padx=5, pady=5, expand="yes")
		Label(lfsortie,text="ν (La longueur moyenne de la file d'attente):", font="arial 12 bold").grid(padx=5, pady=20, row=0 ,column=0)
		Label(lfsortie,text="n (Le nombre moyen de clients dans le systéme):", font="arial 12 bold").grid(padx=5, pady=20, row=1 ,column=0)
		Label(lfsortie,text="tf (Le temps moyen d'attente dans la file d'attente):", font="arial 12 bold").grid(padx=5, pady=20, row=2 ,column=0)
		Label(lfsortie,text="ρ (Le nombre de serveurs inoccupés):", font="arial 12 bold").grid(padx=5, pady=20, row=3 ,column=0)
		Label(lfsortie,text=nu, font="arial 12 bold").grid(padx=5, pady=20, row=0 ,column=1)
		Label(lfsortie,text=n, font="arial 12 bold").grid(padx=5, pady=20, row=1 ,column=1)
		Label(lfsortie,text=tf, font="arial 12 bold").grid(padx=5, pady=20, row=2 ,column=1)
		Label(lfsortie,text=rho, font="arial 12 bold").grid(padx=5, pady=20, row=3 ,column=1)

		

fenetre = Tk()
fenetre.geometry("1150x400")
fenetre.title("Phenomene d'attente")
ftitre=Frame(fenetre, borderwidth=1, relief=RAISED,bg='white')
ftitre.pack(padx=5, pady=5)
titre=Label(ftitre,text="Phénomene d'attente à un nombre donné de serveurs", font="arial 17 bold italic ")
titre.pack(expand="yes",fill="both")
fcontenu=Frame(fenetre, borderwidth=1)
fcontenu.pack(padx=5,pady=5,expand="yes",fill="both")
fentree=Frame(fcontenu, borderwidth=1)
fsortie=Frame(fcontenu, borderwidth=1)
lfentree=LabelFrame(fentree,text="Les entrées",font="arial 12 bold italic",labelanchor = N)
fentree.grid(pady=5, row=0,column=0)
fsortie.grid(pady=5, row=0,column=1)
lfentree.pack(padx=3, pady=5, expand="yes")
Label(lfentree,text="λ (Nombre de clients entrants/unité de temps):", font="arial 12 bold").grid(padx=5, pady=20, row=0 ,column=0)
lamda=Entry(lfentree,font="arial 15 ", width=10)
Label(lfentree,text="μ (Nombre de clients sortant/unité de temps):", font="arial 12 bold").grid(padx=5, pady=20, row=1 ,column=0)
Label(lfentree,text="N (Nombre de serveurs du systemes):", font="arial 12 bold").grid(padx=5, pady=20, row=2 ,column=0)
lamda=Entry(lfentree,font="arial 15 ", width=10)
lamda.grid(padx=5, pady=20, row=0 ,column=1)
mu=Entry(lfentree,font="arial 15 ", width=10)
mu.grid(padx=5, pady=20, row=1 ,column=1)
nb=Entry(lfentree,font="arial 15 ", width=10)
nb.grid(padx=5, pady=20, row=2 ,column=1)
b1=Button(lfentree,text="RESULTAT",bg="gray",font="arial 8 bold",width="15" ,command=traitement)
b1.grid(padx=5,pady=20,row=4,column=0)


fenetre. mainloop()
