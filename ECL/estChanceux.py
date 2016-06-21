# -*- coding: utf-8 -*-
import math
import estPremier

"""def estChanceux(a):
	res=True
	for i in range(1,a):
		if estPremier.estPremier(a+i+i*i)==False:
			res=False
		break
	return res"""

def estChanceux(a):
	n=0
	res=True
	while n<(a-1) and res==True:
		res=estPremier.estPremier(a+n+n*n)
		n=n+1
	return res

if __name__=="__main__":
	a=int(input("Donner a: "))
	print(estChanceux(a))