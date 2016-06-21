# -*- coding: utf-8 -*-
from Tkinter import *
from time import *

A = list()
B = list()


line = 0
line2 = 0
posLine1 = 0 
posLine2= line



def creer_matrice(n, p, X) :
  A = n * [None]
  for i in range(n) :
    A[i ] = p * [X]
  return A

def identite(identite,ligne,colonne) :
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
def permutation(matrice,matId,k,pivot) :
    mat=list()
    mat.append(matrice[k])
    matrice[k] = matrice[pivot]
    matrice[pivot]= mat[0]
    mat=list()
    mat.append(matId[k])
    matId[k] = matId[pivot]
    matId[pivot] =  mat[0]
    return matrice,matId
def elimination(matrice,identite,pivot,ligne,colonne ) :
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
def remonte(matrice,matId,ligne, colonne ) :
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
    matriceIdentite =identite(matriceIdentite,ligne,colonne)
    k=0
    arret = 1
    while k<ligne and arret == 1 :
        pivot=recherchePivot(matrice,k,ligne)
        if pivot==k :
            matrice,matriceIdentite =elimination(matrice,matriceIdentite,pivot,ligne,colonne)
            k=k+1
        else :
            if pivot==-1 :
                arret = 0
            else :
                matrice,matriceIdentite = permutation(matrice,matriceIdentite,k,pivot)
                pivot = k
                matrice,matriceIdentite =elimination(matrice,matriceIdentite,pivot,ligne,colonne)
                k=k+1
    if arret==1 and matrice[ligne-1][colonne-1]!=0 :
            matrice,matriceIdentite = remonte(matrice,matriceIdentite,ligne,colonne)
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

"""Fonction qui permute deux colonnes d une matrice"""
def PermCol(M,j,i):
  for k in range(len(M)-1,-1,-1):
    (M[k][j],M[k][i])=(M[k][i],M[k][j])


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
def determinant(M):
  (Mtriang,sign)=Triangule(M)
  return round(sign*ProdDiag(Mtriang),2)


#les methodes

def nombreDeMatrice( ):
  global nombreLigne,nombreColonne,nombreLigne2,nombreColonne2,nombreMatrice
  try:
    if  nombreMatrice.get()==1:
      # res.delete(0.0, END)
      # On va activer les 4 derniers menus
      for i in range(2,5):
         fint[i].configure(state=ACTIVE) 
      # On demande la taille de la matrice
      nombreLigne = IntVar()
      nombreLigne.set(1)
      nombreColonne = IntVar()
      nombreColonne.set(1)
      labLigne=Label( f2_1,text="Nombre Ligne Matrice:",bg='white').grid(row=1,column=1)
      Entree2=Entry( f2_1,width=5,textvariable=nombreLigne,font="arial 13", 
           justify=CENTER).grid(row=1,column=2)
      labCol=Label( f2_1,text="Nombre Colonne Matrice:",bg='white').grid(row=1,column=3)
      Entree3=Entry( f2_1,width=5,textvariable=nombreColonne,font="arial 13", 
          justify=CENTER).grid(row=1,column=4)
      butLigne=Button( f2_1, text='OK',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE,command=getMatrice).grid(row=1,column=5,padx=4)

    elif  nombreMatrice.get()==2:
      # res.delete(0.0, END)
      # On va activer les 2 premiers menus
      for i in range(2):
         fint[i].configure(state=ACTIVE)
      # On demande la taille des matrices
      nombreLigne = IntVar()
      nombreLigne.set(1)
      nombreColonne = IntVar()
      nombreColonne.set(1)
      nombreLigne2 = IntVar()
      nombreLigne2.set(1)
      nombreColonne2 = IntVar()
      nombreColonne2.set(1)
      labLigne=Label( f2_1,text="Nombre Ligne Matrice1:",bg='white').grid(row=1,column=1)
      Entree2=Entry( f2_1,width=5,textvariable=nombreLigne,font="arial 13", 
         justify=CENTER).grid(row=1,column=2)
      labCol=Label( f2_1,text="Nombre Colonne Matrice1:",bg='white').grid(row=1,column=4)
      Entree3=Entry( f2_1,width=5,textvariable=nombreColonne,font="arial 13", 
         justify=CENTER).grid(row=1,column=5)
      labLigne2=Label( f2_1,text="Nombre Ligne Matrice2:",bg='white').grid(row=2,column=1)
      Entree3=Entry( f2_1,width=5,textvariable=nombreLigne2,font="arial 13", 
         justify=CENTER).grid(row=2,column=2)
      labCol2=Label(f2_1,text="Nombre Colonne Matrice2:",bg='white').grid(row=2,column=4)
      Entree4=Entry(f2_1,width=5,textvariable=nombreColonne2,font="arial 13", 
         justify=CENTER).grid(row=2,column=5)
      butLigne=Button(f2_1, text='OK',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE,command=getDeuxMatrice).grid(row=3,column=3,padx=4)

          
  except:
       resultatText = "Erreur! La valeur saisie doit être égale à 1 ou 2"
      # res.delete(0.0, END)
      # res.insert(5.5, resultatText)

    
def getMatrice():
  fint[2].configure(command=Determinant)
  fint[3].configure(command=Inverse)
  fint[4].configure(command=Transpose)
  # matrice A
  for i in range(nombreLigne.get()):
      A.append([])
      for j in range(nombreColonne.get()):
        A[i].append([])
  for i in range(nombreLigne.get()):
      for j in range(nombreColonne.get()):
        A[i][j]=DoubleVar()
  line = 0
  for i in range(nombreLigne.get()):
      col=10
      for j in range(nombreColonne.get()):
          Entry( res, textvariable=A[i][j], width=5).grid(row=line,column=col, padx=2,pady=2)  
          col +=1
      line +=1
  posColAfter= col+15
  return A

def getDeuxMatrice():
  fint[0].configure(command=Produit)
  fint[1].configure(command=Somme)
  # matrice A
  for i in range(nombreLigne.get()):
      A.append([])
      for j in range(nombreColonne.get()):
        A[i].append([])
  for i in range(nombreLigne.get()):
      for j in range(nombreColonne.get()):
        A[i][j]=DoubleVar()
  line = 0
  for i in range(nombreLigne.get()):
      col=10
      for j in range(nombreColonne.get()):
          Entry( res, textvariable=A[i][j], width=5).grid(row=line,column=col, padx=2,pady=2)  
          col +=1
      line +=1
  posColAfter= col+15
 
  # séparation
  equalSymbol = Canvas(res, width=40, height=10* nombreLigne.get(),  bd=-2,bg="white")
  equalSymbol.create_text(21, 5* nombreLigne.get(), anchor=CENTER, text="-*-*-", font=("arial", 5* nombreLigne.get()))
  equalSymbol.grid(row=(posLine1), column=col+5, rowspan= nombreLigne.get(),padx=2,pady=2)
       # matrice B
  for i in range(nombreLigne2.get()):
      B.append([])
      for j in range(nombreColonne2.get()):
        B[i].append([])
  for i in range(nombreLigne2.get()):
      for j in range(nombreColonne2.get()):
        B[i][j]=DoubleVar()
  line2 = 0
  for i in range(nombreLigne2.get()):
          col2=50+ nombreColonne2.get()
          for j in range(nombreColonne2.get()):
                Entry(res, textvariable=B[i][j], width=5).grid(row=line2,column=col2, padx=2,pady=2)  
                col2 +=1
          line2 +=1
  return A,B
      
def Produit():
  print("produit")
  #for w in  res.winfo_children():
    #w.destroy()
  if  nombreColonne.get()== nombreLigne2.get():
    resultat = list()
    for i in range(nombreLigne.get()):
        for j in range(nombreColonne.get()):
            A[i][j]= float( (A[i][j]).get() )
            print A[i][j] 
    for i in range(nombreLigne2.get()):
        for j in range(nombreColonne2.get()):        
            B[i][j]= float( (B[i][j]).get() ) 
            print B[i][j]
    for i in range(nombreLigne.get()):
        ligne = list()
        for j in range(nombreColonne2.get()):
            element = 0
            for k in range(len(A[0])):
                element= element+ A[i][k]*B[k][j]
            ligne.append(element)
        resultat.append(ligne)
  #affichage du resultat
    for i in range(nombreLigne.get()):
      for j in range(nombreColonne2.get()):
        print resultat[i][j]
    Label(res, text= "Le résultat du produit est : ",fg="blue",bg="#80c0c0").grid(row=10,column=0)
    line3 = 11
    for i in range(nombreLigne.get()):
        col3=1
        for j in range(nombreColonne2.get()):
              Label(res, text=resultat[i][j],fg="red",bg="white").grid(row=line3,column=col3,padx=3,pady=3)  
              col3 +=1
        line3 +=1 
  else:
    resultat="Impossible d'effectuer le produit!"
    print(resultat)
    Label(res, text= resultat,fg="red",bg="#80c0c0").grid(row=10,column=4)
    
  return  resultat

def Somme():
  print("Somme")
  #for w in  res.winfo_children():
     #w.destroy()
  if  nombreColonne.get()== nombreColonne2.get() and  nombreLigne.get()== nombreLigne2.get():
    for i in range(nombreLigne.get()):
      for j in range(nombreColonne.get()):
        A[i][j]= float( (A[i][j]).get() )
        B[i][j]= float( (B[i][j]).get() )
        print A[i][j],B[i][j]
    resultat = list()
    for i in range(len(A)):
      colonne = list()
      for j in range(len(B)):
        colonne.append((A[i][j])+(B[i][j]))
      resultat.append(colonne)
      #affichage du resultat
    for i in range(nombreLigne.get()):
      for j in range(nombreColonne.get()):
        print resultat[i][j]
    Label(res, text= "Le résultat de la somme est : ",fg="blue",bg="#80c0c0").grid(row=10,column=0)
    line3 = 11
    for i in range(nombreLigne.get()):
        col3=1
        for j in range(nombreColonne.get()):
              Label(res, text=resultat[i][j],fg="red",bg="white").grid(row=line3,column=col3,padx=3,pady=3)  
              col3 +=1
        line3 +=1 
  else:
    resultat="Impossible d'effectuer la somme de ces deux matrices.Erreur de saisie!"
    print(resultat)
    Label(res, text= resultat,fg="red",bg="#80c0c0").grid(row=10,column=4)
    
  return  resultat

def Determinant():
  print("Determinant")
  if  nombreColonne.get()== nombreLigne.get():
    for i in range(nombreLigne.get()):
      for j in range(nombreColonne.get()):
        A[i][j]= float( (A[i][j]).get() )

    det=determinant(A)
    print(det)
    Label(res, text= "Le determinant de la matrice : ",fg="blue",bg="#80c0c0").grid(row=10,column=0)
    Label(res, text= det,fg="blue",bg="#80c0c0").grid(row=11,column=0)
    return det
  else:
    print("impossible")

def Inverse():
  print("Inverse")
  if  nombreColonne.get()== nombreLigne.get():
    for i in range(nombreLigne.get()):
      for j in range(nombreColonne.get()):
        A[i][j]= float( (A[i][j]).get() )
    if determinant(A)!=0:
      resultat=inverser(A,nombreLigne.get(),nombreColonne.get())
    else:
      resultat="impossible"
  else:
    resultat="impossible"

  if resultat=="impossible":
    Label(res, text= "Impossible de calculer l'inverse ",fg="blue",bg="#80c0c0").grid(row=10,column=0)
  else:
    Label(res, text= "Le résultat de l'inverse est : ",fg="blue",bg="#80c0c0").grid(row=10,column=0)
    line3 = 11
    for i in range(nombreLigne.get()):
        col3=1
        for j in range(nombreColonne.get()):
              Label(res, text=resultat[i][j],fg="red",bg="white").grid(row=line3,column=col3,padx=3,pady=3)  
              col3 +=1
        line3 +=1 
  print(resultat)
  return resultat
    

def Transpose():
  print("Transpose")
  for i in range(nombreLigne.get()):
    for j in range(nombreColonne.get()):
       A[i][j]= float( (A[i][j]).get() )
  n, p = dimensions(A)
  B = creer_matrice(p, n, None)
  for j in range(p) :
    for i in range(n) :
      B[j][i] = A[i][j]
  #print(A)
  #print(B)
  Label(res, text= "La Transposé de la matrice est : ",fg="blue",bg="#80c0c0").grid(row=10,column=0)
  line3 = 11
  for i in range(p):
      col3=1
      for j in range(n):
            Label(res, text=B[i][j],fg="red",bg="white").grid(row=line3,column=col3,padx=3,pady=3)  
            col3 +=1
      line3 +=1 
  print(A)
  print(B)
  return B


# Interface Graphique
fen=Tk()
fen.title("Calcul Matriciel")
fen.geometry("900x700")
fen.resizable(True, False)
		
		#L'entete
f0 = Frame( fen, bg ='#80c0c0', bd =5, relief =RAISED)
f0.pack(side=TOP)
Entete=Label( f0,text='UNIVERSITE CHEIKH ANTA DIOP\nECOLE SUPERIEURE POLYTECHNIQUE DE DAKAR\nPROGRAMME DE CALCUL MATRICIEL ET DE CALCUL NUMERIQUE', width=100, height=5, bd=5, relief=RAISED, bg='white',font=('Helvetica', 10))
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
for (i, col, rel, txt) in [(0, 'white', RAISED, 'Produit Matrices'),
					(1, 'white', RAISED, 'Addition Matrices'),
					(2, 'white', RAISED, 'Déterminant Matrice'),
					(3, 'white', RAISED, 'Inverse Matrice'),
					(4, 'white', RAISED, 'Transposé Matrice')]:
    fint[i] = Button( f1,text=txt, bd=5, relief=rel,  bg =col, width=20, overrelief=RIDGE)
    fint[i].pack(side =TOP, padx =10, pady =5)
# On va desactiver les 6 boutons au demarrage
for i in range(5):
    fint[i].configure(state=DISABLED) 
		
# L'interface des saisies et des affichages a droite
f2 = Frame( body, bg ='#80c0c0', bd =2, relief =GROOVE)
f2.grid(row=1, column=2, padx =5)
f2_1=Frame( f2, bg ='white', bd =2, relief =GROOVE)
f2_1.pack()
nombreMatrice = IntVar()
nombreMatrice.set(1)
lab1=Label( f2_1,text="Nombre de Matrice:",bg='white').grid(row=1,column=1)
Entree1=Entry( f2_1,width=5,textvariable=nombreMatrice,font="arial 13", 
       justify=CENTER).grid(row=1,column=2)
butt1=Button( f2_1, text='OK',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE,command=nombreDeMatrice).grid(row=1,column=5,padx=4)

# zone des matrices et des résultats
res=Frame( f2,bg='#80c0c0',width=590,height=350)
# res= Text( zoneRes,bg='blue',width=80,height=20)
res.pack(padx=5, pady=5)
# res.insert(4.0,"Zone des résultats")
		
fen.mainloop()
