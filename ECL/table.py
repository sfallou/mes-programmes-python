# -*- coding: utf-8 -*-
import math
N=int(input("Donner N: "))
"""Tab=[]
col1=[]
col2=[]
col3=[]
for i in range(N):
	col1.append(i)
	col2.append(i*i)
	col3.append(math.sqrt(i))
Tab.append(col1)
Tab.append(col2)
Tab.append(col3)
print Tab"""
for x in range(1,N):
	print('{} {} {}'.format(x,x*x,math.sqrt(x)))
