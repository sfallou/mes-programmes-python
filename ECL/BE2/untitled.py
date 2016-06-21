# -*- coding: utf-8 -*-
from math import *
from PIL import Image
import numpy

"""def readPixel(px): #retourne un tableau de tuple de pixel contenue dans le premier quart
	w,h=im.size
	tab=[]
	for i in range(w//2):
		for j in range(h//2):
			tab.append(px[i,j])
	return tab"""

def lirePixel(px,l,c,w,h): #retourne un tableau de tuple de pixel 
	tab=[]
	for i in range(l,w):
		for j in range(c,h):
			tab.append(px[i,j])
	return tab


def affecterCouleurPixel(px,i,j,c1,c2,c3):
	px[i,j]=c1,c2,c3
	return px

def affecterCouleurRegion(px,l,c,w,h,c1,c2,c3):
	for i in range(l,w):
		for j in range(c,h):
			px[i,j]=c1,c2,c3
	return px

def ecartype(tab,):
	mu=moyenne(echantillon)
	tab=[]
	for i in echantillon:
		val=i*i
		tab.append(val)
	res=0
	for i in range(len(echantillon)):
		res=res+tab[i]
	var=(res/len(echantillon))-(mu*mu)
	ecarttype=math.sqrt(var)

"""def esthomogene(px,l,c,w,h,s):
	rm=0
	vm=0
	bm=0
	varr=0
	varv=0
	varb=0
	for i in range(l,w):
		for j in range(c,h):
			rm=rm+px[i,j][0]
			vm=vm+px[i,j][1]
			bm=bm+px[i,j][2]
	rm=rm/(w*h)
	vm=vm/(w*h)
	bm=bm/(w*h)
	for i in range(l,w):
		for j in range(c,h):
			varr=(varr+px[i,j][0]-rm)*(varr+px[i,j][0]-rm)
			varv=(varv+px[i,j][1]-vm)*(varv+px[i,j][1]-vm)
			varb=(varb+px[i,j][2]-bm)*(varb+px[i,j][2]-bm)
	varr=varr/(w*h)
	varv=varv/(w*h)
	varb=varb/(w*h)

	return (sqrt(varr),sqrt(varv),sqrt(varb))"""

def coulerMoyenne(px,l,c,w,h):
	tab1=[]
	tab2=[]
	tab3=[]
	for i in range(l,w):
		for j in range(c,h):
			tab1.append(px[i,j][0])
			tab2.append(px[i,j][1])
			tab3.append(px[i,j][2])
	return (int(numpy.mean(tab1)),int(numpy.mean(tab2)),int(numpy.mean(tab3)))


def esthomogene(px,l,c,w,h,s):
	tab1=[]
	tab2=[]
	tab3=[]
	for i in range(l,w):
		for j in range(c,h):
			tab1.append(px[i,j][0])
			tab2.append(px[i,j][1])
			tab3.append(px[i,j][2])
	return ((numpy.var(tab1)+numpy.var(tab2)+numpy.var(tab3))/3)<s

def quadripartition(px,l,c,w,h,s):
	if esthomogene(px,l,c,w,h,s)==True:
		r,v,b=coulerMoyenne(px,l,c,w,h)
		px=affecterCouleurRegion(px,l,c,w,h,r,v,b)
		return px
		
	else:
		quadripartition(px,l,c,w//2,h//2,s)
		quadripartition(px,w//2,c,w,h//2,s)
		quadripartition(px,l,h//2,w//2,h,s)
		quadripartition(px,w//2,c//2,w,h,s)



#################################


if __name__=="__main__":
	image="Image8.bmp"
	im=Image.open(image)
	px=im.load()
	w,h=im.size
	l=0
	c=0
	s=10
	#print(lirePixel(px,l,c,5,5))	
	#print(affecterCouleurRegion(px,l,c,w,h,50,50,50))
	#print(esthomogene(px,l,c,5,5,5))
	#print(coulerMoyenne(px,l,c,5,5))
	px=quadripartition(px,850,1000,w,h,s)
	im.show()