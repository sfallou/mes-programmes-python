# -*- coding: utf-8 -*-
import math
#a=int(input("Donner le coefficient de a: "))
#b=int(input("Donner le coefficient de b:"))
#c=int(input("Donner le coefficient de c: "))

def quadratique(a,b,c):
	if a==0:
		if b!=0:
			res=-c/b
			print("pas de quadratique: racine simple x= " ,res)
		else:
			print('une blague ! ')
	else:
		delta=b*b-(4*a*c) 
		if delta<0:
			print('pas de racines reelles ')
		else:
			if delta>0:
				x1=(-b+math.sqrt(delta))/(2*a)
				x1=(-b-math.sqrt(delta))/(2*a)
				print('x1=',x1)
				print('x1=',x1)
			else:
				x1=x2=-b/(2*a)
				print ("racine double x1=x2=",x1)
		
if __name__=="__main__":
    quadratique(2,1,1);