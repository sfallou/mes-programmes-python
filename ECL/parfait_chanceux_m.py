# -*- coding: utf-8 -*-
import math
import diviseurPropre
def estChanceux(a):
	res=True
	for i in range(1,a):
		if estPremier(a+i+i*i)==False:
			res=False
		break
	return res

def estPremier(N):
	res=True
	for i in range(2,N-1):
		if N%i==0:
			res=False;
			return res
	return res

def estParfait(N):
	res=True
	tab,nb=diviseurPropre.div(N)
	if N!=sum(tab):
		res=False
	return res

def sumDiv(N):
	tab,nb=diviseurPropre.div(N)
	return sum(tab)

if __name__=="__main__":
	parfait=[]
	chanceux=[]
	for i in range(2,1001):
		if estChanceux(i)==True:
			chanceux.append(i)
		if estParfait(i)==True:
			parfait.append(i)
	print("Liste parfait:\n ",parfait)
	print("Liste chanceux:\n ",chanceux)