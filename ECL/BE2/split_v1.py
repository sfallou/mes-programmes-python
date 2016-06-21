# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------
@Prog: Algo quadripartition appliqué pour la segmentation d'image |
@Authors: Serigne Fallou NDIAYE  & Jordan N'Guessan Ziahi KONAN   |
@From: Ecole Centrale de Lyon                                     |
-------------------------------------------------------------------
"""
########################## Début du programme split #################################

"""
-----------------------------------------------------------
Importation des bibliothèques utilisées dans ce programme |
-----------------------------------------------------------
"""
from math import *
from PIL import Image
import numpy
import time

"""
---------------------------------------------------------------------------------
 Fonction qui prend en entrée une matrice de pixel px,les coordonnées de la zone |
 et retourne un tableau contenant les pixels de cette zonne                      |
 ---------------------------------------------------------------------------------
 """
def lirePixel(px,x1,x2,y1,y2): #retourne un tableau de tuple de pixel 
	tab=[]
	for i in range(x1,x2+1):
		for j in range(y1,y2+1):
			tab.append(px[i,j])
	return tab

"""
-----------------------------------------------------------------------------------
Fonction qui prend en entrée px,la position (i,j) du pixel et les 3 valeurs de la |
couleur à affecter à ce pixel. Elle retourne px modifié							  |
-----------------------------------------------------------------------------------
"""
def affecterCouleurPixel(px,i,j,c1,c2,c3):
	px[i,j]=c1,c2,c3
	return px

"""
----------------------------------------------------------------------------------------------
Fonction qui prend en entrée px,les coordonnées de la zone à colorier et les 3 valeurs de la |
couleur à affecter à cette région															 |
----------------------------------------------------------------------------------------------
"""
def affecterCouleurRegion(px,x1,x2,y1,y2,c1,c2,c3):
	for i in range(x1,x2+1):
		for j in range(y1,y2+1):
			px[i,j]=c1,c2,c3

"""
------------------------------------------------------------------------------------------
Fonction qui prend en entrée px, et les coordonnées de la zone pour retourner la couleur |
moyenne de cette zone sous forme de tuple (r,v,b)                                        |
------------------------------------------------------------------------------------------
"""
def couleurMoyenne(px,x1,x2,y1,y2):
	tab1=[]
	tab2=[]
	tab3=[]
	for i in range(x1,x2+1):
		for j in range(y1,y2+1):
			tab1.append(px[i,j][0])
			tab2.append(px[i,j][1])
			tab3.append(px[i,j][2])
	return (int(numpy.mean(tab1)),int(numpy.mean(tab2)),int(numpy.mean(tab3)))

"""
------------------------------------------------------------------------------------------
Fonction qui prend en entrée px,les coordonnées de la zone et le seuil pour retourner un |
booléen qui teste si la zone est homogène ou non                                         |
------------------------------------------------------------------------------------------
"""
def esthomogene(px,x1,x2,y1,y2,s):
	tab1=[]
	tab2=[]
	tab3=[]
	for i in range(x1,x2+1):
		for j in range(y1,y2+1):
			tab1.append(px[i,j][0])
			tab2.append(px[i,j][1])
			tab3.append(px[i,j][2])
	return ((sqrt(numpy.var(tab1))+sqrt(numpy.var(tab2))+sqrt(numpy.var(tab3)))/3)<s

"""
------------------------------------------------------------------------------------------
Fonction principale de l'algo qui prend en entrée px,les coordonnées de la zone et le    |
seuil pour découper l'image en zone homogène et la colorie avec la couleur moyenne       |
moyenne de cette zone sous forme de tuple (r,v,b)                                        |
------------------------------------------------------------------------------------------
"""

def quadripartition(px,x1,x2,y1,y2,s):
	if x2-x1<4 or y2-y1<4:
		r,v,b=couleurMoyenne(px,x1,x2,y1,y2)
		affecterCouleurRegion(px,x1,x2,y1,y2,r,v,b)
	else:
		if esthomogene(px,x1,x2,y1,y2,s):
			r,v,b=couleurMoyenne(px,x1,x2,y1,y2)
			affecterCouleurRegion(px,x1,x2,y1,y2,r,v,b)
		else:         
			quadripartition(px,x1,x1 +(x2-x1)//2,y1,y1 +(y2-y1)//2,s)
			quadripartition(px,x1+(x2-x1)//2,x2,y1,y1 +(y2-y1)//2,s)
			quadripartition(px,x1,x1+(x2-x1)//2,y1 +(y2-y1)//2,y2,s)
			quadripartition(px,x1+(x2-x1)//2,x2,y1 +(y2-y1)//2,y2,s)

########################## Fin du programme split #################################

########################## Début du programme merge #################################	



########################## Fin du programme merge #################################	

"""
------------------------------------------------------------------------------------------
	                       execution du programme principale                             |
------------------------------------------------------------------------------------------
"""

if __name__=="__main__":
	image="Image8.bmp"
	im=Image.open(image)
	px=im.load()
	x2,y2=im.size
	x1=0
	y1=0
	s=10
	t0 = time.clock()
	quadripartition(px,x1,x2-1,y1,y2-1,s)
	t1 = time.clock()
	print("temps d'execution en seconde: ",t1-t0)
	im.show()