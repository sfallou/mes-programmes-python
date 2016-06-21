# -*- coding: utf-8 -*-
import math
import random
echantillon=[random.gauss(16,2) for n in range(100)]
def moyenne(echantillon):
	return sum(echantillon)/100

mu=moyenne(echantillon)
tab=[]
for i in echantillon:
	val=(i-mu)*(i-mu)
	tab.append(val)
var=moyenne(tab)
ecarttype=math.sqrt(var)
print"la variance est egale : ",var," l'ecart-type= ",ecarttype