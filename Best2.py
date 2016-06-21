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

# Interface Graphique (classe)
class Graphique:   
    def __init__ (self):
      self.fen=Tk()
      self.fen.title("Calcul Matriciel")
      self.fen.geometry("900x700")
      self.fen.resizable(False, False)
		
		#L'entete
      self.f0 = Frame(self.fen, bg ='#80c0c0', bd =5, relief =RAISED)
      self.f0.pack(side=TOP)
      self.Entete=Label(self.f0,text='UNIVERSITE CHEIKH ANTA DIOP\nECOLE SUPERIEURE POLYTECHNIQUE DE DAKAR\nPROGRAMME DE CALCUL MATRICIEL ET DE CALCUL NUMERIQUE', width=100, height=5, bd=5, relief=RAISED, bg='white',font=('Helvetica', 10))
      self.Entete.grid(row =1, column =1, columnspan =3, padx =10, pady =5)
      self.texte = Label(self.f0, text ='Serigne Fallou NDIAYE\nDIC-1 Télécoms&Réseaux 2014/2015\nProfesseur: Dr. OUYA', width='60', height=5, bd=5, bg='white',font=('Helvetica', 12))
      self.texte.grid(row =2, column =2, padx =5, pady =5)
		
    #Images   
      self.image = PhotoImage(file ="me.gif")
      self.canIm = Canvas(self.f0, height = "130", width = "130", bg= "green")
      self.canIm.create_image(90, 90, image = self.image)
      self.canIm.grid(row =2, column =3, sticky=E, rowspan =3, padx =10, pady =5)
      
      self.image2 = PhotoImage(file ="logoesp.gif")
      self.canIm2 = Canvas(self.f0, height = "130", width = "130", bg= "green")
      self.canIm2.create_image(90, 90, image = self.image2)
      self.canIm2.grid(row =2, column =1, sticky=W, rowspan =3, padx =10, pady =5)

    # Conteneur du body
      self.body= Frame(self.fen, bg ='#80c0c0', bd =5, relief =RAISED, )
      self.body.pack(pady=10)
		#Menu de gauche
      self.f1 = Frame(self.body, bg = 'royal blue')
      self.f1.grid(row=1, column=1, padx =5)
		# on cree les 6 buttons avec une boucle for
      self.fint = [0]*6
      for (i, col, rel, txt) in [(0, 'white', RAISED, 'Produit Matrices'),
									(1, 'white', RAISED, 'Addition Matrices'),
									(2, 'white', RAISED, 'Déterminant Matrice'),
									(3, 'white', RAISED, 'Inverse Matrice'),
									(4, 'white', RAISED, 'Transposé Matrice'),
									(5, 'white',RAISED, 'Résolution par Gauss')]:
        self.fint[i] = Button(self.f1,text=txt, bd=5, relief=rel,  bg =col, width=20, overrelief=RIDGE)
        self.fint[i].pack(side =TOP, padx =10, pady =5)
		# On va desactiver les 6 boutons au demarrage
      for i in range(6):
        self.fint[i].configure(state=DISABLED) 
		
		# L'interface des saisies et des affichages a droite
      self.f2 = Frame(self.body, bg ='#80c0c0', bd =2, relief =GROOVE)
      self.f2.grid(row=1, column=2, padx =5)
      self.f2_1=Frame(self.f2, bg ='white', bd =2, relief =GROOVE)
      self.f2_1.pack()
      self.nombreMatrice = IntVar()
      self.nombreMatrice.set(1)
      self.lab1=Label(self.f2_1,text="Nombre de Matrice:",bg='white').grid(row=1,column=1)
      self.Entree1=Entry(self.f2_1,width=5,textvariable=self.nombreMatrice,font="arial 13", 
              justify=CENTER).grid(row=1,column=2)
      self.butt1=Button(self.f2_1, text='OK',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE,command=self.nombreDeMatrice).grid(row=1,column=5,padx=4)

		 # zone des matrices et des résultats
      self.res=Frame(self.f2,bg='#80c0c0',width=590,height=350)
      #self.res= Text(self.zoneRes,bg='blue',width=80,height=20)
      self.res.pack(padx=5, pady=5)
      #self.res.insert(4.0,"Zone des résultats")
		
      self.fen.mainloop()

      #les methodes

    def nombreDeMatrice(self):
      try:
        if self.nombreMatrice.get()==1:
          #self.res.delete(0.0, END)
          # On va activer les 4 derniers menus
          for i in range(2,6):
            self.fint[i].configure(state=ACTIVE) 
          # On demande la taille de la matrice
          self.nombreLigne = IntVar()
          self.nombreLigne.set(1)
          self.nombreColonne = IntVar()
          self.nombreColonne.set(1)
          self.labLigne=Label(self.f2_1,text="Nombre Ligne Matrice:",bg='white').grid(row=1,column=1)
          self.Entree2=Entry(self.f2_1,width=5,textvariable=self.nombreLigne,font="arial 13", 
              justify=CENTER).grid(row=1,column=2)
          self.labCol=Label(self.f2_1,text="Nombre Colonne Matrice:",bg='white').grid(row=1,column=3)
          self.Entree3=Entry(self.f2_1,width=5,textvariable=self.nombreColonne,font="arial 13", 
              justify=CENTER).grid(row=1,column=4)
          self.butLigne=Button(self.f2_1, text='OK',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE,command=self.getMatrice).grid(row=1,column=5,padx=4)

        elif self.nombreMatrice.get()==2:
          #self.res.delete(0.0, END)
          # On va activer les 2 premiers menus
          for i in range(2):
            self.fint[i].configure(state=ACTIVE)
          # On demande la taille des matrices
          self.nombreLigne = IntVar()
          self.nombreLigne.set(1)
          self.nombreColonne = IntVar()
          self.nombreColonne.set(1)
          self.nombreLigne2 = IntVar()
          self.nombreLigne2.set(1)
          self.nombreColonne2 = IntVar()
          self.nombreColonne2.set(1)
          self.labLigne=Label(self.f2_1,text="Nombre Ligne Matrice1:",bg='white').grid(row=1,column=1)
          self.Entree2=Entry(self.f2_1,width=5,textvariable=self.nombreLigne,font="arial 13", 
              justify=CENTER).grid(row=1,column=2)
          self.labCol=Label(self.f2_1,text="Nombre Colonne Matrice1:",bg='white').grid(row=1,column=4)
          self.Entree3=Entry(self.f2_1,width=5,textvariable=self.nombreColonne,font="arial 13", 
              justify=CENTER).grid(row=1,column=5)
          self.labLigne2=Label(self.f2_1,text="Nombre Ligne Matrice2:",bg='white').grid(row=2,column=1)
          self.Entree3=Entry(self.f2_1,width=5,textvariable=self.nombreLigne2,font="arial 13", 
              justify=CENTER).grid(row=2,column=2)
          self.labCol2=Label(self.f2_1,text="Nombre Colonne Matrice2:",bg='white').grid(row=2,column=4)
          self.Entree4=Entry(self.f2_1,width=5,textvariable=self.nombreColonne2,font="arial 13", 
              justify=CENTER).grid(row=2,column=5)
          self.butLigne=Button(self.f2_1, text='OK',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE,command=self.getDeuxMatrice).grid(row=3,column=3,padx=4)

          
      except:
          self.resultatText = "Erreur! La valeur saisie doit être égale à 1 ou 2"
          #self.res.delete(0.0, END)
          #self.res.insert(5.5,self.resultatText)

    
    def getMatrice(self):
      self.fint[2].configure(command=self.Determinant)
      self.fint[3].configure(command=self.Inverse)
      self.fint[4].configure(command=self.Transpose)
      # matrice A
      for i in range(self.nombreColonne.get()):
          A.append([])
          for j in range(self.nombreLigne.get()):
            A[i].append([])
      for i in range(self.nombreColonne.get()):
          for j in range(self.nombreLigne.get()):
            A[i][j]=DoubleVar()
      line = 0
      for i in range(self.nombreColonne.get()):
          col=10
          for j in range(self.nombreLigne.get()):
              Entry(self.res, textvariable=A[i][j], width=5).grid(row=line,column=col, padx=2,pady=2)  
              col +=1
          line +=1
      posColAfter= col+15
      return A

    def getDeuxMatrice(self):
      self.fint[0].configure(command=self.Produit)
      self.fint[1].configure(command=self.Somme)
      # matrice A
      for i in range(self.nombreLigne.get()):
          A.append([])
          for j in range(self.nombreColonne.get()):
            A[i].append([])
      for i in range(self.nombreLigne.get()):
          for j in range(self.nombreColonne.get()):
            A[i][j]=DoubleVar()
      line = 0
      for i in range(self.nombreLigne.get()):
          col=10
          for j in range(self.nombreColonne.get()):
              Entry(self.res, textvariable=A[i][j], width=5).grid(row=line,column=col, padx=2,pady=2)  
              col +=1
          line +=1
      posColAfter= col+15
    
      # séparation
      equalSymbol = Canvas(self.res, width=40, height=10*self.nombreLigne.get(),  bd=-2,bg="white")
      equalSymbol.create_text(21, 5*self.nombreLigne.get(), anchor=CENTER, text="-*-*-", font=("arial", 5*self.nombreLigne.get()))
      equalSymbol.grid(row=(posLine1), column=col+5, rowspan=self.nombreLigne.get(),padx=2,pady=2)
  
        # matrice B
      for i in range(self.nombreLigne2.get()):
          B.append([])
          for j in range(self.nombreColonne2.get()):
            B[i].append([])
      for i in range(self.nombreLigne2.get()):
          for j in range(self.nombreColonne2.get()):
            B[i][j]=DoubleVar()
      line2 = 0
      for i in range(self.nombreLigne2.get()):
              col2=50+self.nombreColonne2.get()
              for j in range(self.nombreColonne2.get()):
                    Entry(self.res, textvariable=B[i][j], width=5).grid(row=line2,column=col2, padx=2,pady=2)  
                    col2 +=1
              line2 +=1
      return A,B
      
    def Produit(self):
      print("produit")
      #for w in self.res.winfo_children():
        #w.destroy()
      if self.nombreColonne.get()==self.nombreLigne2.get():
        resultat = list()
        for i in range(self.nombreLigne.get()):
            for j in range(self.nombreColonne.get()):
                A[i][j]= float( (A[i][j]).get() )
                print A[i][j] 
        for i in range(self.nombreLigne2.get()):
            for j in range(self.nombreColonne2.get()):        
                B[i][j]= float( (B[i][j]).get() ) 
                print B[i][j]
        for i in range(self.nombreLigne.get()):
            ligne = list()
            for j in range(self.nombreColonne2.get()):
                element = 0
                for k in range(len(A[0])):
                    element= element+ A[i][k]*B[k][j]
                ligne.append(element)
            resultat.append(ligne)
      #affichage du resultat
        for i in range(self.nombreLigne.get()):
          for j in range(self.nombreColonne2.get()):
            print resultat[i][j]
        Label(self.res, text= "Le résultat du produit est : ",fg="blue",bg="#80c0c0").grid(row=10,column=0)
        line3 = 11
        for i in range(self.nombreLigne.get()):
            col3=1
            for j in range(self.nombreColonne2.get()):
                  Label(self.res, text=resultat[i][j],fg="red",bg="white").grid(row=line3,column=col3,padx=3,pady=3)  
                  col3 +=1
            line3 +=1 
      else:
        resultat="Impossible d'effectuer le produit!"
        print(resultat)
        Label(self.res, text= resultat,fg="red",bg="#80c0c0").grid(row=10,column=4)
      
      return  resultat

    def Somme(self):
      print("Somme")
      #for w in self.res.winfo_children():
        #w.destroy()
      if self.nombreColonne.get()==self.nombreColonne2.get() and self.nombreLigne.get()==self.nombreLigne2.get():
        for i in range(self.nombreLigne.get()):
          for j in range(self.nombreColonne.get()):
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
        for i in range(self.nombreLigne.get()):
          for j in range(self.nombreColonne.get()):
            print resultat[i][j]
        Label(self.res, text= "Le résultat de la somme est : ",fg="blue",bg="#80c0c0").grid(row=10,column=0)
        line3 = 11
        for i in range(self.nombreLigne.get()):
            col3=1
            for j in range(self.nombreColonne.get()):
                  Label(self.res, text=resultat[i][j],fg="red",bg="white").grid(row=line3,column=col3,padx=3,pady=3)  
                  col3 +=1
            line3 +=1 
      else:
        resultat="Impossible d'effectuer la somme de ces deux matrices.Erreur de saisie!"
        print(resultat)
        Label(self.res, text= resultat,fg="red",bg="#80c0c0").grid(row=10,column=4)
      
      return  resultat

    def Determinant(self):
      print("Determinant")

    def Inverse(self):
      print("Inverse")
    

    def Transpose(self):
      print("Transpose")
      self.n, self.p = dimensions(A)
      self.B = creer_matrice(self.p, self.n, None)
      for j in range(self.p) :
        for i in range(self.n) :
          B[j] [i] = A[i] [j]
      print(B)
      return B

#Execution de la fenetre
Graphique()
