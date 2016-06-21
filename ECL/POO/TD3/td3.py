# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from Forme import *
from Dessin import *


class ZoneAffichage(Canvas):
	def __init__(self,parent, w, h, c):
		Canvas.__init__(self, width = w, height = h, bg = c)
		self.__d=Dessin()
		self.__cer=Cercle(100,100,"blue",100)
		self.__rec=Rectangle(220,220,"yellow",230,125)
		self.__car=Carre(400,120,"green",100)
		self.__d.addForme(self.__cer)
		self.__d.addForme(self.__rec)
		self.__d.addForme(self.__car)

	def afficher(self):
		self.__d.afficher(self)

	def selectForme(self,x,y):
		if self.__d.selectForme(x,y)!=False:
			if self.__d.selectForme(x,y)==1:
				showinfo('Rectangle',str(self.__rec))
			elif self.__d.selectForme(x,y)==2:
				showinfo('Résultat',str(self.__cer))
			else:
				showinfo('Résultat',str(self.__car))
	
class FenPrincipale(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title('Affichage des formes')
		self.__zoneAffichage = ZoneAffichage(self,480,320,'white')
		# La méthode bind() permet de lier un événement avec une fonction :
		# un clic gauche sur la zone graphique provoquera l'appel de la fonction utilisateur cliquer()
		self.__zoneAffichage.bind('<Button-1>',self.cliquer)
		self.__zoneAffichage.pack(padx=5, pady=5)
		# Création d'un widget Button (bouton Afficher)
		self.__boutonAfficher = Button(self, text ='Afficher', command =self.afficherTout).pack(side=LEFT,padx = 5,pady = 5)
		# Création d'un widget Button (bouton Effacer)
		self.__boutonEffacer = Button(self, text ='Effacer', command =self.effacer).pack(side=LEFT,padx = 5,pady = 5)
		# Création d'un widget Button (bouton Quitter)
		self.__boutonQuitter = Button(self, text ='Quitter', command =self.destroy).pack(side=LEFT,padx=5,pady=5)

	def afficherTout(self):
		self.__zoneAffichage.afficher()

		

	def cliquer(self,event):
		""" Gestion de l'événement Clic gauche sur la zone graphique """
		# position du pointeur de la souris
		x = event.x
		y = event.y
		self.__zoneAffichage.selectForme(x,y)

	def effacer(self):
		""" Efface la zone graphique """
		self.__zoneAffichage.delete(ALL)
		
if __name__ == '__main__':
# Création de la fenêtre principale
	fen = FenPrincipale()
	fen.mainloop()
