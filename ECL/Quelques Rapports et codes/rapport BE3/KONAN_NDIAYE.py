# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------
@Authors: Serigne Fallou NDIAYE  & Jordan N'Guessan Ziahi KONAN   |
@From: Ecole Centrale de Lyon                                     |
@Prog: Probleme de la monnaie rendue                              |
@Date: 24 - 03 - 2016                                             |	
-------------------------------------------------------------------
"""
########################## Début du programme  #################################

"""
-----------------------------------------------------------
Importation des bibliothèques utilisées dans ce programme |
-----------------------------------------------------------
"""
from math import *
import numpy


"""
 --------------------------------------------------------------------------------
 Fonction qui implémente l'Algoritme gloutonne                                  |
 --------------------------------------------------------------------------------
"""
def monnaie_gloutonne(S,M):
    Mr=M # Monnaie restante
    T=[0]*len(S) # création d'un vecteur de même dimension que S
    for i in range(len(S)-1,-1,-1): 
        if S[i]<=Mr and S[i]!=0: #recherche de la valeur la plus grande de S proche de M
            Ti=Mr//S[i]
            T[i]=Ti
            Mr= Mr%S[i]
        else: 
            T[i]=0
            if Mr==0:
                break 
    return sum(T),T

"""
 --------------------------------------------------------------------------------
 Fonction qui implémente l'Algoritme PrD                                        |
 --------------------------------------------------------------------------------
"""

def monnaie_optimale(S,M):
    mat=numpy.zeros([len(S),M+1]) # création de la matrice
    for i in range(0,len(S)): 
        for m in range(0,M+1):
            if m==0:
                mat[i][m]=0
            elif i==0:
                mat[i][m]=float('Infinity')
            else:
                if m-S[i]>=0:
                	val1=1+mat[i][m-S[i]]
                else:
                	val1=float('Infinity')
                if i>=1:
                	val2=mat[i-1][m]
                else:
                	val2=float('Infinity')
                mat[i][m]=min(val1,val2)
    return int(mat[len(S)-1][M])
########################## Fin du programme #################################

"""
---------------------------------------------------------------------------
                        Programme Principale                              |
---------------------------------------------------------------------------
"""	

if __name__=="__main__":
    S=[0,1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]
    M=23665
    print("Données du problème")
    print("S:",S)
    print("M=",M)
    print("----------------- Gloutonne ----------------")
    print("Q:",monnaie_gloutonne(S,M)[0])
    print("T:",monnaie_gloutonne(S,M)[1])
    print("----------------- Programmation Dynamique ---------------")
    print("le nombre de pièces nécessaire: ",monnaie_optimale(S,M))