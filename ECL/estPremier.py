# -*- coding: utf-8 -*-
import math
def estPremier(N):
	res=True
	for i in range(2,N-1):
		if N%i==0:
			res=False;
			return res
	return res


if __name__ == '__main__':
	N=int(input("Donner N: "))
	print(estPremier(N))