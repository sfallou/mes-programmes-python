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

def  erlangB(A,N):
  a=0
  for i in range(N+1):
    a+=puissance(A,i)/factoriel(i)
  An=puissance(A,N)
  Nfact=factoriel(N)
  r=An/Nfact
  pb=r/a
  return pb

def nbCircuits(A, a, pb, c):
  i = 1
  j = 0
  for j in range(c):
    if A[j][0]==pb:
      for i in range(53):
        print(str(i))
        if A[j][i]==a or (A[j][i]<a and A[j][i+1]>a) :
          print(str(i))
          break
        #i = i+1
    #j = j+1
  return i

def nbCircuitsC(A, a, pb, c):
  i = 1
  j = 0
  for j in range(c):
    if A[j][0]==pb:
      for i in range(51):
        print(str(i))
        if A[j][i]==a or (A[j][i]<a and A[j][i+1]>a) :
          print(str(i))
          break
        #i = i+1
    #j = j+1
  return i

def calcul():
  print("ok")

def Calculer1():
  print("ok")

def Calculer3():
  print("ok")

def traficB(A,N,pb,c):
  i = 0
  while(i<=(c-1)) and (A[i][0]!=pb):
    i=i+1
  return A[i][N]

def erlangC(A,N):
  a=0
  for k in range(N):
    a+=puissance(A,k)/factoriel(k)
  a+=puissance(A,N)/(factoriel(N)*(1-A/N))
  p0=1/a
  A=puissance(A,N)/(factoriel(N)*(1-A/N))
  r=A*p0
  return r

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

def ErlangB():
    fint[0].configure(state=DISABLED)
    fint[2].configure(state=DISABLED)
    FrameP = Frame(fcontenu)
    #les 3 Frames
    Frame1 = Frame(FrameP, borderwidth=2, bd=2, relief=SUNKEN)
    Frame2 = Frame(FrameP, borderwidth=2, bd=2, relief=SUNKEN)
    Frame3 = Frame(FrameP, borderwidth=2, bd=2, relief=SUNKEN)

    FrameResultat = Frame(FrameP, bg='white')

    #Frame 1
    #Les labels
    LabelTete1 = Label(Frame1, text="Probabilité(blocage)", font=('Helvetica', 12))
    LabTraficOffert1 = Label(Frame1, text='Traffic Offert', font=('Helvetica', 12))
    LabNbCircuits1 = Label(Frame1, text="Circuits", font=('Helvetica', 12))
    #Les champs de texte
    ChampTrafic1 = Entry(Frame1, width=7, font=('Helvetica', 12), justify=CENTER)
    ChampCircuits = Entry(Frame1, width=7, font=('Helvetica', 12), justify=CENTER)
    #Bouton
    Calculer1 = Button(Frame1, text="Calculer", bg='blue', fg='white', font=("Arial", 12, "bold"))
    #Dispositions
    LabelTete1.grid(row=0, columnspan=2, ipady=7)
    LabTraficOffert1.grid(row=1, column=0)
    LabNbCircuits1.grid(row=2, column=0)
    ChampTrafic1.grid(row=1, column=1)
    ChampCircuits.grid(row=2, column=1)
    Calculer1.grid(row=3, columnspan=2)

    #Frame 2
    #Les labels
    LabelTete2 = Label(Frame2, text="Trafic Offert", font=('Helvetica', 12))
    LabProbaBloc2 = Label(Frame2, text='Probabilité(blocage)', font=('Helvetica', 12))
    LabNbCircuits2 = Label(Frame2, text="Circuits", font=('Helvetica', 12))
    #Les champs de texte
    ChampProbaBloc2 = Entry(Frame2, width=7, font=('Helvetica', 12), justify=CENTER)
    ChampCircuits2 = Entry(Frame2, width=7, font=('Helvetica', 12), justify=CENTER)
    #Bouton
    Calculer2 = Button(Frame2, text="Calculer", bg='blue', fg='white', font=("Arial", 12, "bold"))
    #Dispositions
    LabelTete2.grid(row=0, columnspan=2, ipady=7)
    LabProbaBloc2.grid(row=1, column=0)
    LabNbCircuits2.grid(row=2, column=0)
    ChampProbaBloc2.grid(row=1, column=1)
    ChampCircuits2.grid(row=2, column=1)
    Calculer2.grid(row=3, columnspan=2)

    #Frame 3
    #Les labels
    LabelTete3 = Label(Frame3, text="Nombre de Circuits", font=('Helvetica', 12))
    LabProbaBloc3 = Label(Frame3, text='Probabilité(Blocage en %)', font=('Helvetica', 12))
    LabTraficOffert3 = Label(Frame3, text="Trafic Offert", font=('Helvetica', 12))
    #Les champs de texte
    ChampProbaBloc3 = Entry(Frame3, width=7, font=('Helvetica', 12), justify=CENTER)
    ChampTraficOffert3 = Entry(Frame3, width=7, font=('Helvetica', 12), justify=CENTER)
    #Bouton
    Calculer3 = Button(Frame3, text="Calculer", bg='blue', fg='white', font=("Arial", 12, "bold"))
    #Dispositions5
    LabelTete3.grid(row=0, columnspan=2, ipady=7)
    LabProbaBloc3.grid(row=1, column=0)
    LabTraficOffert3.grid(row=2, column=0)
    ChampProbaBloc3.grid(row=1, column=1)
    ChampTraficOffert3.grid(row=2, column=1)
    Calculer3.grid(row=3, columnspan=2)


    #Dispositions des frames
    Frame1.grid(row=0, column=0)
    Frame2.grid(row=0, column=1)
    Frame3.grid(row=0, column=2)
    
    FrameP.pack()
  
def ErlangC():
  print('ok')
def Apropos():
  print('ok')

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
