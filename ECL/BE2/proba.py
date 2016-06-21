# -*- coding: utf-8 -*-
import math
import random


def moyenne(echantillon):
	return sum(echantillon)/len(echantillon)

def ecartype(echantillon):
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