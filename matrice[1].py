#!/usr/bin/python3

"""Ceci est un ensemble de fonction permettant de calculer la somme et
le produit d'un ensemble de matrice  passees en parametre glade"""

class matrice(object):

    def __init__(self, m=0, n=0):
        self.m=m
        self.n=n
        self.C=[]
        for i in range(m):
            c=[]
            for j in range(n):
                c.append(0)
            self.C.append(c)


    def saisi(self):
        for i in range(self.m):
            for j in range(self.n):
                try:
                    print("entrer lelement [",i,"][",j,"] ")
                    self.C[i][j]=int(input())
                except:
                    print("erreur sur la saisi ressayer")
    
    def affichage(Matrice):
       "Affichage de la matrice"
       chaine = ""
       for x in Matrice:
         chaine = chaine + str(x) + '\n'
       print(chaine)

    
    def somme(A, B):
        if(B.m!=A.m):
            return 0
        if(B.n!=A.n):
            return 0
        C=[]
        j=0
        for i in range(m):
            c=[]
            for j in range(n):
                c.append(0)
            C.append(c)
        for i in range(m):
            C[i][j]=0
            for j in range(n):
                C[i][j]=A.C[i][j]+B.C[i][j]
        return C


    def produit(A, B):
        C=[]
        j=0
        for i in range(m):
            c=[]
            for j in range(n):
                c.append(0)
            C.append(c)
        if(A.n!=B.m):
            return 0
        for i in range(A.m):
            for j in range(B.n):
                C[i][j]=0
                for k in range(A.n):
                    C[i][j]=C[i][j]+A.C[i][k]*B.C[k][j]

        return C

"""class matriceCarre(matrice):

    def __init__(self, n=0):
        self.m=n
        self.n=n
   """     
        

if __name__=="__main__":
    print("saisie du nombre d'elements des matrices ")
    try:
        
        m1=int(input("entrez le nombre de ligne de la matrice 1 :"))
        n1=int(input("entrez le nombre de colonne  de la matrice 1:"))
        m2=int(input("entrez le nombre de ligne de la matrice 2 :"))
        n2=int(input("entrez le nombre de colonne  de la matrice 2:"))
    except:
        print("erreur sur la saisi ressayer")

    matriceA=matrice(m1, n1)
    matriceB=matrice(m2, n2)
    print("saisi de la matrice 1 \n")
    print("---------------------")
    matriceA.saisi()
    print("saisi de la matrice 2 \n")
    print("---------------------")
    matriceB.saisi()
    print("le produit des deux matrices est : "
    
    print(matrice.produit(matriceA, matriceB))
    #affichage(res)
    """chaine = ""
    for x in resul:
       chaine = chaine + str(x) + '\n'
       print(chaine)"""
    
    print("---------------------")
    #print("la somme des deux matrices est : ",matrice.somme(matriceA, matriceB))
    
