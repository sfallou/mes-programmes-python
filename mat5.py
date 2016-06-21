# -*- coding: utf-8 -*-
from Tkinter import *
from time import *
import ToutDIC1
n = 0 # Initialisation de la taille de la matrice (Variable globale )


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


"""Fonction qui calcule les+ coefficients du polynome caracteristique"""				
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
      self.x=0
      for (i, col, rel, txt) in [(0, 'white', RAISED, 'Résolution par Gauss'),
									(1, 'white', RAISED, 'Addition Matrices'),
									(2, 'white', RAISED, 'Produit Matrices'),
									(3, 'white', RAISED, 'Inverse Matrice'),
									(4, 'white', RAISED, 'Transposé Matrice'),
									(5, 'white',RAISED, 'Déterminant Matrice')]:
        self.nom="fonction"+ str(self.x)
        self.fint[i] = Button(self.f1,text=txt, bd=5, relief=rel,  bg =col, width=20, overrelief=RIDGE,command=self.nom)
        self.fint[i].pack(side =TOP, padx =10, pady =5)
        self.x+=1
		
		# Les interfaces des saisies et des affichages a droite
      self.f2 = Frame(self.fen, bg ='cyan', bd =2, relief =GROOVE)
      self.f2.pack(side =RIGHT, padx =5, pady =5)
      self.f2_1=Frame(self.f2, bg ='white', bd =2, relief =GROOVE)
      self.f2_1.grid(row=1,column=1)
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
	  # zone saisie matrice 1
      self.f2_2=Frame(self.f2, bg ='white', bd =2, relief =GROOVE)
      self.f2_2.grid(row=2,column=1)
      Label(self.f2_2,text="Matrice A", bg ='cyan').pack(pady=5)
      self.matrixWindows1 = Frame(self.f2_2, width =350, height =200, bg ='white', bd =2, relief =SOLID)
      self.matrixWindows1.pack()
       # zone saisie matrice 2
      self.f2_3=Frame(self.f2, bg ='white', bd =2, relief =GROOVE)
      self.f2_3.grid(row=3,column=1)
      Label(self.f2_2,text="Matrice B",bg ='cyan').pack(pady=5)
      self.matrixWindows2 = Frame(self.f2_3, width =350, height =200, bg ='white', bd =2, relief =SOLID)
      self.matrixWindows2.pack()
      
	
	 # footer
      self.footer = Frame(self.f2, bg ='white', bd =2, relief =GROOVE)
      self.footer.grid(row=4,column=1)
      footerText = "Zone Résultat"
      self.footerLabel = Label(self.footer, text=footerText, font="arial 10", fg="black", bg="white",
              width=55)
      self.footerLabel.grid(row=0, column=0)
		
      self.fen.mainloop()
       
       
       ##### Les methodes de la classe ###
         
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
            if n!=0 and m==1:
                self.buildMatrix()
                self.ActiveMenu1()
            if n!=0 and m==2:
                self.build2Matrix()
                self.ActiveMenu2()
            else:
                self.footerText = "* Les valeurs saisies ne sont pas correctes"
                color = "red"
        except:
            self.footerText = "* Les valeurs données doivent être des entiers"
            color = "red"
        # affichage message
        self.footerLabel.config(text=self.footerText, fg=color)
    # 
    def ActiveMenu1(self):
		self.fint[0].configure(state=DISABLED)
		self.fint[1].configure(state=DISABLED)
		self.fint[2].configure(state=DISABLED)
		
    
    def ActiveMenu2(self):
		self.fint[0].configure(state=DISABLED)
		self.fint[3].configure(state=DISABLED)
		self.fint[4].configure(state=DISABLED)
		self.fint[5].configure(state=DISABLED) 
	
    def buildMatrix(self):
         # matrice A    
        self.caseA = {}
        for i in range(n*n):
            self.elementMatriceAi = IntVar()
            self.elementMatriceAi.set(0)
            # convert to string because backspace deal with string
            self.caseA[i] = Entry(self.matrixWindows1, textvariable=self.elementMatriceAi, bg ='white', font=("arial", 10), width=3)
            self.caseA[i].grid(row=int(i/n), column=1+i%n)
        # creation des parenthèses  
        bracket1 = Canvas(self.matrixWindows1, bg ='white', width=10*n, height=30*n)
        bracket1.create_text(5*n, 13*n, anchor=CENTER, text="(", font=("Calibri Light", 18*n))
        bracket1.grid(row=0, column=0, rowspan=n)
        #
        bracket2 = Canvas(self.matrixWindows1,bg ='white', width=10*n, height=30*n)
        bracket2.create_text(5*n, 13*n, anchor=CENTER, text=")", font=("Calibri Light", 18*n))
        bracket2.grid(row=0, column=n+1, rowspan=n)
        Button(self.matrixWindows1,text="valider",command=self.getMatriceA).grid(row=n+1,column=n+1)
	    #
    
    def build2Matrix(self):
        # matrice A    
        self.caseA = []
        for i in range(n*n):
            self.elementMatriceAi = IntVar()
            self.elementMatriceAi.set(0)
            # convert to string because backspace deal with string
            self.caseA[i] = Entry(self.matrixWindows1, textvariable=self.elementMatriceAi, bg ='white', font=("arial", 10), width=3)
            self.caseA[i].grid(row=int(i/n), column=1+i%n)
        # creation des parenthèses  
        bracket1 = Canvas(self.matrixWindows1, bg ='white', width=10*n, height=30*n)
        bracket1.create_text(5*n, 13*n, anchor=CENTER, text="(", font=("Calibri Light", 18*n))
        bracket1.grid(row=0, column=0, rowspan=n)
        #
        bracket2 = Canvas(self.matrixWindows1,bg ='white', width=10*n, height=30*n)
        bracket2.create_text(5*n, 13*n, anchor=CENTER, text=")", font=("Calibri Light", 18*n))
        bracket2.grid(row=0, column=n+1, rowspan=n)
        Button(self.matrixWindows1,text="valider",command=self.getMatriceA).grid(row=n+1,column=n+1)
        
        # matrice B    
        self.caseB = []
        for i in range(n*n):
            self.elementMatriceBi = IntVar()
            self.elementMatriceBi.set(0)
            # convert to string because backspace deal with string
            self.caseB[i] = Entry(self.matrixWindows2, textvariable=self.elementMatriceBi, bg ='white', font=("arial", 10), width=3)
            self.caseB[i].grid(row=int(i/n), column=1+i%n)
        # creation des parenthèses  
        bracket1 = Canvas(self.matrixWindows2, bg ='white', width=10*n, height=30*n)
        bracket1.create_text(5*n, 13*n, anchor=CENTER, text="(", font=("Calibri Light", 18*n))
        bracket1.grid(row=0, column=0, rowspan=n)
        #
        bracket2 = Canvas(self.matrixWindows2,bg ='white', width=10*n, height=30*n)
        bracket2.create_text(5*n, 13*n, anchor=CENTER, text=")", font=("Calibri Light", 18*n))
        bracket2.grid(row=0, column=n+1, rowspan=n)
        Button(self.matrixWindows2,text="valider",command=self.getMatriceB).grid(row=n+1,column=n+1)   
        
             
    #
    def getMatriceA(self):
        self.n=n
        self.C=[]
        z=0
        for i in range(n):
            c=[]
            for j in range(n):
                c.append(0)
            self.C.append(c)
            
        for i in range(self.n):
            for j in range(self.n):
                try:
                    self.C[i][j]=int(self.caseA[z].get())
                    z+=1
                except:
                    print("erreur sur la saisi ressayer")
        #print(self.C)
        self.p=ProdMat(self.C,self.C)
        print(self.p)
        self.d=Determinant(self.C)
        print(self.d)
        self.l=PolyCarac(self.C)
        print(self.l)
        
        #return self.C
        
	    #
    def getMatriceB(self):
        self.n=n
        self.C=[]
        z=0
        for i in range(n):
            c=[]
            for j in range(n):
                c.append(0)
            self.C.append(c)
            
        for i in range(self.n):
            for j in range(self.n):
                try:
                    self.C[i][j]=int(self.caseB[z].get())
                    z+=1
                except:
                    print("erreur sur la saisi ressayer")
        print(self.C)
        return self.C
     
    
    def fonction0(self):
		print("okay")
		
    def fonction1(self):
	    print("okay")
	    
    def fonction2(self):
		print("okay")
   
    def fonction3(self):
		print("okay")
        
    def fonction4(self):
		print("okay")
   
    def fonction5(self):	
		print("okay")
		
"""	if 1=1:
chaine = ""
       for x in resul:
       chaine = chaine + str(x) + '\n'
       print(chaine)
	
    def affichage(Mat):
       "Affichage de la matrice"
       chaine = ""
       for x in Mat:
         chaine = chaine + str(x) + '\n'
       print(chaine)

    result=affichage(Matrice)
    self.footerLabel.config(text=result, fg="blue", font="Helvetica 10 bold", justify=LEFT)		
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
            	
		
"""		
#Execution de la fenetre
Graphique()
