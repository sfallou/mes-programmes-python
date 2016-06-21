# -*- coding: utf-8 -*-
import math
import random
N=100
echantillon=[random.gauss(16,2) for n in range(N)]
def moyenne(echantillon):
	return sum(echantillon)/100

mu=moyenne(echantillon)
tab=[]
for i in echantillon:
	val=i*i
	tab.append(val)
"""print(echantillon)
print("-------------")
print(tab)"""
res=0
for i in range(N):
	res=res+tab[i]
#print(res)
var=(res/N)-(mu*mu)
ecarttype=math.sqrt(var)
print"la variance est egale : ",var," l'ecart-type= ", ecarttype