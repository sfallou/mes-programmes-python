# -*- coding: utf-8 -*-
import math
N=int(input("Donner N: "))
res=0
for i in range(0,N):
	res+=1/math.factorial(i)
print(res)
