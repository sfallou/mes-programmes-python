# -*- coding: utf-8 -*-
import math
import diviseurPropre

def estParfait(N):
	res=True
	tab,nb=diviseurPropre.div(N)
	if N!=sum(tab):
		res=False
	return res



N=int(input("Donner N: "))

print(estParfait(N))