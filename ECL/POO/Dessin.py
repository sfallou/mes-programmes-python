# -*- coding: utf-8 -*-

class Dessin:
	def __init__(self):
		self.__formes=[]

	def addForme(self,f):
		self.__formes.append(f)

	def delForme(self,position):
		del(self.__formes[position])


	def printForme(self):
		for f in self.__formes:
			print(f)

	def afficher(self,can):
		for f in self.__formes:
			f.afficher(can)

	def afficherElement(self,can,nb):
		self.__formes[len(self.__formes)-nb].afficher(can)

	def selectForme(self,x,y):
		for f in self.__formes:
			if f.selectForme(x,y)!=False:
				return f.selectForme(x,y)
		return False