# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------
@Authors: Serigne Fallou NDIAYE  & Jordan N'Guessan Ziahi KONAN   |
@From: Ecole Centrale de Lyon                                     |
@Prog: POO : Pendu                                                |
@Date: 01 - 05 - 2016                                             |	
-------------------------------------------------------------------
"""
########################## Début du programme  #################################

"""
-----------------------------------------------------------
Importation des bibliothèques utilisées dans ce programme |
-----------------------------------------------------------
"""
from tkinter import *
from tkinter.messagebox import *
from Forme import *
from Dessin import *
from random import randint

"""
-------------------------------------------------------------
Classe ZoneAffichage pour afficher les formes géométriques  |
-------------------------------------------------------------
"""
class ZoneAffichage(Canvas):
	def __init__(self,parent, w, h, c):
		Canvas.__init__(self, width = w, height = h, bg = c) # Héritage de Canvas
		self.__d=Dessin()									# objet qui va dessiner les formes
		# L'ensembles des formes nécessaires pour afficher le pendu
		self.__rec1=Rectangle(100,305,"black",50,2)         
		self.__rec2=Rectangle(100,180,"black",2,250)
		self.__rec3=Rectangle(155,55,"black",105,2)
		self.__rec4=Rectangle(205,75,"black",2,35)
		self.__cer=Cercle(205,110,"black",40) # Tête
		self.__rec5=Rectangle(205,155,"black",20,55)
		self.__rec6=Rectangle(196,200,"black",2,55)
		self.__rec7=Rectangle(214,200,"black",2,55)
		self.__rec8=Rectangle(176,145,"black",40,2)
		self.__rec9=Rectangle(234,145,"black",40,2)
		# on ajoute les formes dans l'objet Dessin
		self.__d.addForme(self.__rec9)
		self.__d.addForme(self.__rec8)
		self.__d.addForme(self.__rec7)
		self.__d.addForme(self.__rec6)
		self.__d.addForme(self.__rec5)
		self.__d.addForme(self.__cer)
		self.__d.addForme(self.__rec4)
		self.__d.addForme(self.__rec3)
		self.__d.addForme(self.__rec2)
		self.__d.addForme(self.__rec1)
	# Méthode qui permet d'afficher un élément contenu dans l'objet dessin
	def afficherElement(self,nb):
		self.__d.afficherElement(self,nb)


########################### Fin de la classe ################################
"""
-------------------------------------------------------------
Classe MonButton pour afficher et gérer le clavier virtuel  |
-------------------------------------------------------------
"""
class MonButton(Button):
	def __init__(self,parent,fenPr,l,w):
		self.__fenPr=fenPr
		self.__lettre=l
		Button.__init__(self,master=parent,text=self.__lettre,width=w,bd=2, relief=RAISED, fg='re'\
			'd', bg ='white', overrelief=RIDGE)

	# Méthode cliquer qui désactive le bouton cliqué et fait appel à la methode traitement de FenPrincipale
	def cliquer(self):
		self.config(state=DISABLED)
		self.__fenPr.traitement(self.__lettre)

########################### Fin de la classe###################################
"""
----------------------------------------------------------------------------
Classe FenPrincipale heritant de TK et qui utilise les classes précédentes |
----------------------------------------------------------------------------
"""
class FenPrincipale(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title('Jeu du Pendu')
		# Frame qui contient le menu
		f1=Frame(self)
		f1.pack(side=TOP,padx=5,pady=5)
		boutonNew = Button(f1, text ='Nouvelle Partie',bd=2, relief=RAISED,  bg ='royal' \
			'blue', overrelief=RIDGE, command =self.newPartie).pack(side=LEFT,padx=5,pady=5)
		boutonQuit = Button(f1, text ='Quitter',bd=2, relief=RAISED,  bg ='re'\
			'd', overrelief=RIDGE, command =self.destroy).pack(side=LEFT,padx=5,pady=5)
		#Canevas d'affichage des formes (le pendu)
		self.__zoneAffichage = ZoneAffichage(self,320,320,'snow2')
		self.__zoneAffichage.pack(padx=5, pady=5)
		#Label qui va servir à afficher le mot à deviner 
		self.__labelMot=Label(self,bd=5, relief=SUNKEN, bg='white',font=('Helvetica', 12))
		self.__labelMot.pack(padx=5,pady=5)
		# Frame qui contient les buttons du clavier virtuel
		f2=Frame(self)
		f2.pack(side=TOP,padx=5,pady=5)
		#Création des boutons du clavier
		self.__buttons = []
		for i in range(26):
			l=chr(ord('A')+i)
			self.__buttons.append(MonButton(f2,self,l,4))
			self.__buttons[i].config(command=self.__buttons[i].cliquer)
		# Affichage du clavier virtuel
		for i in range(3):
			for j in range(7):
				self.__buttons[j+7*i].grid(padx=1,pady=1,row=i,column=j)
		for i in range(1):
			for  j in range(5):
				self.__buttons[21+j].grid(padx=1,pady=1,row=4,column=j+1)

		#on fait appel aux méthodes chargerMots et newPartie dans le constructeur de la classe
		# pour pouvoir gérer l'initialisation des variables nécessaires pour jouer une partie
		self.chargerMots()
		self.newPartie()

		"""
		-------------------------------------------------------------
		Méthode newPartie pour initialiser les paramètres du jeu    |
		-------------------------------------------------------------
		"""
	def newPartie(self):
		self.effacer() # on efface le canvas
		self.__mot=self.nouveauMot() # on récupère le mot tiré au hasard
		print(self.__mot)	# on va afficher le mot dans le console (pour pouvoir tester le fonctionnement de code)
		self.__motAffiche=len(self.__mot)*'*' #On affiche les asterix pour cacher le mot à deviner
		self.__labelMot.config(text='Mot: '+self.__motAffiche,bg='white')
		self.__nbManques=0 # va servir à afficher le bon élément du pendu et à determiner la fin de partie
		self.__nbGagne=0   # permet de determiner la fin de partie
		self.__lesmots=len(self.__mot)*['*']
		for b in self.__buttons:   #activation de tous les boutons du clavier virtuel
			b.config(state=NORMAL)
		"""
		--------------------------------------------------------------------------------
		Méthode chargerMots pour récuperer les mots contenus dans le fichier mots.txt  |
		--------------------------------------------------------------------------------
		"""
	def chargerMots(self):
		fich=open('mots.txt','r')
		contenu=fich.read()
		self.__mots=contenu.split('\n')
		fich.close()
		"""
		----------------------------------------------------------------------
		Méthode nouveauMot pour séléctionner au hasard un mot du fichier txt |
		----------------------------------------------------------------------
		"""
	def nouveauMot(self):
		return self.__mots[randint(0,len(self.__mots))]
		"""
		----------------------------------------------------------------------------------------
		Méthode traitement qui constitue le coeur du programme en prenant en entrée une lettre |
		pour ensuite décider de l'affichage du pendu ou non en fonction du résultat du clic    |
		----------------------------------------------------------------------------------------
		"""
	def traitement(self,letr):
		cpt=0  								# un compteur pour determiner le nombre de fois oû la lettre apparait 
		for i in range(0,len(self.__mot)):	# on parcours le mot et teste si la lettre s'y trouve ou pas
			if self.__mot[i]==letr:
				self.__lesmots[i]=letr
				cpt+=1
				self.__nbGagne+=1
		if cpt==0:							# si la lettre n'est pas dans le mot on affiche un élément du pendu
			self.__nbManques+=1
			self.afficheElement(self.__nbManques)
			#tester si fin partie
			if self.__nbManques==10:
				self.finPartie(False)
		else:								# sinon on affiche une partie du mot à deviner
			self.__labelMot.config(text='Mot: '+''.join(self.__lesmots))
			# on teste si fin partie
			if self.__nbGagne==len(self.__mot):
				self.finPartie(True)
		"""
		----------------------------------------------------------------------------------
		Méthode finPartie qui prend un booléen et affiche le résultat final de la partie |
		----------------------------------------------------------------------------------
		"""
	def finPartie(self,booleen):
		if booleen:
			message=self.__mot+" - Bravo! Vous avez gagné."
			couleur='green'
		else:
			message="Vous avez perdu! Le mot était: "+self.__mot
			couleur='red'
		#on change le texte qui va s'afficher à la place du mot et la couleur du label
		self.__labelMot.config(text=message,bg=couleur)
		#on desactive le clavier
		for but in self.__buttons:
			but.config(state=DISABLED)
		"""
		---------------------------------------------------------------------------------------
		Méthode afficherElement qui fait appelle à la méthode afficherElement de ZoneAffichage|
		---------------------------------------------------------------------------------------
		"""
	def afficheElement(self,nb):
		self.__zoneAffichage.afficherElement(nb)
		"""
		-------------------------------------------------------------
		Méthode qui sert juste à effacer le canevas                 |
		-------------------------------------------------------------
		"""
	def effacer(self):
		""" Efface la zone graphique """
		self.__zoneAffichage.delete(ALL)

########################## Fin de la classe ######################

##########################################################################################
#                            Execution du programme principale                           #
##########################################################################################		
if __name__ == '__main__':
# Création de la fenêtre principale
	fen = FenPrincipale()
	fen.mainloop()
