# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from Forme import *
from Dessin import *
from random import randint

###############################################################"
class ZoneAffichage(Canvas):
	def __init__(self,parent, w, h, c):
		Canvas.__init__(self, width = w, height = h, bg = c)
		self.__d=Dessin()
		self.__rec1=Rectangle(100,305,"black",50,2) 
		self.__rec2=Rectangle(100,180,"black",2,250)
		self.__rec3=Rectangle(155,55,"black",105,2)
		self.__rec4=Rectangle(205,75,"black",2,35)
		self.__cer=Cercle(205,110,"black",40)
		self.__rec5=Rectangle(205,155,"black",20,55)
		self.__rec6=Rectangle(196,200,"black",2,55)
		self.__rec7=Rectangle(214,200,"black",2,55)
		self.__rec8=Rectangle(176,145,"black",40,2)
		self.__rec9=Rectangle(234,145,"black",40,2)
	
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

	def afficher(self):
		self.__d.afficher(self)

	def afficherElement(self,nb):
		self.__d.afficherElement(self,nb)

	def selectForme(self,x,y):
		if self.__d.selectForme(x,y)!=False:
			if self.__d.selectForme(x,y)==1:
				showinfo('Rectangle',str(self.__rec))
			elif self.__d.selectForme(x,y)==2:
				showinfo('Résultat',str(self.__cer))
			else:
				showinfo('Résultat',str(self.__car))


########################################################################
class MonButton(Button):
	def __init__(self,parent,fenPr,l,w):
		self.__fenPr=fenPr
		self.__lettre=l
		Button.__init__(self,master=parent,text=self.__lettre,width=w,bd=2, relief=RAISED, fg='red', bg ='white', overrelief=RIDGE)

	def cliquer(self):
		self.config(state=DISABLED)
		self.__fenPr.traitement(self.__lettre)
		return self.__lettre
		

########################################################################
class FenPrincipale(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title('Jeu du Pendu')
		#Création de la première Frame
		f1=Frame(self)
		f1.pack(side=TOP,padx=5,pady=5)
		boutonNew = Button(f1, text ='Nouvelle Partie',bd=2, relief=RAISED,  bg ='royal blue', overrelief=RIDGE, command =self.newPartie).pack(side=LEFT,padx=5,pady=5)
		boutonQuit = Button(f1, text ='Quitter',bd=2, relief=RAISED,  bg ='red', overrelief=RIDGE, command =self.destroy).pack(side=LEFT,padx=5,pady=5)
		#Canevas d'affichage
		self.__zoneAffichage = ZoneAffichage(self,320,320,'snow2')
		self.__zoneAffichage.pack(padx=5, pady=5)
		
		#Partie oû l'on affiche le mot et le résultat final
		self.__labelMot=Label(self,bd=5, relief=SUNKEN, bg='white',font=('Helvetica', 12))
		self.__labelMot.pack(padx=5,pady=5)

		#les buttons du clavier virtuel
		f2=Frame(self)
		f2.pack(side=TOP,padx=5,pady=5)
		self.__buttons = []
		for i in range(26):
			l=chr(ord('A')+i)
			self.__buttons.append(MonButton(f2,self,l,4))
			self.__buttons[i].config(command=self.__buttons[i].cliquer)

		# Affichage du clavier
		for i in range(3):
			for j in range(7):
				self.__buttons[j+7*i].grid(padx=1,pady=1,row=i,column=j)

		for i in range(1):
			for  j in range(5):
				self.__buttons[21+j].grid(padx=1,pady=1,row=4,column=j+1)

		self.chargerMots()
		self.newPartie()

	def newPartie(self):
		self.effacer() # on efface le canvas
		self.__mot=self.nouveauMot()
		print(self.__mot)
		self.__motAffiche=len(self.__mot)*'*'
		self.__labelMot.config(text='Mot: '+self.__motAffiche)
		self.__nbManques=0
		self.__nbGagne=0
		self.__lesmots=len(self.__mot)*['*']
		for b in self.__buttons:   #activation de tous les boutons du clavier virtuel
			b.config(state=NORMAL)

	def chargerMots(self):
		fich=open('mots.txt','r')
		contenu=fich.read()
		self.__mots=contenu.split('\n')
		fich.close()

	def nouveauMot(self):
		return self.__mots[randint(0,len(self.__mots))]

	def traitement(self,letr):
		cpt=0
		for i in range(0,len(self.__mot)):
			if self.__mot[i]==letr:
				self.__lesmots[i]=letr
				cpt+=1
				self.__nbGagne+=1
		if cpt==0:
			self.__nbManques+=1
			self.afficheElement(self.__nbManques)
			#tester si fin
			if self.__nbManques==10:
				self.finPartie(False)
		else:
			self.__labelMot.config(text='Mot: '+''.join(self.__lesmots))
			if self.__nbGagne==len(self.__mot):
				self.finPartie(True)
	
		"""if letr not in self.__mot:
			self.__nbManques+=1
			self.afficheElement(self.__nbManques)
			if self.__nbManques==10:
				self.finPartie(False)
		else:
			cpt=0
			lettres=list(self.__motAffiche)
			for i in range(len(self.__mot)):
				if self.__mot[i]==letr:
					lettres[i]==letr
					self.__motAffiche=''.join(lettres)
					self.__labelMot.config(text='Mot: '+letr)
					#test si fin
					if self.__nbManques==10:
						self.finPartie(True)"""

	def finPartie(self,booleen):
		if booleen:
			message=self.__mot+" - Bravo! Vous avez gagné."
		else:
			message="Vous avez perdu! Le mot était: "+self.__mot
		self.__labelMot.config(text=message)
		#on desactive le clavier
		for but in self.__buttons:
			but.config(state=DISABLED)

	def afficheElement(self,nb):
		self.__zoneAffichage.afficherElement(nb)

	def effacer(self):
		""" Efface la zone graphique """
		self.__zoneAffichage.delete(ALL)
		
if __name__ == '__main__':
# Création de la fenêtre principale
	fen = FenPrincipale()
	fen.mainloop()
