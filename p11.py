# -*- coding: utf-8 -*-
from Tkinter import *
from time import *
	
A = list()
B = list()
n1=4 #nombre de colonne matrice 1
n2=2 #nombre de colonne matrice 2
m1=2 #nombre de ligne matrice 1
m2=3 #nombre de ligne matrice 2

line = 0
line2 = 0
posLine1 = 0 
posLine2= line
	
##### Les methodes ###    
     

def getMatrice():
	
    # matrice A
	for i in range(n1):
		A.append([])
		for j in range(m1):
			A[i].append([])
	for i in range(n1):
		for j in range(m1):
			A[i][j]=IntVar()
	line = 0
    	for i in range(n1):
        	col=10
        	for j in range(m1):
            		Entry(matrixWindows1, textvariable=A[i][j], width=5).grid(row=line,column=col, padx=2,pady=2)  
            		col +=1
        	line +=1
    	posColAfter= col+15
    
	# séparation
	equalSymbol = Canvas(matrixWindows1, width=40, height=30*m1,  bd=-2,bg="white")
	equalSymbol.create_text(21, 15*m1, anchor=CENTER, text="-*-*-", font=("arial", 8*m1))
	equalSymbol.grid(row=(posLine1), column=col+5, rowspan=m1)
	
    # matrice B
	for i in range(n2):
		B.append([])
		for j in range(m2):
			B[i].append([])
	for i in range(n2):
		for j in range(m2):
			B[i][j]=IntVar()
	line2 = 0
    	for i in range(n2):
        	col2=50+m2
        	for j in range(m2):
            		Entry(matrixWindows1, textvariable=B[i][j], width=5).grid(row=line2,column=col2, padx=2,pady=2)  
            		col2 +=1
        	line2 +=1
	return A,B	

def affiche():
	print(float( (A[0][0]).get() ))
	print(float( (A[0][0]).get() ))


def traitement():
	getMatrice()


# Interface Graphique 
fen=Tk()
fen.title("Calcul Matriciel")
fen.geometry("700x700")
fen.resizable(True, False)

		
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
butt1=Button( f2, text='Get',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE,command=affiche).grid(row=5,column=2,padx=4)

      

#Execution de la fenetre
fen.mainloop()