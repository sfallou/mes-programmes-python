#!/usr/bin/python        # Emplacement de l’interpréteur Python (sous Linux)
# -*- coding: utf-8 -*-  # Définition l'encodage des caractères
from tkinter import *
 
def repondre():
 affichage['text'] = reponse.get()	# lecture du contenu du widget "reponse"
 
Fenetre = Tk()
Fenetre.title('Mon nom')
 
nom = Label(Fenetre, text = 'Votre nom :')
reponse = Entry(Fenetre)
valeur = Button(Fenetre, text =' Valider', command=repondre)
affichage = Label(Fenetre, width=30)
votre_nom=Label(Fenetre, text='Votre nom est :')
nom.pack()
reponse.pack()
valeur.pack()
votre_nom.pack()
affichage.pack()
 
Fenetre.mainloop()
