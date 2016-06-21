#!/usr/bin/python3

from tkinter import *
fp = Tk()
L1 = Label(fp, text = 'Nom')
E1 = Entry(fp, width=20)
L2 = Label(fp, text = '\nPrénom') #le \n permet de séparer un peu verticalement
E2 = Entry(fp, width=15)
B1 = Button(fp, text='Bouton1', bd=5)
B2 = Button(fp, text='EXIT', bd=5, command=fp.destroy)
E3 = Text(fp, width=20, height=15)
E3.pack(side=RIGHT, fill=BOTH, padx=5, pady=10, expand=1)
L1.pack()
E1.pack()
L2.pack()
E2.pack()
B1.pack(pady=20)
B2.pack(pady=5)
fp.mainloop()

