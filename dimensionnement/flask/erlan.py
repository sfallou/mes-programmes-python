# -*- coding: utf-8 -*-
#!/usr/lib/python2.7
S	=0
mu	=0
lamda	=0 	
teta 	=0

def Facto(n):
  res=1
  n=n+1
  for i in range(1,n):
    res=res*i
  return res


def Puissance(p,n):
  res=1
  for i in range(n):
    res=res*p
  return res
#------------------------------------ Loi d'Erlang B ----------------------------------------#

#– les clients arrivent selon un processus de Poisson de parametre lamda > 0,
#–le temps de service est une loi exponentielle de parametre mu > 0,
#– il y a s serveurs montes en parallele,
#– il n’y a pas de file d’attente.

#Probabilité de perte
def B(teta,S) :
	somme=0
	num = Puissance(teta,S)/Facto(S)
	for k in range(S+1):
		somme = somme + Puissance(teta,k)/Facto(k)	
	
	return (num/somme)
#Trafic écoulé
def TrafEc(teta,S):
	return (teta*( 1- B(teta,S)))
#-----------------------------------Loi d'Erlang C------------------------------------------#

#Probabilité d'attente
def C(teta,S) :
	somme = 0
	num = Puissance(teta,S)/Facto(S)
	denom =1
	a = (1 - (teta/S)) 
	for i in range(S):
		somme = somme + Puissance(teta,i)/Facto(i)	
	denom = num + (a*somme)
	return (num/denom)

#Nombre moyen de clients en attente
def Q(teta,S):
	num = teta*C(teta,S)
	denom = S - teta
	return num/denom
#Temps moyen d'attente dans la file
def tempMoy(teta,S,lamda):
	num = Q(teta,S)
	a=lamda
	return num/a
#Taux de séjour (attente+service)
def t (teta,S,mu,lamda):
	return (tempMoy(teta,S,lamda) + 1/mu)
