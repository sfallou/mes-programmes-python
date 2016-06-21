from Tkinter import *
from gauss import *



def fenLU():
	frameLU = Frame (panel)
	frameLU.pack()
	Label(frameLU, text= "vous etes la mais LU n'y est pas").pack()

#Creation de la fenetre principale
fenetre = Tk()
fenetre.title("Accueil")
panel=PanedWindow(orient=HORIZONTAL)
panel.pack(expand='yes', fill='both')

frameDescription=Frame(panel)
frameDescription.pack()
Label(frameDescription, text="ce programme vous permet de \n "
			     "Resoudre une equation de la forme\n"
			     "Ax = b par les methodes suivants:   ").pack()

frameChoixOp = Frame(panel)
frameChoixOp.pack()
Label(frameChoixOp, text="Faites un choix", fg="red").pack()
#entree=Entry(frameChoixOp)
#entree.pack()
Button(frameChoixOp, text="LU",command=fenLU).pack()
Button(frameChoixOp, text="LRU",command=fenLU).pack()
Button(frameChoixOp, text="Cholesky",command=fenLU).pack()

frameResult = Frame(panel).pack()

fenetre.mainloop()
