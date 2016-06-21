#!/usr/bin/python3

from tkinter import *

n=int(input("Donner le nombre de Ligne de la matrice:"))
m=int(input("Donner le nombre de Colonne de la matrice:"))
if n and m:
	fp = Tk()
	fp.geometry('600x600+100+100')
	fp.title("Matrice")
	L1=Label(fp,text="Résultat")
	fram = Frame(fp, bg='black', bd=5,relief = RIDGE)
	for i in range(n):
		for j in range(n):
			matri=l[i*n+j]
			Eij = Entry(fram, width=5,textvariable=str(matri))
			Eij.grid(row=i,column=j)
	L1.pack()
	fram.pack(pady=20)
	fp.mainloop()

