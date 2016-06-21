# -*- coding: utf-8 -*-
from Tkinter import *
from time import *

n = 0 # Initialisation de la taille de la matrice (Variable globale )

def recherchepivot(k,A):
    i = k
    while i != n and A[i][k] == 0:
        i+=1
    if i != n:
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
            A[i][j] -= r*A[k][j]
            j+=1
        i+=1    
    return A,b

def remonte(A,b):
    x = []
    i = 0
    while i<n:
        x.append(0)
        i+=1        
    x[n-1] = b[n-1]/A[n-1][n-1]
    i = n-2
    while i>=0:    
        x[i] = b[i]            
        j = i+1
        while j<n:
            x[i] -= A[i][j]*x[j]
            j+=1            
        x[i]/=A[i][i]
        i-=1
    return x

# Interface Graphique (classe)
class Graphique:   
    def __init__ (self):
      self.fen=Tk()
      self.fen.title("Calcul Matriciel")
      self.fen.geometry("700x700")
      self.fen.resizable(True, False)
		
		#L'entete
      self.f0 = Frame(self.fen, bg ='#80c0c0', bd =5, relief =RAISED)
      self.f0.pack(side=TOP)
      self.Entete=Label(self.f0,text='Ecole Supérieure Polytechnique de Dakar\nSerigne Fallou Ndiaye DIC1-TR 2015\nPROGRAMME DE CALCUL MATRICIEL', width=100, height=5, bd=5, relief=RAISED, bg='white',font=('Helvetica', 10))
      self.Entete.pack()
      self.f0_1=Frame(self.fen,bg ='green', bd =2, relief =GROOVE)
      self.f0_1.grid(row=1,column=3)
		
		#Menu de gauche
      self.f1 = Frame(self.fen, bg = 'cyan')
      self.f1.pack(side =LEFT, padx =5)
		# on cree les 6 buttons avec une boucle for
      self.fint = [0]*6
      for (i, col, rel, txt) in [(0, 'white', RAISED, 'Résolution par Gauss'),
									(1, 'white', RAISED, 'Addition Matrices'),
									(2, 'white', RAISED, 'Produit Matrices'),
									(3, 'white', RAISED, 'Inverse Matrice'),
									(4, 'white', RAISED, 'Transposé Matrice'),
									(5, 'white',RAISED, 'Déterminant Matrice')]:
        self.fint[i] = Button(self.f1,text=txt, bd=5, relief=rel,  bg =col, width=20, overrelief=RIDGE)
        self.fint[i].pack(side =TOP, padx =10, pady =5)
		
		# L'interface des saisies et des affichages a droite
      self.f2 = Frame(self.fen, bg ='cyan', bd =2, relief =GROOVE)
      self.f2.pack(side =RIGHT, padx =5)
      self.f2_1=Frame(self.f2, bg ='white', bd =2, relief =GROOVE)
      self.f2_1.pack()
      self.nombreMatrice = IntVar()
      self.nombreMatrice.set(1)
      self.lab1=Label(self.f2_1,text="Nombre de Matrice:",bg='white').grid(row=1,column=1)
      self.Entree1=Entry(self.f2_1,width=5,textvariable=self.nombreMatrice,font="arial 13", 
              justify=CENTER).grid(row=1,column=2)
      self.tailleMatrice = IntVar()
      self.tailleMatrice.set(1)
      self.lab2=Label(self.f2_1,text="Taille Matrice:",bg='white').grid(row=1,column=3)
      self.Entree2=Entry(self.f2_1,width=5,textvariable=self.tailleMatrice,font="arial 13", 
              justify=CENTER).grid(row=1,column=4)
      self.butt1=Button(self.f2_1, text='OK',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE,command=self.matrixLen).grid(row=1,column=5,padx=4)
   
		
	# zone saisie matrice
      self.matrixWindows = Frame(self.f2, width =450, height =450, bg ='white', bd =2, relief =SOLID)
      self.matrixWindows.pack()
      self.selectedCase = ""
	
	 # footer
      self.footer = Frame(self.f2)
      self.footer.pack(padx=8, pady=8)
      footerText = "Résolution d'un sytème d'équations linéaires"
      self.footerLabel = Label(self.footer, text=footerText, font="arial 10", fg="black", bg="white",
              width=55)
      self.footerLabel.grid(row=0, column=0)
		
      self.fen.mainloop()
       
       
       ##### Les methodes de la classe
         
    def matrixLen(self):
        self.footerText = " Entrer les éléments de la Matrice"
        color = "blue"
        try:
            global n,m
            n = int(self.tailleMatrice.get())
            m = int(self.nombreMatrice.get())
            if n == 0 or m==0:
                self.footerText = "* Veuillez donner des valeurs non nulles"
                color = "red"
            else:
                if m==1:
                    self.buildMatrix()
                    self.ActiveMenu1()
                elif m==2:
                    self.build2Matrix()
                    self.ActiveMenu2()
                else:
                   self.footerText = "* Le nombre de matrice ne doit pas dépasser 2"
                   color = "red"
        except:
            self.footerText = "* Les valeurs données doivent être des entiers"
            color = "red"
        # affichage message
        self.footerLabel.config(text=self.footerText, fg=color)
    # 
    def ActiveMenu1(self):
		self.fint[1].configure(state=DISABLED)
		self.fint[2].configure(state=DISABLED)
		
    
    def ActiveMenu2(self):
		self.fint[0].configure(state=DISABLED)
		self.fint[3].configure(state=DISABLED)
		self.fint[4].configure(state=DISABLED)
		self.fint[5].configure(state=DISABLED) 
	
    def build2Matrix(self):
        self.footerLabel.config(text="it's work!", fg=color)
			
    
    def buildMatrix(self):
        # matrice A     
        self.caseA = {}
        for i in range(n*n):
            self.elementMatriceAi = IntVar()
            self.elementMatriceAi.set(0)
            # convert to string because backspace deal with string
            self.caseA[i] = Entry(self.matrixWindows, textvariable=self.elementMatriceAi, bg ='white', font=("arial", 10), width=3)
            self.caseA[i].grid(row=int(i/n), column=1+i%n)
        # creation des parenthèses  
        bracket1 = Canvas(self.matrixWindows, bg ='white', width=10*n, height=30*n)
        bracket1.create_text(5*n, 13*n, anchor=CENTER, text="(", font=("Calibri Light", 18*n))
        bracket1.grid(row=0, column=0, rowspan=n)
        #
        bracket2 = Canvas(self.matrixWindows,bg ='white', width=10*n, height=30*n)
        bracket2.create_text(5*n, 13*n, anchor=CENTER, text=")", font=("Calibri Light", 18*n))
        bracket2.grid(row=0, column=n+1, rowspan=n)        
        #
        bracket3 = Canvas(self.matrixWindows,bg ='white', width=10*n, height=30*n)
        bracket3.create_text(5*n, 13*n, anchor=CENTER, text="(", font=("Calibri Light", 18*n))
        bracket3.grid(row=0, column=n+2, rowspan=n)
        # inconnues xi
        caseX = {}
        for i in range(n):
            caseX[i] = Label(self.matrixWindows, text="x{}".format(i+1),bg ='white', font=("arial", 10), width=3)
            caseX[i].grid(row=i, column=n+3)
        #
        bracket4 = Canvas(self.matrixWindows,bg ='white', width=10*n, height=30*n)
        bracket4.create_text(5*n, 13*n, anchor=CENTER, text=")", font=("Calibri Light", 18*n))
        bracket4.grid(row=0, column=n+4, rowspan=n)
        # signe égalité
        equalSymbol = Canvas(self.matrixWindows, bg ='white', width=20, height=30*n)
        equalSymbol.create_text(21, 15*n, anchor=CENTER, text="=", font=("arial", 18*n))
        equalSymbol.grid(row=0, column=n+5, rowspan=n)
        #
        bracket5 = Canvas(self.matrixWindows, bg ='white', width=10*n, height=30*n)
        bracket5.grid(row=0, column=n+6, rowspan=n)
        bracket5.create_text(5*n, 13*n, anchor=CENTER, text="(", font=("Calibri Light", 18*n))
        # vecteur b
        self.caseB = {}
        for i in range(n):
            self.elementMatriceBi = IntVar()
            self.elementMatriceBi.set(0)
            self.caseB[i] = Entry(self.matrixWindows, bg ='white', textvariable=self.elementMatriceBi, font=("arial", 10), width=3)
            self.caseB[i].grid(row=i, column=n+7)
        #
        bracket6 = Canvas(self.matrixWindows, bg ='white', width=10*n, height=30*n)
        bracket6.create_text(5*n, 13*n, anchor=CENTER, text=")", font=("Calibri Light", 18*n))
        bracket6.grid(row=0, column=n+8, rowspan=n)
        # solve button
        Button(self.footer, text="Résoudre", height=2, bg="royal blue", fg="white",
               font=("Arial", 10, "bold"), command=self.solveEquation).grid(row=0, column=1)
    #
    def solveEquation(self):
        # eval matrix elements
        A = []
        b = []
        for i in range(n):
            error = "ERREURS !"  
            # adding vector b elem
            try:            
                if self.caseB[i]["textvariable"] != "":
                    error += "\n * Remplissez les cases par des nombres"     
                    self.footerLabel.config(text=error, fg="red", font="arial 10")                    
                    return 0  # stopping programm
                b.append(eval(int(self.caseB[i]["textvariable"])))
            except:
                error += "\n * Tous les éléments de la matrice doivent être des nombres" 
                self.footerLabel.config(text=error, fg="red", font="arial 10")                
                return 0  # stopping programm
            # adding matrix A elem   
            A.append([])
            for j in range(n):
                try:
                    if self.caseA[i*n+j]["textvariable"] != "":
                        error += "\n * Remplissez les cases par des nombres"     
                        self.footerLabel.config(text=error, fg="red", font="arial 10")                    
                        return 0  # stopping programm
                    A[i].append(eval(int(self.caseA[i*n+j]["textvariable"])))
                except:
                    error += "\n * Tous les éléments de la matrice doivent être des nombres"
                    self.footerLabel.config(text=error, fg="red", font="arial 10")                  
                    return 0  # stopping programm	
	
	if 1 == 1:
            tps1 = time()
            # solve equation by GAUSS method
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
                result = "Ce système admet pour solution :"
                for i in range(n):
                    result += "\n x{} = {}".format(i+1, x[i])          
            else:
                # no unique solution
                result = "Ce système n'admet pas de solution unique"
            # Showing results
            tps2 = time()
            t =0
            t = tps2 - tps1
            result += "\ntemps d'execution: "
            result +=str(t)
            self.footerLabel.config(text=result, fg="blue", font="Helvetica 10 bold", justify=LEFT)
            	
		
		
		
#Execution de la fenetre
Graphique()
