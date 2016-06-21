# -*- coding: utf-8 -*-

def purifie(L):
	P=[]
	for i in L:
		if i not in P:
			P.append(i)	
	return P


if __name__=="__main__":
	L=[1,2,17,1,3,4,5,6,5,5,4,33,4]
	print ("La liste initiale est:")
	print (L)
	print ("La liste purifiée avec Set est:")
	print (set(L))
	print ("La liste purifiée avec ma fonction est:")
	print (purifie(L))
