# -*- coding: utf-8 -*-
from Tkinter import *
from time import *
import tkMessageBox
	
A = list()
B = list()
D = list()
E = list()

line = 0
line2 = 0
posLine1 = 0 
posLine2= line
	
##### Les methodes ###    
"""Fonction qui cree une matrice carre et linitialise a la matrice nulle"""
def CreeMatCar(n):
	return [ [0.0 for j in range(0,n)] for i in range(0,n) ]

"""Fonction qui cree une matrice identite"""
def CreeMatId(n):
	I=CreeMatCar(n)
	for i in range(0,n):
		I[i][i]=1.0
	return I
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


def getMatrice():
	# parenthèse 1
	bracket1 = Canvas(matrixWindows1, width=10*n.get(), height=30*n.get(),  bd=2,bg="white")
	bracket1.create_text(5*n.get(), 13*n.get(), anchor=CENTER, text="(",font=("Calibri Light", 24*n.get()))
	bracket1.grid(row=posLine1, column=0, rowspan=n.get())   
    # matrice
	for i in range(n.get()):
		A.append([])
		for j in range(n.get()):
			A[i].append([])
	for i in range(n.get()):
		for j in range(n.get()):
			A[i][j]=IntVar()
	line = 0
    	for i in range(n.get()):
        	col=10
        	for j in range(n.get()):
            		Entry(matrixWindows1, textvariable=A[i][j], width=5).grid(row=line,column=col, padx=2,pady=2)  
            		col +=1
        	line +=1
    	posColAfter= col+15
    # parenthèse 2
	bracket2 = Canvas(matrixWindows1, width=10*n.get(), height=30*n.get(), bd=2,bg="white")
	bracket2.create_text(5*n.get(), 13*n.get(), anchor=CENTER, text=")",font=("Calibri Light", 24*n.get()))
	bracket2.grid(row=posLine1, column=col+1, rowspan=n.get())
	# signe égalite
	equalSymbol = Canvas(matrixWindows1, width=40, height=30*n.get(),  bd=-2,bg="white")
	equalSymbol.create_text(21, 15*n.get(), anchor=CENTER, text="-*-", font=("arial", 8*n.get()))
	equalSymbol.grid(row=(posLine1), column=col+5, rowspan=n.get())
	# parenthèse 5
	bracket3 = Canvas(matrixWindows1, width=10*n.get(), height=30*n.get(), bd=2,bg="white")
	bracket3.create_text(5*n.get(), 13*n.get(), anchor=CENTER, text="(",font=("Calibri Light", 24*n.get()))
	bracket3.grid(row=posLine1, column=posColAfter, rowspan=n.get())
	posColAfter2= posColAfter+1
    # matrice
	for i in range(n.get()):
		B.append([])
		for j in range(n.get()):
			B[i].append([])
	for i in range(n.get()):
		for j in range(n.get()):
			B[i][j]=IntVar()
	line2 = 0
    	for i in range(n.get()):
        	col2=50+n.get()
        	for j in range(n.get()):
            		Entry(matrixWindows1, textvariable=B[i][j], width=5).grid(row=line2,column=col2, padx=2,pady=2)  
            		col2 +=1
        	line2 +=1
    # Parenthèse 6
	bracket2 = Canvas(matrixWindows1, width=10*n.get(), height=30*n.get(), bd=2,bg="white")
	bracket2.create_text(5*n.get(), 13*n.get(), anchor=CENTER, text=")",font=("Calibri Light", 24*n.get()))
	bracket2.grid(row=posLine1, column=col2+2, rowspan=n.get())
	
	return A,B	
     
def somme():
	for i in range(n.get()):
		for j in range(n.get()):
			A[i][j]= float( (A[i][j]).get() ) 
			B[i][j]= float( (B[i][j]).get() ) 
			print A[i][j],B[i][j]
		resultat = list()
    	for i in range(len(A)):
      		colonne = list()
        	for j in range(len(B)):
            		colonne.append(A[i][j]+B[i][j])
        	resultat.append(colonne)
	for i in range(n.get()):
        	for j in range(n.get()):
			print resultat[i][j]
	Label(matrixWindows2, text= "Le résultat est : ",fg="royal blue",bg="white").grid(row=10,column=0)
	line3 = 11
    	for i in range(n.get()):
        	col3=1
        	for j in range(n.get()):
            		Label(matrixWindows2, text=resultat[i][j],fg="royal blue",bg="white" ).grid(row=line3,column=col3)  
            		col3 +=1
        	line3 +=1	
    	return  resultat

def multiplcation():
    resultat = list()
    for i in range(n.get()):
        for j in range(n.get()):
	        A[i][j]= float( (A[i][j]).get() ) 
		B[i][j]= float( (B[i][j]).get() ) 
		print A[i][j],B[i][j]
    for i in range(len(A)):
        ligne = list()
        for j in range(len(B[0])):
            element = 0
            for k in range(len(A[0])):
                element= element+ A[i][k]*B[k][j]
            ligne.append(element)
        resultat.append(ligne)
    
    for i in range(n.get()):
        for j in range(n.get()):
		print resultat[i][j]
	Label(matrixWindows2, text= "Le résultat est : ",fg="royal blue",bg="white").grid(row=10,column=0)

	line3 = 11
    	for i in range(n.get()):
        	col3=1
        	for j in range(n.get()):
            		Label(matrixWindows2, text=resultat[i][j],fg="royal blue",bg="white" ).grid(row=line3,column=col3)  
            		col3 +=1
        	line3 +=1
    

    return resultat 
    
def determinant():
	A,B=getMatrice()
	#detA=Determinant(A)
	#detB=Determinant(B)
	Label(matrixWindows2, text=A,fg="royal blue",bg="white" ).grid(row=1,column=1)
	Label(matrixWindows2, text=B,fg="royal blue",bg="white" ).grid(row=2,column=1)
def polynome():
	 j=0   

def traitement():
	footerText = " Entrer les éléments de la Matrice"
	color = "blue"
	try:
		global n1
		n1 = int(n.get())
		
		if n.get() == 0 :
			footerText = "* Veuillez donner des valeurs non nulles"
		
		else :
			getMatrice()
	except:
		footerText = "* Les valeurs données doivent être des entiers"
		color = "red"
		# affichage message
		footerLabel.config(text= footerText, fg=color)
   
     
		


# Interface Graphique 
fen=Tk()
fen.title("Calcul Matriciel")
fen.geometry("700x700")
fen.resizable(True, False)

#L'entete
f0 = Frame( fen, bg ='#80c0c0', bd =5, relief =RAISED)
f0.pack(side=TOP)
Entete=Label( f0,text='Ecole Supérieure Polytechnique de Dakar\nSerigne Fallou Ndiaye DIC1-TR 2015\nPROGRAMME DE CALCUL MATRICIEL', width=100, height=5, bd=5, relief=RAISED, bg='white',font=('Helvetica', 10))
Entete.pack()
f0_1=Frame( fen,bg ='green', bd =2, relief =GROOVE)
f0_1.grid(row=1,column=3)

#Menu de gauche
f1 = Frame( fen, bg = 'cyan')
f1.pack(side =LEFT, padx =5)

Menu1 = Button( f1,text='Addition Matrices', bd=5, relief=RAISED,  bg ='white', width=20, overrelief=RIDGE,command=somme)
Menu1.pack(side =TOP, padx =10, pady =5)
Menu2 = Button( f1,text='Produit Matrices', bd=5, relief=RAISED,  bg ='white', width=20, overrelief=RIDGE,command=multiplcation)
Menu2.pack(side =TOP, padx =10, pady =5)
Menu3 = Button( f1,text='Determinant  Matrices', bd=5, relief=RAISED,  bg ='white', width=20, overrelief=RIDGE,command=determinant)
Menu3.pack(side =TOP, padx =10, pady =5)
Menu4 = Button( f1,text='Polynome Caracteristique', bd=5, relief=RAISED,  bg ='white', width=20, overrelief=RIDGE,command=polynome)
Menu4.pack(side =TOP, padx =10, pady =5)
   
		
# Les interfaces des saisies et des affichages a droite
f2 = Frame( fen, bg ='cyan', bd =2, relief =GROOVE)
f2.pack(side =RIGHT, padx =5, pady =5)
f2_1=Frame( f2, bg ='white', bd =2, relief =GROOVE)
f2_1.grid(row=1,column=1)
n = IntVar()
n.set(" ")
lab2=Label(f2_1,text="Taille Matrice:",bg='white').grid(row=1,column=3)
Entree2=Entry(f2_1,width=5,textvariable=n,font="arial 13",justify=CENTER).grid(row=1,column=4)
butt1=Button( f2_1, text='OK',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE,command=traitement).grid(row=1,column=5,padx=4)
# zone saisie matrice 1
f2_2=Frame( f2, bg ='white', bd =2, relief =GROOVE)
f2_2.grid(row=2,column=1)
matrixWindows1 = Frame( f2_2, width =550, height =200, bg ='white', bd =2, relief =SOLID)
matrixWindows1.pack()
# zone saisie matrice 2
f2_3=Frame( f2, bg ='white', bd =2, relief =GROOVE)
f2_3.grid(row=3,column=1)
matrixWindows2 = Frame( f2_3, width =350, height =200, bg ='white', bd =2, relief =SOLID)
matrixWindows2.pack()
      
# footer
footer = Frame( f2, bg ='white', bd =2, relief =GROOVE)
footer.grid(row=4,column=1)
footerText = "Zone Résultat"
footerLabel = Label( footer, text=footerText, font="arial 10", fg="black", bg="white",width=55)
footerLabel.grid(row=0, column=0)
      

#Execution de la fenetre
fen.mainloop()
