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

def calcul_n():  #Le nombre moyen de clients dans le systemes
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
		lfsortie=LabelFrame(fsortie,text="Résultats",font="arial 12 bold italic",labelanchor = N,bg='white')
		lfsortie.pack(padx=5, pady=5, expand="yes")
		Label(lfsortie,text="ν (La longueur moyenne de la file d'attente):", font="arial 12 bold",bg='white').grid(padx=5, pady=20, row=0 ,column=0)
		Label(lfsortie,text="n (Le nombre moyen de clients dans le systéme):", font="arial 12 bold",bg='white').grid(padx=5, pady=20, row=1 ,column=0)
		Label(lfsortie,text="tf (Le temps moyen d'attente dans la file d'attente):", font="arial 12 bold",bg='white').grid(padx=5, pady=20, row=2 ,column=0)
		Label(lfsortie,text="ρ (Le nombre de serveurs inoccupés):", font="arial 12 bold",bg='white').grid(padx=5, pady=20, row=3 ,column=0)
		Label(lfsortie,text=nu, font="arial 12 bold",bg='red').grid(padx=5, pady=20, row=0 ,column=1)
		Label(lfsortie,text=n, font="arial 12 bold",bg='red').grid(padx=5, pady=20, row=1 ,column=1)
		Label(lfsortie,text=tf, font="arial 12 bold",bg='red').grid(padx=5, pady=20, row=2 ,column=1)
		Label(lfsortie,text=rho, font="arial 12 bold",bg='red').grid(padx=5, pady=20, row=3 ,column=1)



# Interface Graphique
fen=Tk()
fen.title("Dimensionnement")
fen.geometry("1150x650")
fen.resizable(True, True)
		
		#L'entete
f0 = Frame( fen, bg ='#80c0c0', bd =5, relief =RAISED)
f0.pack(side=TOP)
Entete=Label( f0,text='UNIVERSITE CHEIKH ANTA DIOP\nECOLE SUPERIEURE POLYTECHNIQUE DE DAKAR\nDimensionnement Réseaux', width=100, height=5, bd=5, relief=RAISED, bg='white',font=('Helvetica', 10))
Entete.grid(row =1, column =1, columnspan =3, padx =10, pady =5)
texte = Label( f0, text ='Serigne Fallou NDIAYE\nDIC-1 Télécoms&Réseaux 2014/2015\nProfesseur: Dr. OUYA\n Phénomene d\'attente avec plusieurs serveurs', width='60', height=5, bd=5, bg='white',font=('Helvetica', 12))
texte.grid(row =2, column =2, padx =5, pady =5)
		
#Images   
image = PhotoImage(file ="me.gif")
canIm = Canvas( f0, height = "130", width = "130", bg= "green")
canIm.create_image(90, 90, image =  image)
canIm.grid(row =2, column =3, sticky=E, rowspan =3, padx =10, pady =5)
     
image2 = PhotoImage(file ="logoesp.gif")
canIm2 = Canvas( f0, height = "130", width = "130", bg= "green")
canIm2.create_image(90, 90, image =  image2)
canIm2.grid(row =2, column =1, sticky=W, rowspan =3, padx =10, pady =5)

# Conteneur du body
body= Frame( fen, bg ='#80c0c0', bd =5, relief =RAISED,  width=100,)
body.pack(pady=10)

#Contenu de gauche
f1 = Frame( body, bg = 'royal blue')
f1.grid(row=1, column=1, padx =5)

fcontenu=Frame(f1, borderwidth=1,bg ='#80c0c0')
fcontenu.pack(padx=5,pady=5,expand="yes",fill="both",)
fentree=Frame(fcontenu, borderwidth=1,bg ='#80c0c0')
lfentree=LabelFrame(fentree,text="Les entrées",font="arial 12 bold italic",labelanchor = N,bg='white')
fentree.grid(pady=5, row=0,column=0)
lfentree.pack(padx=3, pady=5, expand="yes")
Label(lfentree,text="λ (Nombre de clients entrants/seconde):", font="arial 12 bold",bg='white').grid(padx=5, pady=10, row=0 ,column=0)
lamda=Entry(lfentree,font="arial 15 ", width=10)
Label(lfentree,text="μ (Nombre de clients sortant/seconde):", font="arial 12 bold",bg='white').grid(padx=5, pady=10, row=1 ,column=0)
Label(lfentree,text="N (Nombre de serveurs du systemes):", font="arial 12 bold",bg='white').grid(padx=5, pady=10, row=2 ,column=0)
lamda=Entry(lfentree,font="arial 15 ", width=10)
lamda.grid(padx=5, pady=20, row=0 ,column=1)
mu=Entry(lfentree,font="arial 15 ", width=10)
mu.grid(padx=5, pady=20, row=1 ,column=1)
nb=Entry(lfentree,font="arial 15 ", width=10)
nb.grid(padx=5, pady=20, row=2 ,column=1)
b1=Button(lfentree,text='Calculer',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE ,command=traitement)
b1.grid(padx=5,pady=20,row=4,column=0)

		
# L'interface des saisies et des affichages a droite
f2 = Frame( body, bg = 'royal blue', bd =2, relief =GROOVE)
f2.grid(row=1, column=2, padx =5)
fcontenu2=Frame(f2, borderwidth=1,bg ='#80c0c0')
fcontenu2.pack(padx=5,pady=5,expand="yes",fill="both")
fsortie=Frame(fcontenu2, borderwidth=1,bg ='#80c0c0')
fsortie.grid(pady=5, row=0,column=1)
		
fen.mainloop()
