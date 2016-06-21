#!/usr/bin/python2.7
# -*-coding:Utf-8 -*


from Tkinter import *
from tkMessageBox import *
from erlan import *

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



def traitement0():
  theta=float(lamda.get())/float(mu.get())
  nbs=int(nb.get())
  rho=int(nbs-theta)
  if theta<1:
    nu=calcul_nu()
    tf=calcul_t()
    n=calcul_n()
    lfsortie=LabelFrame(fsortie,text="Résultats",font=('Helvetica', 12),labelanchor = N,bg='#80c0c0')
    lfsortie.pack(padx=5, pady=5, expand="yes")
    Label(lfsortie,text="ν (Longueur moyenne de la file d'attente):", font=('Helvetica', 12),bg='#80c0c0').grid(padx=5, pady=5, row=0 ,column=0)
    Label(lfsortie,text="n (Nombre moyen de clients dans le systéme):", font=('Helvetica', 12),bg='#80c0c0').grid(padx=5, pady=5, row=1 ,column=0)
    Label(lfsortie,text="tf (Temps moyen d'attente dans la file d'attente):", font=('Helvetica', 12),bg='#80c0c0').grid(padx=5, pady=5, row=2 ,column=0)
    Label(lfsortie,text="ρ (Nombre de serveurs inoccupés):", font=('Helvetica', 12),bg='#80c0c0').grid(padx=5, pady=5, row=3 ,column=0)
    Label(lfsortie,text=nu, font="arial 15 ",bg='#80c0c0').grid(padx=5, pady=5, row=0 ,column=1)
    Label(lfsortie,text=n, font="arial 15 ",bg='#80c0c0').grid(padx=5, pady=5, row=1 ,column=1)
    Label(lfsortie,text=tf, font="arial 15 ", bg='#80c0c0').grid(padx=5, pady=5, row=2 ,column=1)
    Label(lfsortie,text=rho, font="arial 15 ", bg='#80c0c0').grid(padx=5, pady=5, row=3 ,column=1)

def traitement1():
  theta=float(lamda.get())/float(mu.get())
  nbs=int(nb.get())
  probaPertB=B(theta,nbs)
  traficEcoule=TrafEc(theta,nbs)
  lfsortie=LabelFrame(fsortie,text="Résultats",font=('Helvetica', 12),labelanchor = N,bg='#80c0c0')
  lfsortie.pack(padx=5, pady=5, expand="yes")
  Label(lfsortie,text="La probabilité de Perte:", font=('Helvetica', 12),bg='#80c0c0').grid(padx=5, pady=5, row=0 ,column=0)
  Label(lfsortie,text="Le trafic Ecoulé:", font=('Helvetica', 12),bg='#80c0c0').grid(padx=5, pady=5, row=1 ,column=0)
  Label(lfsortie,text=probaPertB, font="arial 15 ",bg='#80c0c0').grid(padx=5, pady=5, row=0 ,column=1)
  Label(lfsortie,text=traficEcoule, font="arial 15 ",bg='#80c0c0').grid(padx=5, pady=5, row=1 ,column=1)

def traitement2():
  global lamda
  global mu
  global nb
  theta=float(lamda.get())/float(mu.get())
  lamda=int(lamda.get())
  mu=int(mu.get())
  nbs=int(nb.get())
  if theta<1:
    probaAttenteC=C(theta,nbs)
    nbrClientAttente=Q(theta,nbs)
    tempMoyFil=tempMoy(theta,nbs,lamda)
    tauxSejour=t(theta,nbs,mu,lamda)
    lfsortie=LabelFrame(fsortie,text="Résultats",font=('Helvetica', 12),labelanchor = N,bg='#80c0c0')
    lfsortie.pack(padx=5, pady=5, expand="yes")
    Label(lfsortie,text="La probabilité d'attente:", font=('Helvetica', 12),bg='#80c0c0').grid(padx=5, pady=5, row=0 ,column=0)
    Label(lfsortie,text="Le nombre de clients en attente:", font=('Helvetica', 12),bg='#80c0c0').grid(padx=5, pady=5, row=1 ,column=0)
    Label(lfsortie,text="Le temps moyen d'attente dans la file:", font=('Helvetica', 12),bg='#80c0c0').grid(padx=5, pady=5, row=2 ,column=0)
    Label(lfsortie,text="Le taux de séjour dans le systéme:", font=('Helvetica', 12),bg='#80c0c0').grid(padx=5, pady=5, row=3 ,column=0)
    Label(lfsortie,text=probaAttenteC, font="arial 15 ",bg='#80c0c0').grid(padx=5, pady=5, row=0 ,column=1)
    Label(lfsortie,text=nbrClientAttente, font="arial 15 ",bg='#80c0c0').grid(padx=5, pady=5, row=1 ,column=1)
    Label(lfsortie,text=tempMoyFil, font="arial 15 ", bg='#80c0c0').grid(padx=5, pady=5, row=2 ,column=1)
    Label(lfsortie,text=tauxSejour, font="arial 15 ", bg='#80c0c0').grid(padx=5, pady=5, row=3 ,column=1)



def Apropos():
  Aproposfen = Tk()
  Aproposfen.configure(bg ='#80c0c0')
  Aproposfen.title("Dimensionnement")
  s="Cette application a été réalisée dans le cadre \n du cours outils maths pour le dimensionnement. Ce module \n a été dispensé par le Docteur Samuel OUYA\n à l'école Supérieure Polytechnique de Dakar."
  Labelapro = Label(Aproposfen, text=s,bg="white", font=("Arial", 12, "bold"))
  Boutonqt = Button(Aproposfen, text="Quitter", font=("Arial", 12, "bold"), fg='white', bg='red', command=Aproposfen.destroy)
  Labelapro.grid(row=0, column=0, padx=5, pady=5)
  Boutonqt.grid(row=2, column=0, padx=5, pady=5)
  Aproposfen.mainloop()

def ErlangB():
  global lamda
  global mu
  global nb
  fint[0].configure(state=DISABLED)
  fint[2].configure(state=DISABLED)
  lfentree=LabelFrame(fentree,text="Paramètres d'entrées",font=('Helvetica', 12),labelanchor = N,bg ='#80c0c0')
  lfentree.pack( expand="yes")
  Label(lfentree,text="λ (clients/seconde):", font=('Helvetica', 12),bg ='#80c0c0').grid(row=0 ,column=0)
  lamda=Entry(lfentree,font="arial 15 ", width=10)
  Label(lfentree,text="μ (clients/seconde):", font=('Helvetica', 12),bg ='#80c0c0').grid(row=1 ,column=0)
  Label(lfentree,text="N (Nombre de serveurs):", font=('Helvetica', 12),bg ='#80c0c0').grid(row=2 ,column=0)
  lamda=Entry(lfentree,font="arial 15 ", width=10)
  lamda.grid(row=0 ,column=1)
  mu=Entry(lfentree,font="arial 15 ", width=10)
  mu.grid(row=1 ,column=1)
  nb=Entry(lfentree,font="arial 15 ", width=10)
  nb.grid( row=2 ,column=1)
  b1=Button(lfentree,text='Calculer',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE ,command=traitement1)
  b1.grid(row=4,column=0)

def ErlangC():
  global lamda
  global mu
  global nb
  fint[0].configure(state=DISABLED)
  fint[1].configure(state=DISABLED)
  lfentree=LabelFrame(fentree,text="Paramètres d'entrées",font=('Helvetica', 12),labelanchor = N,bg ='#80c0c0')
  lfentree.pack( expand="yes")
  Label(lfentree,text="λ (clients/seconde):", font=('Helvetica', 12),bg ='#80c0c0').grid(row=0 ,column=0)
  lamda=Entry(lfentree,font="arial 15 ", width=10)
  Label(lfentree,text="μ (clients/seconde):", font=('Helvetica', 12),bg ='#80c0c0').grid(row=1 ,column=0)
  Label(lfentree,text="N (Nombre de serveurs):", font=('Helvetica', 12),bg ='#80c0c0').grid(row=2 ,column=0)
  lamda=Entry(lfentree,font="arial 15 ", width=10)
  lamda.grid(row=0 ,column=1)
  mu=Entry(lfentree,font="arial 15 ", width=10)
  mu.grid(row=1 ,column=1)
  nb=Entry(lfentree,font="arial 15 ", width=10)
  nb.grid( row=2 ,column=1)
  b1=Button(lfentree,text='Calculer',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE ,command=traitement2)
  b1.grid(row=4,column=0)

def File_attente():
  global lamda
  global mu
  global nb
  fint[1].configure(state=DISABLED)
  fint[2].configure(state=DISABLED)
  lfentree=LabelFrame(fentree,text="Paramètres d'entrées",font=('Helvetica', 12),labelanchor = N,bg ='#80c0c0')
  lfentree.pack( expand="yes")
  Label(lfentree,text="λ (clients/seconde):", font=('Helvetica', 12),bg ='#80c0c0').grid(row=0 ,column=0)
  lamda=Entry(lfentree,font="arial 15 ", width=10)
  Label(lfentree,text="μ (clients/seconde):", font=('Helvetica', 12),bg ='#80c0c0').grid(row=1 ,column=0)
  Label(lfentree,text="N (Nombre de serveurs):", font=('Helvetica', 12),bg ='#80c0c0').grid(row=2 ,column=0)
  lamda=Entry(lfentree,font="arial 15 ", width=10)
  lamda.grid(row=0 ,column=1)
  mu=Entry(lfentree,font="arial 15 ", width=10)
  mu.grid(row=1 ,column=1)
  nb=Entry(lfentree,font="arial 15 ", width=10)
  nb.grid( row=2 ,column=1)
  b1=Button(lfentree,text='Calculer',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE ,command=traitement0)
  b1.grid(row=4,column=0)

#------------------------------------------------------------

# Interface Graphique
fen=Tk()
fen.title("Calcul Matriciel")
fen.geometry("900x700")
fen.resizable(True, False)
		
		#L'entete
f0 = Frame( fen, bg ='#80c0c0', bd =5, relief =RAISED)
f0.pack(side=TOP)
Entete=Label( f0,text='UNIVERSITE CHEIKH ANTA DIOP\nECOLE SUPERIEURE POLYTECHNIQUE DE DAKAR\nPROGRAMME DE DIMENSIONNEMENT', width=100, height=5, bd=5, relief=RAISED, bg='white',font=('Helvetica', 10))
Entete.grid(row =1, column =1, columnspan =3, padx =10, pady =5)
texte = Label( f0, text ='Serigne Fallou NDIAYE\nDIC-1 Télécoms&Réseaux 2014/2015\nProfesseur: Dr. OUYA', width='60', height=5, bd=5, bg='white',font=('Helvetica', 12))
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
body= Frame( fen, bg ='#80c0c0', bd =5, relief =RAISED, )
body.pack(pady=10)
#Menu de gauche
f1 = Frame( body, bg = 'royal blue')
f1.grid(row=1, column=1, padx =5)
# on cree les 6 buttons avec une boucle for
fint = [0]*5
for (i, col, rel, txt) in [(0, 'white', RAISED, 'File d\'attente'),
					(1, 'white', RAISED, 'Erlang B'),
					(2, 'white', RAISED, 'Erlang C'),
					(3, 'white', RAISED, 'A propos'),
					(4, 'white', RAISED, 'Quitter')]:
    #traitement="traitement"+str(i+6) 
    fint[i] = Button( f1,text=txt, bd=5, relief=rel,  bg =col, width=20, overrelief=RIDGE)
    fint[i].pack(side =TOP, padx =10, pady =5)
#fonctions lies aux boutons
fint[0].configure(command=File_attente)
fint[1].configure(command=ErlangB)
fint[2].configure(command=ErlangC)
fint[3].configure(command=Apropos)
fint[4].configure(command=fen.destroy)

# L'interface des saisies 
f2 = Frame( body, bg = 'royal blue', bd =2, relief =GROOVE)
f2.grid(row=1, column=2, padx =5)

fcontenu=Frame(f2, borderwidth=1,bg ='royal blue')
fcontenu.pack(expand="yes",fill="both",)
fentree=Frame(fcontenu, borderwidth=1)
fentree.pack(pady=5)




# zone des matrices et des résultats

fsortie=Frame(fcontenu, borderwidth=1,bg ='#80c0c0')
fsortie.pack()
    


"""# On va desactiver les 6 boutons au demarrage
for i in range(5):
    fint[i].configure(state=NORMAL)"""

		
fen.mainloop()
