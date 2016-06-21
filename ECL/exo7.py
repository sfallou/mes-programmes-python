# -*- coding: utf-8 -*-

def Convertir(S):
	if S.isdigit()==True:
		return int(S)
	else:
		return "Impossible de cconvertir cette chaine"


if __name__=="__main__":
	print(Convertir("111111222hy"))