#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import *
from werkzeug import secure_filename
import os

#fonction de creation d'une matrice de type (n,p)
# avec initialisation d'une valeur X
def creer_matrice(n, p, X) :
  A = n * [None]
  for i in range(n) :
    A[i ] = p * [X]
  return A

def identite(identite,ligne,colonne) :
    i,j=0,0
    while i<ligne :
        matligne = list()
        while j <colonne :
            if i==j :
                matligne.append(1)
            else :
                matligne.append(0)
            j=j+1
        identite.append(matligne)
        i=i+1
        j=0
    return identite
def recherchePivot(matrice,k,ligne) :
    i=k
    while i < ligne:
        if matrice[i][k]!= 0 :
            return i
        i=i+1
    return -1
def permutation(matrice,matId,k,pivot) :
    mat=list()
    mat.append(matrice[k])
    matrice[k] = matrice[pivot]
    matrice[pivot]= mat[0]
    mat=list()
    mat.append(matId[k])
    matId[k] = matId[pivot]
    matId[pivot] =  mat[0]
    return matrice,matId
def elimination(matrice,identite,pivot,ligne,colonne ) :
    i=0
    while i < ligne :
       j=0
       if i!=pivot and matrice[i][pivot]!=0 :
           a=float(matrice[i][pivot])/float(matrice[pivot][pivot])
           while j < colonne:
                matrice[i][j]= matrice[i][j] - (matrice[pivot][j]*a)
                identite[i][j]= identite[i][j] - (identite[pivot][j]* a)
                j+=1
       i=i+1
    return matrice,identite
def remonte(matrice,matId,ligne, colonne ) :
    pivot,i=0,0
    while pivot<ligne :
        b=matrice[pivot][pivot]
        while i<colonne:
            a=matrice[pivot][i]
            d=matId[pivot][i]
            matrice[pivot][i]= float(a) / float(b)
            matId[pivot][i]= float(d) / float(b)
            matId[pivot][i]=format(matId[pivot][i],'.2f')
            i+=1
        pivot+=1
        i=0
    return matrice,matId
def inverser(matrice,ligne,colonne):
    matriceIdentite = list()
    matriceIdentite =identite(matriceIdentite,ligne,colonne)
    k=0
    arret = 1
    while k<ligne and arret == 1 :
        pivot=recherchePivot(matrice,k,ligne)
        if pivot==k :
            matrice,matriceIdentite =elimination(matrice,matriceIdentite,pivot,ligne,colonne)
            k=k+1
        else :
            if pivot==-1 :
                arret = 0
            else :
                matrice,matriceIdentite = permutation(matrice,matriceIdentite,k,pivot)
                pivot = k
                matrice,matriceIdentite =elimination(matrice,matriceIdentite,pivot,ligne,colonne)
                k=k+1
    if arret==1 and matrice[ligne-1][colonne-1]!=0 :
            matrice,matriceIdentite = remonte(matrice,matriceIdentite,ligne,colonne)
    else :
            matriceIdentite.append(-1) 
    return matriceIdentite

#Fonction qui permet de copier une matrice A
#dans une matrice B
def copie_matrice(A) :
  n = len(A)
  B = n * [None]
  for i in range(n) :
    B[i ] = A[i ]
  return B

#Fonction qui renvoit la dimension de la matrice
def dimensions(A) :
  n=len(A)
  p=len(A[0])
  return n,p

"""Fonction qui permute deux colonnes d une matrice"""
def PermCol(M,j,i):
  for k in range(len(M)-1,-1,-1):
    (M[k][j],M[k][i])=(M[k][i],M[k][j])


"""Fonction qui calcule le produit des diagonales"""
def ProdDiag(M):
  j=0
  p=1
  while j<len(M):     
    p=p*M[j][j]
    j+=1  
  return p

"""Fonction qui triangule une matrice carre--triangulaire superieure--"""
def Triangule(M):
  sign=1
  n=len(M) -1
  for i in range(n,0,-1):#A partir de  la derniere jusqua la 2eme ligne 
    for j in range(0,i):#Mij=0 si j<i
      if M[i][j+1] !=0.0:#Si c'est nulle, jai qu'a faire une permutation pour avoir 0
        q=(M[i][j])/(M[i][j+1]) 
        if q!=0.0:#Si c'est nulle, pas besoin de le rendre nulle
          for k in range(n,-1,-1):#A chaque combinaison, c'est les elements de toute la colonne qui doivent changer
            M[k][j]= M[k][j] - q*M[k][j+1]
      else:
        PermCol(M,j+1,j)
        sign=sign*(-1)#le determinant est multipli par -1 si on permute deux colonnes de la matrice
  return M,sign

"""Fonction qui calcule le determinant une matrice carre"""
def determinant(M):
  (Mtriang,sign)=Triangule(M)
  return round(sign*ProdDiag(Mtriang),2)


################ Début ###############################s

app = Flask(__name__)
app.secret_key = 'd66HR8dç"f_-àgjYYic*df'

@app.route('/')
def index():
    return render_template('accueil2.html')

#################################################### Somme ###########################################################

@app.route('/somme/')
def sommeMatrice():
    return render_template('layout.html')

@app.route('/somme/getmatrices/', methods=['GET', 'POST'])
def getMatriceSomme():
    error = None
    if request.method == 'POST':
        if int(request.form['nbreLigne']) < 0 or int(request.form['nbreColonne']) < 0 :
            error = 'Valeur incorrecte'
            return redirect(url_for('sommeMatrice'))
        else:
            m1=int(request.form['nbreLigne'])
            n1=int(request.form['nbreColonne'])
            return render_template('layout1.html',m1=m1,n1=n1)


@app.route('/somme/getmatrices/calculer', methods=['GET', 'POST'])
def calculSomme():
    global Matr1,Matr2
    error = None
    if request.method == 'POST':
        ligne=int(request.form['ligne']) 
        colonne=int(request.form['colonne'])
        Matr1=creer_matrice(ligne,colonne,0)
        Matr2=creer_matrice(ligne,colonne,0)
        for i in range(ligne):
            for j in range(colonne):
                Matr1[i][j]=float(request.form['case1_'+str(i)+''+str(j)])
        for i in range(ligne):
            for j in range(colonne):
                Matr2[i][j]=float(request.form['case2_'+str(i)+''+str(j)])

        resultat = list()
        for i in range(len(Matr1)):
            col = list()
            for j in range(len(Matr2)):
                col.append((Matr1[i][j])+(Matr2[i][j]))
            resultat.append(col)
        return render_template('layout2.html',ligne=ligne,colonne=colonne,resultat=resultat,Matr1=Matr1,Matr2=Matr2)

####################################################### END ###########################################################
####################################################### Produit ######################################################

@app.route('/produit/')
def produitMatrice():
    return render_template('produit.html')

@app.route('/produit/getmatrices/', methods=['GET', 'POST'])
def getMatriceProduit():
    error = None
    if request.method == 'POST':
        if int(request.form['nbreLigne1']) < 0 or int(request.form['nbreColonne1']) < 0  or int(request.form['nbreColonne2']) < 0 :
            error = 'Valeur incorrecte'
            return redirect(url_for('produitMatrice'))
        else:
            m1=int(request.form['nbreLigne1'])
            n1=int(request.form['nbreColonne1'])
            m2=int(request.form['nbreColonne1'])
            n2=int(request.form['nbreColonne2'])
            return render_template('produit1.html',m1=m1,n1=n1,m2=m2,n2=n2)


@app.route('/produit/getmatrices/calculer', methods=['GET', 'POST'])
def calculProduit():
    global A,B
    error = None
    if request.method == 'POST':
        ligne1=int(request.form['ligne1']) 
        colonne1=int(request.form['colonne1'])
        ligne2=int(request.form['colonne1'])
        colonne2=int(request.form['colonne2'])
        A=creer_matrice(ligne1,colonne1,0)
        B=creer_matrice(ligne2,colonne2,0)
        for i in range(ligne1):
            for j in range(colonne1):
                A[i][j]=float(request.form['case1_'+str(i)+''+str(j)])
        for i in range(ligne2):
            for j in range(colonne2):
                B[i][j]=float(request.form['case2_'+str(i)+''+str(j)])
        resultat = list()
        for i in range(ligne1):
            ligne = list()
            for j in range(colonne2):
                element = 0
                for k in range(len(A[0])):
                    element= element+ A[i][k]*B[k][j]
                ligne.append(element)
            resultat.append(ligne)
        return render_template('produit2.html',ligne1=ligne1,colonne1=colonne1,ligne2=ligne2,colonne2=colonne2,resultat=resultat,A=A,B=B)
####################################################### END ###########################################################
####################################################### INVERSE ###########################################################
@app.route('/inverse/')
def inverseMatrice():
    return render_template('inverse.html')

@app.route('/inverse/getmatrice/', methods=['GET', 'POST'])
def getMatriceInverse():
    error = None
    if request.method == 'POST':
        if int(request.form['nbreLigne']) < 0 or int(request.form['nbreColonne']) < 0 :
            error = 'Valeur incorrecte'
            return redirect(url_for('inverseMatrice'))
        else:
            m=int(request.form['nbreLigne'])
            n=int(request.form['nbreColonne'])
            return render_template('inverse1.html',m=m,n=n)


@app.route('/inverse/getmatrice/calculer', methods=['GET', 'POST'])
def calculInverse():
    global M
    error = None
    if request.method == 'POST':
        ligne=int(request.form['ligne']) 
        colonne=int(request.form['colonne'])
        M=creer_matrice(ligne,colonne,0)
        for i in range(ligne):
            for j in range(colonne):
                M[i][j]=float(request.form['case'+str(i)+''+str(j)])

        Mat=M
        resultat = list()
        #resultat=creer_matrice(ligne,colonne,0)
        resultat = inverser(M,ligne,colonne)
        return render_template('inverse2.html',ligne=ligne,colonne=colonne,resultat=resultat,Mat=Mat)

####################################################### END ###########################################################
##################################################### Déterminant #####################################################


@app.route('/determinant/')
def determinantMatrice():
    return render_template('determinant.html')

@app.route('/determinant/getmatrice/', methods=['GET', 'POST'])
def getMatriceDeterminant():
    error = None
    if request.method == 'POST':
        if int(request.form['nbreLigne']) < 0 or int(request.form['nbreColonne']) < 0 :
            error = 'Valeur incorrecte'
            return redirect(url_for('determinantMatrice'))
        else:
            m=int(request.form['nbreLigne'])
            n=int(request.form['nbreColonne'])
            return render_template('determinant1.html',m=m,n=n)


@app.route('/determinant/getmatrice/calculer', methods=['GET', 'POST'])
def calculDeterminant():
    global P
    error = None
    if request.method == 'POST':
        ligne=int(request.form['ligne']) 
        colonne=int(request.form['colonne'])
        P=creer_matrice(ligne,colonne,0)
        for i in range(ligne):
            for j in range(colonne):
                P[i][j]=float(request.form['case'+str(i)+''+str(j)])

        Matrix=P
        #resultat=creer_matrice(ligne,colonne,0)
        res = determinant(P)
        return render_template('determinant2.html',ligne=ligne,colonne=colonne,resultat=res,Mat=Matrix)

####################################################### END ###########################################################


@app.route('/transpose/')
def transposeMatrice():
    return render_template('index.html')

@app.route('/gauss/')
def resolutionGauss():
    return render_template('index.html')

@app.route('/lu/')
def resolutionLU():
    return render_template('index.html')


"""
@app.route('/home/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        if request.form['nbreMatr'] <=0:
            error = 'Il faut entrer un nombre supérieur à 0'
        elif request.form['nbreMatr'] > 2:
            error = 'Il faut entrer un nombre inférieur ou égal à 2'
        else:
	    flash('Bienvenue')
            if request.form['nbreMatr'] == 1:
            	return redirect(url_for('equation'))
	    elif request.form['nbreMatr'] == 2:
		return redirect(url_for('equation'))
    return render_template('login.html', error=error)
"""


if __name__ == '__main__':
    app.run(debug=True)
