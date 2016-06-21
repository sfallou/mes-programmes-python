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
from threading import *
import time
from tkinter import *
import queue
import math
##############################################################

Couleurs=['green','yellow','blue','wihte']

"""
-------------------------------------------------------------
Classe BalleMobile											|
-------------------------------------------------------------
"""
class BalleMobile:
	def __init__(self,can,x,y,couleur,rayon,angle,vitesse):
		self.__can=can
		self.__x=x
		self.__y=y
		self.__couleur=couleur
		self.__rayon=rayon
		self.__angle=angle
		self.__vitesse_x=vitesse
		self.__vitesse_y=vitesse
		self.__balle=self.__can.create_oval(self.__x-self.__rayon,self.__y-self.__rayon,self.__x+self.__rayon,self.__y+self.__rayon, outline=self.__couleur)

	def deplacement(self):
		w=self.__can.winfo_width()
		h=self.__can.winfo_hight()
		dx=self.__vitesse_x*math.cos(self.__angle)
		dy=self.__vitesse_y*math.sin(self.__angle)
		if (self.__x+dx+self.__rayon>w) or (self.__x+dx-self.__rayon<0):
			self.__vitesse_x=-self.__vitesse_x
		if (self.__y+dy+self.__rayon>h) or (self.__y+dy-self.__rayon<0):
			self.__vitesse_y=-self.__vitesse_y
		dx=self.__vitesse_x*math.cos(self.__angle)
		dy=self.__vitesse_y*math.sin(self.__angle)
		self.__x+=dx
		self.__y+=dy
		self.__can.move(self.__balle,dx,dy)
		
"""
-------------------------------------------------------------
Classe ZoneAffichage pour afficher les balles               |
-------------------------------------------------------------
"""
class ZoneAffichage(Canvas):
	def __init__(self,w, h):
		Canvas.__init__(self, width = w, height = h, bg = 'black') # Héritage de Canvas
		self.__balles=[]									
	
	def ajoutBalle(self,x,y,rayon,couleur,angle,vitesse):
		self.__balles.append(BalleMobile(self,x,y,rayon,couleur,angle,vitesse))

	def afficher(self):
		for b in self.__balles:
			b.deplacement()
		self.after(10,self.afficher) # boucler après 10 millisecondes


########################### Fin de la classe ################################
"""
-------------------------------------------------------------
Classe Generateur qui herite de Threads                     |
-------------------------------------------------------------
"""
class Generateur(Thread):
	def __init__(self,capacite):
		Thread.__init__(self)
		self.__queue=queue.Queue(capacite)
		self.__running=True

	def getQueue(self):
		return self.__queue
	
	def stop(self):
		self.__running = False

	def run(self):
		while self.__running:
			if randint(0,1000)<60:
				x=randint(100,150)
				y=randint(100,150)
				couleur=Couleurs[randint(0,len(Couleurs))]
				rayon=randint(10,30)
				angle=math.radians(randint(1,360))
				vitessex=randint(1,150)
				#vitesseY=randint(1,150)
				queue.put(x,y,rayon,couleur,angle,vitesseX)
		time.sleep(0.01)

########################### Fin de la classe###################################
"""
----------------------------------------------------------------------------
Classe FenPrincipale heritant de TK et qui utilise les classes précédentes |
----------------------------------------------------------------------------
"""
class FenPrincipale(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title('Animation Balles')
		#Canevas d'affichage la balle
		self.__zoneAffichage = ZoneAffichage(320,320)
		self.__zoneAffichage.pack(padx=5, pady=5)
		self.__generator=Generateur(3000)
		# Frame qui contient le menu
		f1=Frame(self)
		f1.pack(side=TOP,padx=5,pady=5)
		boutonNew = Button(f1, text ='Démarrer',bd=2, relief=RAISED,  bg ='royal' \
			'blue', overrelief=RIDGE,command =self.demarreAnimation).pack(side=LEFT,padx=5,pady=5)
		boutonQuit = Button(f1, text ='Quitter',bd=2, relief=RAISED,  bg ='re'\
			'd', overrelief=RIDGE, command =self.destroy).pack(side=LEFT,padx=5,pady=5)

	
	def demarreAnimation(self):
		self.__generator.start()
		self.__zoneAffichage.afficher()
		self.verifierGenerateur()

	def verifierGenerateur(self):
		try:
			x,y,rayon,couleur,angle,vitesse=self.__generator.getQueue().get(block=False)
		except queue.Empty:
			pass
		else:
			self.__zoneAffichage.ajoutBalle(x,y,rayon,couleur,angle,vitesse)
		self.__zoneAffichage.after(50,self.verifierGenerateur)


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
