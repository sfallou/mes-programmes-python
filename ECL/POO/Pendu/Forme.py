# -*- coding: utf-8 -*-
Couleurs=["black","red","blue","green","yellow"]
from math import *

class Forme:
	def __init__(self,x,y,c):
		self.setCentre(x,y)
		self.setCouleur(c)
		

	def getCentre(self):
		return self.__x,self.__y

	def getCouleur(self):
		return self.__c

	def setCentre(self,x1,y1):
		if x1>=0:
			self.__x=x1
		else:
			self.__x=0
		if y1>=0:
			self.__y=y1
		else:
			self.__y=0

	def setCouleur(self,new_c):
		if new_c in Couleurs:
			self.__c=new_c
		else:
			self.__c=Couleurs[0]

	def deplacement(self,dx,dy):
		self.__x=max(0,self.__x+dx)
		self.__y=max(0,self.__y+dy)
#####################################################

class Rectangle(Forme):
	def __init__(self,x,y,c,l,h):
		Forme.__init__(self,x,y,c)
		if l >= 0:
			self.__l=l
		else:
			self.__l=0
		if h >= 0:
			self.__h=h
		else:
			self.__h=0

	def getDim(self):
		return self.__l,self.__h

	def setDim(self,new_l,new_h):
		if new_l >= 0:
			self.__l=new_l
		else:
			self.__l=0
		if new_h >= 0:
			self.__h=new_h
		else:
			self.__h=0

	def perimetre(self):
		return 2*(self.__l+self.__h)

	def surface(self):
		return (self.__l*self.__h)

	def afficher(self,can):
		x,y=self.getCentre()
		can.create_rectangle(x-self.__l//2,y-self.__h//2,x+self.__l//2,y+self.__h//2,outline='blue',fill=self.getCouleur())

	def selectForme(self,x,y):
		xc,yc=self.getCentre()
		x0=xc-self.__l//2
		y0=yc-self.__h//2
		x1=xc+self.__l//2
		y1=yc+self.__h//2
		if x>=x0 and x<=x1:
			if y>=y0 and y<=y1:
				return 1
		return False
	
	def __str__(self):
		x,y=self.getCentre()
		c=self.getCouleur()
		return 'Rectangle - Centre: ({} {}) | couleur: {} | longueur: {} | hauteur: {} | Surface: {} | Perimètre:{}'.format(x,y,c,self.__l,self.__h,self.surface(),self.perimetre())

#########################################################

class Cercle(Forme):
	def __init__(self,x,y,c,d):
		Forme.__init__(self,x,y,c)
		self.setDim(d)

	def getDim(self):
		return self.__d

	def setDim(self,d1):
		if d1 >= 0:
			self.__d=d1
		else:
			self.__d=0

	def perimetre(self):
		return (pi*(self.__d))

	def surface(self):
		return (pi*(self.__d)*(self.__d))/4

	def afficher(self,can):
		x,y=self.getCentre()
		can.create_oval(x-self.__d//2,y-self.__d//2,x+self.__d//2,y+self.__d//2,outline='blue',fill=self.getCouleur())

	def selectForme(self,x,y):
		xc,yc=self.getCentre()
		x0=xc-self.__d//2
		y0=yc-self.__d//2
		x1=xc+self.__d//2
		y1=yc+self.__d//2
		if x>=x0 and x<=x1:
			if y>=y0 and y<=y1:
				return 2
		return False
			
	def __str__(self):
		x,y=self.getCentre()
		c=self.getCouleur()
		return 'Cercle - Centre: ({} {}) | couleur: {} | Diamètre:{} | Surface: {} | Perimètre:{}'.format(x,y,c,self.__d,self.surface(),self.perimetre())



############################################################

class Carre(Rectangle):
	def __init__(self,x,y,c,l):
		Rectangle.__init__(self,x,y,c,l,l)
		
	def getDim(self):
		l1,l2=Rectangle.getDim(self)
		return l1

	def setDim(self,new_l):
		Rectangle.setDim(self,new_l,new_l)

	def afficher(self,can):
		x,y=self.getCentre()
		l=self.getDim()
		can.create_rectangle(x-l//2,y-l//2,x+l//2,y+l//2,outline='blue',fill=self.getCouleur())

	def selectForme(self,x,y):
		xc,yc=self.getCentre()
		l=self.getDim()
		x0=xc-l//2
		y0=yc-l//2
		x1=xc+l//2
		y1=yc+l//2
		if x>=x0 and x<=x1:
			if y>=y0 and y<=y1:
				return 3
		return False

	def __str__(self):
		x,y=self.getCentre()
		c=self.getCouleur()
		return 'Carré - Centre: ({} {}) | couleur: {} | longueur: {} | Surface: {} | Perimètre:{}'.format(x,y,c,self.getDim(),self.surface(),self.perimetre())


