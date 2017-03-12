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
from adjacence import *
from effaceDoublon import *

"""
-----------------------------------------------------------
Déclaration de quelques variables globales				  |
-----------------------------------------------------------
"""
L_regions=[]

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
booléen qui teste si la zone est homogène ou non et la liste L_regions après l'avoir     |
modifié ou non en fonction du test                                                       |
------------------------------------------------------------------------------------------
"""
def esthomogene(px,x1,x2,y1,y2,s):
	global L_regions
	region=[] # je considère qu'une région est définie par (x1,x2,y1,y2,r,v,b) 
	tab1=[]
	tab2=[]
	tab3=[]
	for i in range(x1,x2+1):
		for j in range(y1,y2+1):
			tab1.append(px[i,j][0])
			tab2.append(px[i,j][1])
			tab3.append(px[i,j][2])
	booleen=((sqrt(numpy.var(tab1))+sqrt(numpy.var(tab2))+sqrt(numpy.var(tab3)))/3)<s
	if booleen:
		r,v,b=couleurMoyenne(px,x1,x2,y1,y2)
		if L_regions==[]:
			region=[0,x1,x2,y1,y2,r,v,b]
		else:
			region=[L_regions[-1][0]+1,x1,x2,y1,y2,r,v,b]
		L_regions.append(region)
	return booleen,L_regions
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
		if esthomogene(px,x1,x2,y1,y2,s)[0]:
			r,v,b=couleurMoyenne(px,x1,x2,y1,y2)
			affecterCouleurRegion(px,x1,x2,y1,y2,r,v,b)
		else:         
			quadripartition(px,x1,x1 +(x2-x1)//2,y1,y1 +(y2-y1)//2,s)
			quadripartition(px,x1+(x2-x1)//2,x2,y1,y1 +(y2-y1)//2,s)
			quadripartition(px,x1,x1+(x2-x1)//2,y1 +(y2-y1)//2,y2,s)
			quadripartition(px,x1+(x2-x1)//2,x2,y1 +(y2-y1)//2,y2,s)

########################## Fin du programme split #################################

########################## Début du programme merge #################################

"""
------------------------------------------------------------------------------------------
Fonction estAdjacente qui prend en entrée 2 régions  pour tester si elles sont           |
adjacentes ou pas                  														 |
------------------------------------------------------------------------------------------
"""
def estAdjacente(L1,L2):
	#je transforme chaque région en 4 segments et je teste si un des segments de L1 intersecte un segment de L2
	
	#segment L1
	L1_segement1=[[L1[1],L1[3]],[L1[2],L1[3]]]
	L1_segement2=[[L1[2],L1[3]],[L1[2],L1[4]]]
	L1_segement3=[[L1[2],L1[4]],[L1[1],L1[3]]]
	L1_segement4=[[L1[1],L1[3]],[L1[1],L1[3]]]
	#segment L2
	L2_segement1=[[L2[1],L2[3]],[L2[2],L2[3]]]
	L2_segement2=[[L2[2],L2[3]],[L2[2],L2[4]]]
	L2_segement3=[[L2[2],L2[4]],[L2[1],L2[3]]]
	L2_segement4=[[L2[1],L2[3]],[L2[1],L2[3]]]
	if segment_intersect(L1_segement1[0],L1_segement1[1],L2_segement3[0],L2_segement3[1]):
		return True
	elif segment_intersect(L1_segement2[0],L1_segement2[1],L2_segement4[0],L2_segement4[1]):
		return True
	elif segment_intersect(L1_segement3[0],L1_segement3[1],L2_segement1[0],L2_segement1[1]):
		return True
	elif segment_intersect(L1_segement4[0],L1_segement4[1],L2_segement2[0],L2_segement2[1]):
		return True
	else:
		return False


"""
------------------------------------------------------------------------------------------
Fonction ListeAdjacent qui prend en entrée une L_région et un indice i pour trouver toutes|
les régions adjacentes             														  |
------------------------------------------------------------------------------------------
"""
def ListeAdjacent(L,i):
	ListeAdj=[]
	region=L[i]
	ListeAdj.append(i)
	for j in L:
		if estAdjacente(j,region) and L.index(j) not in ListeAdj:
			ListeAdj.append(L.index(j))
	return ListeAdj

"""
------------------------------------------------------------------------------------------
Fonction RAL qui prend en entrée une L_région pour retourner la "Region Ajacency List"    |
------------------------------------------------------------------------------------------
"""
def RAL(L):
	ral = []
	for region in L:
		ral.append(ListeAdjacent(L,region[0]))
	return ral

"""
------------------------------------------------------------------------------------------
Fonction estRegion_homogene qui prend en entrée 2 régions et un seuil pour verifier si   |
les deux régions sont homogènes ou pas                                                   |
------------------------------------------------------------------------------------------
"""
def estRegion_homogene(L1,L2,seuil):
	coul1 = [L1[5],L1[6],L1[7]]
	coul2 = [L2[5],L2[6],L2[7]]
	return ((sqrt(numpy.var(coul1))+sqrt(numpy.var(coul2)))/2)<seuil


"""
------------------------------------------------------------------------------------------
Fonction Fusion qui prend en entrée px,L_regions et un seuil faire le merge              |
------------------------------------------------------------------------------------------
"""
def fusion(px,x1,x2,y1,y2,seuil):
	ok=0
	notok=0
	L=esthomogene(px,x1,x2,y1,y2,seuil)[1] #on récupère L_regions
	ral=RAL(L)
	for i in range(len(ral)):
		indiceRegion=ral[i][0]
		for j in range(1,len(ral[i])+1):
			if estRegion_homogene(L[indiceRegion],L[j],seuil) and "D" not in L[j]:
				for k in ral[j]:
					ral[i].append(k)
				ral[i]=purifie(ral[i])
				r1,v1,b1=couleurMoyenne(px,L[indiceRegion][1],L[indiceRegion][2],L[indiceRegion][3],L[indiceRegion][4])
				r2,v2,b2=couleurMoyenne(px,L[j][1],L[j][2],L[j][3],L[j][4])
				r,v,b=(r1+r2)//2,(v1+v2)//2,(b1+b2)//2
				affecterCouleurRegion(px,L[indiceRegion][1],L[indiceRegion][2],L[indiceRegion][3],L[indiceRegion][4],r,v,b)
				affecterCouleurRegion(px,L[j][1],L[j][2],L[j][3],L[j][4],r,v,b)
			ral[j].append("D")



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
	seuil=30
	t0 = time.clock()
	quadripartition(px,x1,x2-1,y1,y2-1,s)
	im.show()
	im.save("resultatSplit.jpg")
	fusion(px,x1,x2-1,y1,y2-1,seuil)
	im.show()
	im.save("resultatMerge.jpg")
	t1 = time.clock()
	print("temps d'execution en seconde: ",t1-t0)
	#im.show()
	#L=esthomogene(px,x1,x2-1,y1,y2-1,s)[1]
	#print(RAL(L))
