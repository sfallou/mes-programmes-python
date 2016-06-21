# -*- coding: utf-8 -*-
def empile(p,a):
	p.append(a)

def depile(p):
	try :
		del p[0]
		return p
	except:
		print("La pile est vide!")
		return None

def top(p):
	try :
		return p[0]
	except :
		print("La pile est vide!")
		return None

def est_vide(p):
	return p==[]

print(" Pile initiale ".center(50, '-'))
lifo=[]
print ("Empilage".center(50, '-'))
empile(lifo,5)
empile(lifo,8)
empile (lifo,11)
print("lifo:", lifo,'\n')
#rien=input("Entree")
print("Empilage".center(50, '-'))
empile(lifo,11)
print("lifo : ",lifo, '\n ')
#rien=input("Entree")
print("Depilages".center(50,'−'))
for i in range(5): #du premier au 5e (d’indice 0 à l’indice 4)
	depile(lifo)
	print("lifo : " ,lifo)

