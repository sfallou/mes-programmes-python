# -*-coding:Utf-8 -*
from tkinter import *
from Bibliotheque import *


class BibiothequeGraphique(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Gestion Bibliotheque')
        self.geometry("1150x650")
        self.resizable(True, True)
    #L'entete
        self.entete = Frame(self, bg ='#80c0c0', bd =5, relief =RAISED)
        self.entete.pack(side=TOP)
        self.textEntete=Label(self.entete,text='Ecole Centrale de Lyon\nBE2 Informatique TC2\nGestion Bibliothèque\nECL 2015-2016', width=100, height=5, bd=5, relief=RAISED, bg='white',font=('Helvetica', 12))
        self.textEntete.grid(row =1, column =1, columnspan =3, padx =10, pady =5)    

    #Body
        self.body= Frame(self, bg ='#80c0c0', bd =5, relief =RAISED)
        self.body.pack(pady=10)
        #fenetre de gauche
        self.fg = Frame(self.body, bg = 'royal blue' ,width=100, height=5, bd=5,)
        self.fg.grid(row=1, column=1, padx =5)
        # Widgets de la fenetre de gauche
        self.contain_g=Frame(self.fg, borderwidth=1,bg ='#80c0c0',width="100")
        self.contain_g.pack(padx=5,pady=5,expand="yes",fill="both")
        self.contain_form=Frame(self.contain_g, borderwidth=1,bg ='#80c0c0')
        self.contain_form.grid(pady=5, row=0,column=0)
        self.labelContain_form=LabelFrame(self.contain_form,text="Bienvenue",font="arial 12 bold italic",labelanchor = N,bg='white')
        self.labelContain_form.pack(padx=3, pady=5, expand="yes")
        self.labelCreer=Label(self.labelContain_form,text="Créer une nouvelle Bibliothèque:", font="arial 12 bold",bg='white')
        self.labelCreer.grid(padx=5, pady=10, row=0 ,column=0)
        self.labelSelect=Label(self.labelContain_form,text="Selectionner une Bibliothèque:", font="arial 12 bold",bg='white')
        self.labelSelect.grid(padx=5, pady=10, row=1 ,column=0)
        self.creer=Button(self.labelContain_form,text='Créer',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE, command=self.creerBiblio)
        self.creer.grid(padx=5, pady=20, row=0 ,column=1)
        self.selection=Button(self.labelContain_form,text='Selectionner',bd=2, relief=RAISED,  bg ='royal blue', width=10, overrelief=RIDGE )
        self.selection.grid(padx=5, pady=20, row=1 ,column=1)
        self.b1=Button(self.contain_g,text='Quitter',bd=2, relief=RAISED, width=3, overrelief=RIDGE,fg="red",command=self.destroy)
        self.b1.grid(padx=5,pady=20,row=4,column=0)


    def creerBiblio(self):
        self.creer.configure(state='disabled')
        self.selection.configure(state='disabled')
        # L'interface des saisies et des affichages a droite
        self.fd = Frame(self.body, bg = 'royal blue', bd =2, relief =GROOVE)
        self.fd.grid(row=1, column=2, padx =5)
        self.contain_d=Frame(self.fd, borderwidth=1,bg ='#80c0c0')
        self.contain_d.pack(padx=5,pady=5,expand="yes",fill="both")
        self.contain_results=Frame(self.contain_d, borderwidth=1,bg ='#80c0c0')
        self.contain_results.grid(pady=5, row=0,column=1)
        self.label_containResults=LabelFrame(self.contain_results,text="Création d'une nouvelle Bibliotheque",font="arial 12 bold italic",labelanchor = N,bg='white')
        self.label_containResults.pack(padx=5, pady=5, expand="yes")
        self.labelNomBiblio=Label(self.label_containResults,text="Nom de la Bibliotheque:", font="arial 12 bold",bg='white')
        self.labelNomBiblio.grid(padx=5, pady=20, row=0 ,column=0)
        self.nomBiblio=Entry(self.label_containResults,font="arial 15 ", width=20)
        self.nomBiblio.grid(padx=5,row=0 ,column=1)
        self.valider=Button(self.label_containResults,text='Valider',bd=2, relief=RAISED, width=3, overrelief=RIDGE,fg="red",command=self.creationBiblio)
        self.valider.grid(row=0 ,column=2)

    def creationBiblio(self):
        self.creer.configure(command=self.destroy)
        if self.nomBiblio.get():
            self.B=Bibliotheque(self.nomBiblio.get())
            self.labelNomBiblio.destroy()
            self.nomBiblio.destroy()
            self.valider.destroy()
            print(self.B)
            self.infoBiblio=StringVar()
            self.infoBiblio.set(str(self.B))
            Label(self.label_containResults,textvariable=self.infoBiblio, font="arial 12 bold",bg='white').pack(padx=5, pady=20)
        
if __name__ == '__main__':
    Biblio=BibiothequeGraphique()
    Biblio.mainloop()
