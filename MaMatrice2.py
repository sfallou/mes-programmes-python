# -*- coding: utf-8 -*-
from Tkinter import *
from time import *

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
    
def gauss():
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
	footerLabel.config(text=result, fg="blue", font="Helvetica 10 bold", justify=LEFT)
            	
	
A = list()
B = list()
D = list()
E = list()

line = 0
line2 = 0
posLine1 = 0 
posLine2= line
	
##### Les methodes ###    
     

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
	
	return A	
     
     
def getVecteur():
	# parenthèse 1
	bracket1 = Canvas(matrixWindows2, width=10*n.get(), height=30*n.get(),  bd=2,bg="white")
	bracket1.create_text(5*n.get(), 13*n.get(), anchor=CENTER, text="(",font=("Calibri Light", 24*n.get()))
	bracket1.grid(row=posLine1, column=0, rowspan=n.get())   
    # matrice
	for i in range(n.get()):
		B.append([])
		for j in range(n.get()):
			B[i].append([])
	for i in range(n.get()):
		for j in range(n.get()):
			B[i][j]=IntVar()
	line = 0
    	for i in range(n.get()):
        	col=10
        	for j in range(n.get()):
            		Entry(matrixWindows2, textvariable=B[i][j], width=5).grid(row=line,column=col, padx=2,pady=2)  
            		col +=1
        	line +=1
    	posColAfter= col+15
    # parenthèse 2
	bracket2 = Canvas(matrixWindows2, width=10*n.get(), height=30*n.get(), bd=2,bg="white")
	bracket2.create_text(5*n.get(), 13*n.get(), anchor=CENTER, text=")",font=("Calibri Light", 24*n.get()))
	bracket2.grid(row=posLine1, column=col+1, rowspan=n.get())
	
	return B	
       
     
    
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
f0_1.pack()

#Image
FenImage = Frame(f0_1)
FenImage.grid(row = 0, column = 3)   
image = PhotoImage(file ="me.gif")
canIm = Canvas(FenImage, height = "90", width = "90", bg= "green")
canIm.create_image(0, 0, anchor = CENTER, image = image)
canIm.grid(row = 0, column = 0, padx = 5, pady = 5)


		
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
