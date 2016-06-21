#/usr/bin/python2.7
#-*-coding: utf-8-*-

from Tkinter import *
from math import *
import tkMessageBox

A = list()
B = list()
D = list()
E = list()

line = 0
line2 = 0
posLine1 = 0 
posLine2= line



def saisir_matrice():
 	
	
    # parenthèse 1
    	bracket1 = Canvas(fram, width=10*n.get(), height=30*n.get(),  bd=-2,bg="white")
    	bracket1.create_text(5*n.get(), 13*n.get(), anchor=CENTER, text="(",
                         font=("Calibri Light", 24*n.get()))
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
            		Entry(fram, textvariable=A[i][j], width=5).grid(row=line,column=col, padx=10,pady=10)  
            		col +=1
        	line +=1
	
    	posColAfter= col+15


	

   	 # parenthèse 2
    	bracket2 = Canvas(fram, width=10*n.get(), height=30*n.get(), bd=-2,bg="white")
    	bracket2.create_text(5*n.get(), 13*n.get(), anchor=CENTER, text=")",
                         font=("Calibri Light", 24*n.get()))
    	bracket2.grid(row=posLine1, column=col+1, rowspan=n.get())


    	# signe égalite
	equalSymbol = Canvas(fram, width=40, height=30*n.get(),  bd=-2,bg="white")
    	equalSymbol.create_text(21, 15*n.get(), anchor=CENTER, text="*", font=("arial", 8*n.get()))
    	equalSymbol.grid(row=(posLine1), column=col+5, rowspan=n.get())
	

    	# parenthèse 5
    	bracket3 = Canvas(fram, width=10*n.get(), height=30*n.get(), bd=-2,bg="white")
    	bracket3.create_text(5*n.get(), 13*n.get(), anchor=CENTER, text="(",
                         font=("Calibri Light", 24*n.get()))
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
            		Entry(fram, textvariable=B[i][j], width=5).grid(row=line2,column=col2, padx=10,pady=10)  
            		col2 +=1
        	line2 +=1
	
    	


    	# Parenthèse 6
    	bracket2 = Canvas(fram, width=10*n.get(), height=30*n.get(), bd=-2,bg="white")
    	bracket2.create_text(5*n.get(), 13*n.get(), anchor=CENTER, text=")",font=("Calibri Light", 24*n.get()))
    	bracket2.grid(row=posLine1, column=col2+2, rowspan=n.get())
	
	return A,B	
#---------------------------------------------------------------------------------------------------------------------------


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
	Label(fen, text= "Le résultat est : ",fg="blue",bg="white").grid(row=10,column=0)

	line3 = 11
    	for i in range(n.get()):
        	col3=1
        	for j in range(n.get()):
            		Label(fen, text=resultat[i][j],fg="blue",bg="white" ).grid(row=line3,column=col3)  
            		col3 +=1
        	line3 +=1	

    	return  resultat

def multiplier():
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
	Label(fen, text= "Le résultat est : ",fg="blue",bg="white").grid(row=10,column=0)

	line3 = 11
    	for i in range(n.get()):
        	col3=1
        	for j in range(n.get()):
            		Label(fen, text=resultat[i][j],fg="blue",bg="white" ).grid(row=line3,column=col3)  
            		col3 +=1
        	line3 +=1

    return resultat 

def ordre():
	try:
            global n1
            n1 = int(n.get())
            if n.get() == 0:
		tkMessageBox.showinfo('ordre',"La taille de la matrice doit est être non nulle")
    
            else:
                saisir_matrice()
        except:
	
	    tkMessageBox.showinfo('ordre',"La taille de la matrice doit être un entier")

fenetre=Tk()
fenetre.title("Opération sur les matrices")
fenetre.geometry("580x250")
fen = Frame(fenetre,bd=5,bg="royalblue")
fram= LabelFrame(fen,bg="white", font=('times', 10, 'bold italic'))
fram.grid(row=2, column=0, padx=5, pady=3, sticky=W, columnspan=10)


n = IntVar()
n.set(" ")

menuder = Menu(fenetre,fg="royalblue")
filemenu = Menu(menuder,tearoff=0)
filemenu.add_command(label="Somme")
filemenu.add_command(label="Produit")
filemenu.add_command(label="Inverse")
filemenu.add_separator()
filemenu.add_command(label="Quitter", command=fenetre.destroy)
menuder.add_cascade(label="Operation", menu=filemenu)


aide = Menu(menuder,tearoff=0)
aide.add_command(label="Aide..." )
aide.add_command(label="A propos")
menuder.add_cascade(label="Aide", menu=aide)

fenetre.config(menu=menuder)

Label(fen, text= "Entrer l'ordre de la matrice",fg="blue",bg="white").grid(row=20,column=0)
Entry(fen, textvariable=n,fg="blue").grid(row=20,column=1)
Button(fen, text='Entrer', command=ordre,bg="white",fg="blue").grid(row=20,column=3)

Button(fen, text='Somme',command=somme,bg="white",fg="blue").grid(row=0,column=0)
Button(fen, text='Produit',command=multiplier,bg="white",fg="blue").grid(row=0,column=1)
Button(fen, text='Inverse',bg="white",fg="blue").grid(row=0,column=3)
Button(fen, text='Quitter', command=fen.quit,bg="white",fg="blue").grid(row=20,column=4)

fen.pack()
fen.mainloop()
