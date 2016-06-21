# -*- coding: utf-8 -*-
import math
def div(N):
	compt=0;
	tab=[]
	for i in range(1,N):
		if N%i==0:
			tab.append(i)
			compt=compt+1
	return tab,compt

if __name__=="__main__":
	N=int(input("Donner N: "))
	val,nombre=div(N)
	print(val)
	print(nombre)