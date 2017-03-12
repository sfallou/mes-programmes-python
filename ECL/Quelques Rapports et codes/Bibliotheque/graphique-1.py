# -*-coding:Utf-8 -*
from tkinter import *
from tkinter.messagebox import *
from Bibliotheque import *


class BibiothequeGraphique(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Gestion Bibliotheque')
        self.geometry("1150x750")
        self.resizable(True, True)
        self.__B=None # on crée une variable initialisé à None qui va etre l'objet bibliotheque par la suite
        # on crée l'ensemble des toplevels qu'on va utiliser dans le programme
        self.fenetre2 = Toplevel(self,bg ='#80c0c0', bd =5, relief =RAISED)
        self.fenetre2.geometry('400x400+100+250')
        self.fenetre3 = Toplevel(self,bg ='#80c0c0', bd =5, relief =RAISED)
        self.fenetre3.geometry('400x400+100+250')
        self.fenetre4 = Toplevel(self,bg ='#80c0c0', bd =5, relief =RAISED)
        self.fenetre4.geometry('400x400+100+250')
        self.fenetre5 = Toplevel(self,bg ='#80c0c0', bd =5, relief =RAISED)
        self.fenetre5.geometry('400x400+100+250')
        #on les caches jusqu'au moment oû on fera à eux
        self.fenetre2.withdraw()
        self.fenetre3.withdraw()
        self.fenetre4.withdraw()
        self.fenetre5.withdraw()


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
        self.contain_form.grid(pady=1, row=0,column=0)
        self.labelContain_form=LabelFrame(self.contain_form,text="Bienvenue",font="arial 12 bold italic",labelanchor = N,bg='white')
        self.labelContain_form.pack(padx=3, pady=5, expand="yes")
        self.labelCreer=Label(self.labelContain_form,text="Créer une nouvelle Bibliothèque:", font="arial 12 bold",bg='white')
        self.labelCreer.grid(padx=5, pady=10, row=0 ,column=0)
        self.creer=Button(self.labelContain_form,text='Créer',bd=2, relief=RAISED,  bg ='royal blue', overrelief=RIDGE, command=self.creerBiblio)
        self.creer.grid(padx=5, pady=20, row=0 ,column=1)
        self.b1=Button(self.contain_g,text='Quitter',bd=2, relief=RAISED,  overrelief=RIDGE,fg="red",command=self.destroy)
        self.b1.grid(padx=5,pady=0,row=4,column=0)

        
    def creerBiblio(self):
       	self.creer.configure(state='disabled')
       	#L'interface des saisies et des affichages a droite
       	self.fd = Frame(self.body, bg = 'royal blue',bd=2,relief=GROOVE)
       	self.fd.grid(row=1, column=2, padx =5)
       	self.contain_d=Frame(self.fd, borderwidth=1,bg ='#80c0c0')
       	self.contain_d.pack(padx=5,pady=5,expand="yes",fill="both")
       	self.contain_results=Frame(self.contain_d, borderwidth=1,bg ='#80c0c0')
       	self.contain_results.grid(pady=5, row=0,column=1)
        #on affichera une image dans la page principale pour rendre faire jolie
        self.image = PhotoImage(file ="logo2.png")
        self.canIm = Canvas(self.contain_results, height = "310", width = "300")
        self.canIm.create_image(160, 160, image =  self.image)
        self.canIm.pack(padx=5, pady=1, expand="yes")

        # l'autre partie de la page principale qui affiche du texte
       	self.label_containResults=LabelFrame(self.contain_results,text="Création d'une nouvelle Bibliotheque",font="arial 12 bold italic",labelanchor = N,bg='white')
       	self.label_containResults.pack(padx=5, pady=5, expand="yes")
       	self.labelNomBiblio=Label(self.label_containResults,text="Nom de la Bibliotheque:", font="arial 12 bold",bg='white')
       	self.labelNomBiblio.grid(padx=5, pady=20, row=0 ,column=0)
       	self.nomBiblio=Entry(self.label_containResults,font="arial 15 ", width=20)
       	self.nomBiblio.grid(padx=5,row=0 ,column=1)
       	self.valider=Button(self.label_containResults,text='Valider',bd=2, relief=RAISED, overrelief=RIDGE,bg ='royal blue',command=self.creationBiblio)
       	self.valider.grid(row=0 ,column=2)


    def creationBiblio(self):
       	#self.creer.destroy()
    	if self.nomBiblio.get():
    		self.__B=Bibliotheque(self.nomBiblio.get())
    		self.labelNomBiblio.destroy()
    		self.nomBiblio.destroy()
    		self.valider.destroy()
    		print(self.__B)
    		# on affiche les infos de la bibliotheque
    		self.afficheBiblio()
    		# on affiche le menu
    		self.menu()

    def afficheBiblio(self):
        if self.__B!=None:
            self.label_containResults.configure(text="Information de la Bibliothèque",relief =RAISED)
            self.nom=StringVar()
            self.nom.set(self.__B.getNomBiblio())
            Label(self.label_containResults,text="Nom:", font="arial 12 ",bg='white').grid(padx=5, pady=5,row=0, column=0)
            Label(self.label_containResults,textvariable=self.nom, font="arial 12",bg='white').grid(padx=5, pady=5,row=0, column=1)
            self.nbLivre=StringVar()
            self.nbLivre.set(len(self.__B.getLivres()))
            Label(self.label_containResults,text="Nombre de Livres:", font="arial 12 ",bg='white').grid(padx=5, pady=5,row=1, column=0)
            Label(self.label_containResults,textvariable=self.nbLivre, font="arial 12 ",bg='white').grid(padx=5, pady=5,row=1, column=1)
            self.nbLecteur=StringVar()
            self.nbLecteur.set(len(self.__B.getLecteurs()))
            Label(self.label_containResults,text="Nombre d'abonnés:", font="arial 12 ",bg='white').grid(padx=5, pady=5,row=2, column=0)
            Label(self.label_containResults,textvariable=self.nbLecteur, font="arial 12 ",bg='white').grid(padx=5, pady=5,row=2, column=1)
            self.nbEmprunt=StringVar()
            self.nbEmprunt.set(len(self.__B.getEmprunts()))
            Label(self.label_containResults,text="Nombre d'Emprunts:", font="arial 12 ",bg='white').grid(padx=5, pady=5,row=3, column=0)
            Label(self.label_containResults,textvariable=self.nbEmprunt, font="arial 12 ",bg='white').grid(padx=5, pady=5,row=3, column=1)
    		
           

    def menu(self):
        self.labelContain_form.destroy()
        # Widgets de la fenetre de gauche u'on modifie
        self.labelContain_form=LabelFrame(self.contain_form,text="Menu",font="arial 12 bold italic",labelanchor = N,bg='white')
        self.labelContain_form.pack(padx=3, pady=5, expand="yes")
            #section Lecteur
        self.AddLecteur=Button(self.labelContain_form,text="Ajouter Lecteur",bd=2, width=20,relief=RAISED, bg ='#80c0c0', overrelief=RIDGE, command=self.add_lecteur)
        self.AddLecteur.grid(padx=5, pady=5, row=1 ,column=0)
        self.findLecteur_nom=Button(self.labelContain_form,text="Trouver un Lecteur (nom) ",bd=2,  width=20,relief=RAISED, bg ='#80c0c0',  overrelief=RIDGE, command=self.find_lecteur_nom)
        self.findLecteur_nom.grid(padx=5, pady=5, row=2 ,column=0)
        self.findLecteur_numero=Button(self.labelContain_form,text="Trouver un Lecteur (num)",bd=2,  width=20,relief=RAISED, bg ='#80c0c0',  overrelief=RIDGE, command=self.find_lecteur_numero)
        self.findLecteur_numero.grid(padx=5, pady=5, row=3 ,column=0)
        self.AfficheLecteur=Button(self.labelContain_form,text="Afficher Lecteurs",bd=2,  width=20,relief=RAISED, bg ='#80c0c0',  overrelief=RIDGE, command=self.afficher_lecteurs)
        self.AfficheLecteur.grid(padx=5, pady=5, row=4 ,column=0)
        self.retraitLecteur=Button(self.labelContain_form,text="Retirer Lecteur",bd=2,  width=20,relief=RAISED, bg ='#80c0c0',  overrelief=RIDGE, command=self.retirer_lecteur)
        self.retraitLecteur.grid(padx=5, pady=5, row=4 ,column=0)
            #section livre
        self.AddLivre=Button(self.labelContain_form,text="Ajouter Livre",bd=2,  width=20,relief=RAISED, bg ='#80c0c0', overrelief=RIDGE, command=self.add_livre)
        self.AddLivre.grid(padx=5, pady=5, row=6 ,column=0)
        self.findLivre_titre=Button(self.labelContain_form,text="Trouver un Livre (titre)",bd=2,  width=20,relief=RAISED, bg ='#80c0c0',  overrelief=RIDGE, command=self.find_livre_titre)
        self.findLivre_titre.grid(padx=5, pady=5, row=7 ,column=0)
        self.findLivre_numero=Button(self.labelContain_form,text="Trouver un Livre (numero)",bd=2,  width=20,relief=RAISED, bg ='#80c0c0', overrelief=RIDGE, command=self.find_livre_numero)
        self.findLivre_numero.grid(padx=5, pady=5, row=8 ,column=0)
        self.AfficheLivre=Button(self.labelContain_form,text="Afficher Livres",bd=2, width=20,relief=RAISED, bg ='#80c0c0', command=self.afficher_livres)
        self.AfficheLivre.grid(padx=5, pady=5, row=9 ,column=0)
            #section Emprunt
        self.AddEmprunt=Button(self.labelContain_form,text="Ajouter Emprunt",bd=2,  width=20,relief=RAISED, bg ='#80c0c0', overrelief=RIDGE, command=self.add_emprunt)
        self.AddEmprunt.grid(padx=5, pady=5, row=10 ,column=0)
        self.SuppEmprunt=Button(self.labelContain_form,text="Supprimer Emprunt",bd=2,  width=20,relief=RAISED, bg ='#80c0c0',  overrelief=RIDGE, command=self.supprimer_emprunt)
        self.SuppEmprunt.grid(padx=5, pady=5, row=11 ,column=0)
        self.AfficheEmprunt=Button(self.labelContain_form,text="Afficher Emprunts",bd=2,  width=20,relief=RAISED, bg ='#80c0c0', overrelief=RIDGE, command=self.afficher_emprunt)
        self.AfficheEmprunt.grid(padx=5, pady=5, row=12 ,column=0)
    
    def fermerToutToplevel(self):
        self.fenetre2.destroy()
        self.fenetre3.destroy()
        self.fenetre4.destroy()
        self.fenetre5.destroy()
        
    def add_lecteur(self):
        self.fermerToutToplevel()

        self.fenetre2 = Toplevel(self,bg ='#80c0c0', bd =5, relief =RAISED)
        self.fenetre2.geometry('400x400+100+250')
        self.fenetre2.title('Ajouter Lecteur')
        self.labelNomLecteur=Label(self.fenetre2,text="Nom", font="arial 12 bold",bg='white')
        self.labelNomLecteur.grid(padx=5, pady=20, row=0 ,column=0)
        self.nomLecteur=Entry(self.fenetre2,font="arial 15 ", width=20)
        self.nomLecteur.grid(padx=5,row=0 ,column=1)
        self.labelPnomLecteur=Label(self.fenetre2,text="Prénom", font="arial 12 bold",bg='white')
        self.labelPnomLecteur.grid(padx=5, pady=20, row=1 ,column=0)
        self.pnomLecteur=Entry(self.fenetre2,font="arial 15 ", width=20)
        self.pnomLecteur.grid(padx=5,row=1 ,column=1)
        self.labelAdresseLecteur=Label(self.fenetre2,text="Adresse", font="arial 12 bold",bg='white')
        self.labelAdresseLecteur.grid(padx=5, pady=20, row=2 ,column=0)
        self.adresseLecteur=Entry(self.fenetre2,font="arial 15 ", width=20)
        self.adresseLecteur.grid(padx=5,row=2 ,column=1)
        self.labelNumeroLecteur=Label(self.fenetre2,text="N° Lecteur", font="arial 12 bold",bg='white')
        self.labelNumeroLecteur.grid(padx=5, pady=20, row=3 ,column=0)
        self.numeroLecteur=Entry(self.fenetre2,font="arial 15 ", width=20)
        self.numeroLecteur.grid(padx=5,row=3 ,column=1)
        self.validerLecteur=Button(self.fenetre2,text='Valider',bd=2, relief=RAISED, overrelief=RIDGE,bg ='royal blue',command=self.valider_ajout_lecteur)
        self.validerLecteur.grid(pady=15,row=4 ,column=1)
        self.annulerLecteur=Button(self.fenetre2,text='Quitter',bd=2, relief=RAISED, overrelief=RIDGE,fg="red",command=self.fenetre2.destroy)
        self.annulerLecteur.grid(row=5 ,column=1)

    def valider_ajout_lecteur(self):
        if self.nomLecteur.get() and self.pnomLecteur.get() and self.adresseLecteur.get() and self.numeroLecteur.get():
            self.__B.ajouterLecteur(self.nomLecteur.get(),self.pnomLecteur.get(),self.adresseLecteur.get(),int(self.numeroLecteur.get()))
            self.fenetre2.destroy()
            showinfo('Résultat','Lecteur crée avec succès!')
            self.label_containResults.destroy()
            self.rafraichir_affichage()
            print(self.__B)


    def rafraichir_affichage(self):
        self.label_containResults.destroy()
        self.label_containResults=LabelFrame(self.contain_results,text="Information de la Bibliothèque",font="arial 12 bold italic",labelanchor = N,bg='white')
        self.label_containResults.pack(padx=5, pady=5, expand="yes")
        self.nom=StringVar()
        self.nom.set(self.__B.getNomBiblio())
        Label(self.label_containResults,text="Nom:", font="arial 12 ",bg='white').grid(padx=5, pady=5,row=0, column=0)
        Label(self.label_containResults,textvariable=self.nom, font="arial 12",bg='white').grid(padx=5, pady=5,row=0, column=1)
        self.nbLivre=StringVar()
        self.nbLivre.set(len(self.__B.getLivres()))
        Label(self.label_containResults,text="Nombre de Livres:", font="arial 12 ",bg='white').grid(padx=5, pady=5,row=1, column=0)
        Label(self.label_containResults,textvariable=self.nbLivre, font="arial 12 ",bg='white').grid(padx=5, pady=5,row=1, column=1)
        self.nbLecteur=StringVar()
        self.nbLecteur.set(len(self.__B.getLecteurs()))
        Label(self.label_containResults,text="Nombre d'abonnés:", font="arial 12 ",bg='white').grid(padx=5, pady=5,row=2, column=0)
        Label(self.label_containResults,textvariable=self.nbLecteur, font="arial 12 ",bg='white').grid(padx=5, pady=5,row=2, column=1)
        self.nbEmprunt=StringVar()
        self.nbEmprunt.set(len(self.__B.getEmprunts()))
        Label(self.label_containResults,text="Nombre d'Emprunts:", font="arial 12 ",bg='white').grid(padx=5, pady=5,row=3, column=0)
        Label(self.label_containResults,textvariable=self.nbEmprunt, font="arial 12 ",bg='white').grid(padx=5, pady=5,row=3, column=1)
            


    def find_lecteur_nom(self):
        self.fermerToutToplevel()

        self.fenetre3 = Toplevel(self,bg ='#80c0c0', bd =5, relief =RAISED)
        self.fenetre3.geometry('500x100+100+250')
        self.fenetre3.title('Chercher un Lecteur par son nom')
        self.labelNomLecteur=Label(self.fenetre3,text="Nom", font="arial 12 bold",bg='white')
        self.labelNomLecteur.grid(padx=5, pady=20, row=0 ,column=0)
        self.nomLecteur=Entry(self.fenetre3,font="arial 15 ", width=20)
        self.nomLecteur.grid(padx=5,row=0 ,column=1)
        self.chercherLecteur=Button(self.fenetre3,text='Chercher',bd=2, relief=RAISED,  overrelief=RIDGE,bg ='royal blue',command=self.valider_recherche_lecteurNom)
        self.chercherLecteur.grid(padx=15,row=0 ,column=2)
        self.annulerLecteur=Button(self.fenetre3,text='Quitter',bd=2, relief=RAISED,  overrelief=RIDGE,fg="red",command=self.fenetre3.destroy)
        self.annulerLecteur.grid(padx=0,row=0 ,column=3)

    def valider_recherche_lecteurNom(self):
        if self.nomLecteur.get():
            self.resultat="Aucun Lecteur n'a été trouvé!"
            boolen,res=self.__B.chercherLecteurByNom(self.nomLecteur.get())
            if boolen:
                self.resultat=res
            showinfo('Résultat',self.resultat)
            print(boolen)
            print(self.resultat)

    def find_lecteur_numero(self):
        self.fermerToutToplevel()

        self.fenetre4 = Toplevel(self,bg ='#80c0c0', bd =5, relief =RAISED)
        self.fenetre4.geometry('400x100+100+250')
        self.fenetre4.title('Chercher un Lecteur par son numero')
        self.labelNumeroLecteur=Label(self.fenetre4,text="N°", font="arial 12 bold",bg='white')
        self.labelNumeroLecteur.grid(padx=5, pady=20, row=0 ,column=0)
        self.numeroLecteur=Entry(self.fenetre4,font="arial 15 ", width=10)
        self.numeroLecteur.grid(padx=5,row=0 ,column=1)
        self.chercherLecteur=Button(self.fenetre4,text='Chercher',bd=2, relief=RAISED,  overrelief=RIDGE,bg ='royal blue',command=self.valider_recherche_lecteurNumero)
        self.chercherLecteur.grid(padx=15,row=0 ,column=2)
        self.annulerLecteur=Button(self.fenetre4,text='Quitter',bd=2, relief=RAISED,  overrelief=RIDGE,fg="red",command=self.fenetre4.destroy)
        self.annulerLecteur.grid(padx=0,row=0 ,column=3)

    def valider_recherche_lecteurNumero(self):
        if self.numeroLecteur.get():
            self.resultat="Aucun Lecteur n'a été trouvé!"
            boolen,res=self.__B.chercherLecteurByNumero(int(self.numeroLecteur.get()))
            if boolen:
                self.resultat=res
            showinfo('Résultat',self.resultat)
            print(boolen)
            print(self.resultat)

    def afficher_lecteurs(self):
        self.resultat="Rien à afficher"
        res=self.__B.afficherLecteurs()
        if len(res)!=0:
            self.resultat=res
        showinfo('Résultat',self.resultat)
        print(self.resultat)

    def retirer_lecteur(self):
        self.fermerToutToplevel()

        self.fenetre4 = Toplevel(self,bg ='#80c0c0', bd =5, relief =RAISED)
        self.fenetre4.geometry('400x100+100+250')
        self.fenetre4.title('N°Lecteur à supprimé')
        self.labelNumeroLecteur=Label(self.fenetre4,text="N°", font="arial 12 bold",bg='white')
        self.labelNumeroLecteur.grid(padx=5, pady=20, row=0 ,column=0)
        self.numeroLecteur=Entry(self.fenetre4,font="arial 15 ", width=10)
        self.numeroLecteur.grid(padx=5,row=0 ,column=1)
        self.chercherLecteur=Button(self.fenetre4,text='Supprimer',bd=2, relief=RAISED,  overrelief=RIDGE,bg ='royal blue',command=self.valider_retrait_lecteur)
        self.chercherLecteur.grid(padx=15,row=0 ,column=2)
        self.annulerLecteur=Button(self.fenetre4,text='Quitter',bd=2, relief=RAISED,  overrelief=RIDGE,fg="red",command=self.fenetre4.destroy)
        self.annulerLecteur.grid(padx=0,row=0 ,column=3)

    def valider_retrait_lecteur(self):
        if self.numeroLecteur.get():
            res=self.__B.retraitLecteur(int(self.numeroLecteur.get()))
            if res==1:
                self.resultat="Retrait effectué avec succès!"
            elif res==0:
                self.resultat="Echec! Le lecteur n'existe pas"
            else:
                self.resultat="Impossible de supprimr le lecteur, il a des emprunts en cours"
            self.fenetre2.destroy()
            showinfo('Résultat',self.resultat)
            self.label_containResults.destroy()
            self.rafraichir_affichage()
            print(self.__B)


    def add_livre(self):
        self.fermerToutToplevel()

        self.fenetre2 = Toplevel(self,bg ='#80c0c0', bd =5, relief =RAISED)
        self.fenetre2.geometry('400x400+100+250')
        self.fenetre2.title('Ajouter Livre')
        self.labelTitre=Label(self.fenetre2,text="Titre", font="arial 12 bold",bg='white')
        self.labelTitre.grid(padx=5, pady=20, row=0 ,column=0)
        self.titre=Entry(self.fenetre2,font="arial 15 ", width=20)
        self.titre.grid(padx=5,row=0 ,column=1)
        self.labelAuteur=Label(self.fenetre2,text="Auteur", font="arial 12 bold",bg='white')
        self.labelAuteur.grid(padx=5, pady=20, row=1 ,column=0)
        self.auteur=Entry(self.fenetre2,font="arial 15 ", width=20)
        self.auteur.grid(padx=5,row=1 ,column=1)
        self.labelNumeroLivre=Label(self.fenetre2,text="N° Livre", font="arial 12 bold",bg='white')
        self.labelNumeroLivre.grid(padx=5, pady=20, row=2 ,column=0)
        self.numeroLivre=Entry(self.fenetre2,font="arial 15 ", width=20)
        self.numeroLivre.grid(padx=5,row=2 ,column=1)
        self.labelNombreLivre=Label(self.fenetre2,text="Nbre Exemplaire", font="arial 12 bold",bg='white')
        self.labelNombreLivre.grid(padx=5, pady=20, row=3 ,column=0)
        self.nombreLivre=Entry(self.fenetre2,font="arial 15 ", width=20)
        self.nombreLivre.grid(padx=5,row=3 ,column=1)
        self.validerLivre=Button(self.fenetre2,text='Valider',bd=2, relief=RAISED,  overrelief=RIDGE,bg ='royal blue',command=self.valider_ajout_livre)
        self.validerLivre.grid(pady=15,row=4 ,column=1)
        self.annulerLecteur=Button(self.fenetre2,text='Quitter',bd=2, relief=RAISED, overrelief=RIDGE,fg="red",command=self.fenetre2.destroy)
        self.annulerLecteur.grid(row=5 ,column=1)

    def valider_ajout_livre(self):
        if self.titre.get() and self.auteur.get() and self.numeroLivre.get() and self.nombreLivre.get():
            self.__B.ajouterLivre(self.auteur.get(),self.titre.get(),int(self.numeroLivre.get()),int(self.nombreLivre.get()))
            self.fenetre2.destroy()
            showinfo('Résultat','Livre crée avec succès!')
            self.label_containResults.destroy()
            self.rafraichir_affichage()
            print(self.__B)

    def find_livre_numero(self):
        self.fermerToutToplevel()

        self.fenetre4 = Toplevel(self,bg ='#80c0c0', bd =5, relief =RAISED)
        self.fenetre4.geometry('400x100+100+250')
        self.fenetre4.title('Chercher un Livre par son numero')
        self.labelNumeroLivre=Label(self.fenetre4,text="N°", font="arial 12 bold",bg='white')
        self.labelNumeroLivre.grid(padx=5, pady=20, row=0 ,column=0)
        self.numeroLivre=Entry(self.fenetre4,font="arial 15 ", width=10)
        self.numeroLivre.grid(padx=5,row=0 ,column=1)
        self.chercherLivre=Button(self.fenetre4,text='Chercher',bd=2, relief=RAISED,  overrelief=RIDGE,bg ='royal blue',command=self.valider_recherche_livreNumero)
        self.chercherLivre.grid(padx=15,row=0 ,column=2)
        self.annulerLivre=Button(self.fenetre4,text='Quitter',bd=2, relief=RAISED,  overrelief=RIDGE,fg="red",command=self.fenetre4.destroy)
        self.annulerLivre.grid(padx=0,row=0 ,column=3)

    def valider_recherche_livreNumero(self):
        if self.numeroLivre.get():
            self.resultat="Aucun Livre n'a été trouvé!"
            boolen,res=self.__B.chercherLivreByNumero(int(self.numeroLivre.get()))
            if boolen:
                self.resultat=res
            showinfo('Résultat',self.resultat)
            print(boolen)
            print(self.resultat)


    def find_livre_titre(self):
        self.fermerToutToplevel()

        self.fenetre3 = Toplevel(self,bg ='#80c0c0', bd =5, relief =RAISED)
        self.fenetre3.geometry('500x100+100+250')
        self.fenetre3.title('Chercher un Livre par son titre')
        self.labelTitre=Label(self.fenetre3,text="Titre", font="arial 12 bold",bg='white')
        self.labelTitre.grid(padx=5, pady=20, row=0 ,column=0)
        self.titre=Entry(self.fenetre3,font="arial 15 ", width=20)
        self.titre.grid(padx=5,row=0 ,column=1)
        self.chercherLivre=Button(self.fenetre3,text='Chercher',bd=2, relief=RAISED,  overrelief=RIDGE,bg ='royal blue',command=self.valider_recherche_livreTitre)
        self.chercherLivre.grid(padx=15,row=0 ,column=2)
        self.annulerLivre=Button(self.fenetre3,text='Quitter',bd=2, relief=RAISED,  overrelief=RIDGE,fg="red",command=self.fenetre3.destroy)
        self.annulerLivre.grid(padx=0,row=0 ,column=3)

    def valider_recherche_livreTitre(self):
        if self.titre.get():
            self.resultat="Aucun Livre n'a été trouvé!"
            boolen,res=self.__B.chercherLivreByTitre(self.titre.get())
            if boolen:
                self.resultat=res
            showinfo('Résultat',self.resultat)
            print(boolen)
            print(self.resultat)

    def afficher_livres(self):
        self.resultat="Rien à afficher"
        res=self.__B.afficherLivres()
        if len(res)!=0:
            self.resultat=res
        showinfo('Résultat',self.resultat)
        print(self.resultat)

    def add_emprunt(self):
        self.fermerToutToplevel()

        self.fenetre2 = Toplevel(self,bg ='#80c0c0', bd =5, relief =RAISED)
        self.fenetre2.geometry('400x300+100+250')
        self.fenetre2.title('Ajouter Emprunt')
        self.labelNumeroLivre=Label(self.fenetre2,text="N°Livre", font="arial 12 bold",bg='white')
        self.labelNumeroLivre.grid(padx=5, pady=20, row=0 ,column=0)
        self.numeroLivre=Entry(self.fenetre2,font="arial 15 ", width=20)
        self.numeroLivre.grid(padx=5,row=0 ,column=1)
        self.labelNumeroLecteur=Label(self.fenetre2,text="N°Lecteur", font="arial 12 bold",bg='white')
        self.labelNumeroLecteur.grid(padx=5, pady=20, row=1 ,column=0)
        self.numeroLecteur=Entry(self.fenetre2,font="arial 15 ", width=20)
        self.numeroLecteur.grid(padx=5,row=1 ,column=1)
        self.validerEmprunt=Button(self.fenetre2,text='Valider',bd=2, relief=RAISED,  overrelief=RIDGE,bg ='royal blue',command=self.valider_ajout_emprunt)
        self.validerEmprunt.grid(pady=15,row=4 ,column=1)
        self.annulerEmprunt=Button(self.fenetre2,text='Quitter',bd=2, relief=RAISED,  overrelief=RIDGE,fg="red",command=self.fenetre2.destroy)
        self.annulerEmprunt.grid(row=5 ,column=1)

    def valider_ajout_emprunt(self):
        if self.numeroLecteur.get() and self.numeroLivre.get():
            res=self.__B.ajouterEmprunt(int(self.numeroLivre.get()),int(self.numeroLecteur.get()))
            self.fenetre2.destroy()
            if not res:
                showinfo('Résultat','Echec Emprunt!')
            else:
                showinfo('Résultat','Emprunt ajouté avec succès!')
            self.label_containResults.destroy()
            self.rafraichir_affichage()
            print(self.__B)

    def supprimer_emprunt(self):
        self.fermerToutToplevel()

        self.fenetre2 = Toplevel(self,bg ='#80c0c0', bd =5, relief =RAISED)
        self.fenetre2.geometry('400x300+100+250')
        self.fenetre2.title('Supprimer Emprunt')
        self.labelNumeroLivre=Label(self.fenetre2,text="N°Livre", font="arial 12 bold",bg='white')
        self.labelNumeroLivre.grid(padx=5, pady=20, row=0 ,column=0)
        self.numeroLivre=Entry(self.fenetre2,font="arial 15 ", width=20)
        self.numeroLivre.grid(padx=5,row=0 ,column=1)
        self.labelNumeroLecteur=Label(self.fenetre2,text="N°Lecteur", font="arial 12 bold",bg='white')
        self.labelNumeroLecteur.grid(padx=5, pady=20, row=1 ,column=0)
        self.numeroLecteur=Entry(self.fenetre2,font="arial 15 ", width=20)
        self.numeroLecteur.grid(padx=5,row=1 ,column=1)
        self.validerEmprunt=Button(self.fenetre2,text='Supprimer',bd=2, relief=RAISED,  overrelief=RIDGE,bg ='royal blue',command=self.valider_supprimer_emprunt)
        self.validerEmprunt.grid(pady=15,row=4 ,column=1)
        self.annulerEmprunt=Button(self.fenetre2,text='Quitter',bd=2, relief=RAISED,  overrelief=RIDGE,fg="red",command=self.fenetre2.destroy)
        self.annulerEmprunt.grid(row=5 ,column=1)

    def valider_supprimer_emprunt(self):
        if self.numeroLecteur.get() and self.numeroLivre.get():
            res=self.__B.supprimerEmprunt(int(self.numeroLivre.get()),int(self.numeroLecteur.get()))
            self.fenetre2.destroy()
            if not res:
                showinfo('Résultat','Echec Suppression Emprunt!')
            else:
                showinfo('Résultat','Emprunt supprimé avec succès!')
            self.label_containResults.destroy()
            self.rafraichir_affichage()
            print(self.__B)


    def afficher_emprunt(self):
        self.resultat="Rien à afficher"
        res=self.__B.afficherEmprunts()
        if len(res)!=0:
            self.resultat=res
        showinfo('Résultat',self.resultat)
        print(self.resultat)

##############################################################################

if __name__ == '__main__':
    Biblio=BibiothequeGraphique()
    Biblio.mainloop()
