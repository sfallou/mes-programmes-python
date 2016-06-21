#!/usr/bin/env python
# -*- coding:utf-8 -*-
from MesFonctionsMaths import *
from Fonction import *
from flask import *
from werkzeug import secure_filename
import os
import pickle
import time
import copy

################ Début ###############################s


app = Flask(__name__)
app.secret_key = 'd66HR8dç"f_-àgjYYic*df'
users=['sfallou','oury','bass','sine','kama']

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def validLogin():
    error = None
    if request.method == 'POST':
        if request.form['username'] in users:
            session['logged_in'] = True
            session['pseudo']=request.form['username']
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    #flash('You were logged out')
    return redirect(url_for('login'))


@app.route('/index/')
def index():
    if not session.get('logged_in'):
        abort(401)
    pseudo=session.get('pseudo')
    pseudo=pseudo.upper()
    return render_template('accueil2.html',pseudo=pseudo)

#################################################### Somme ###########################################################

@app.route('/somme/')
def sommeMatrice():
    if not session.get('logged_in'):
        abort(401)
    return render_template('layout.html')

@app.route('/somme/getmatrices/', methods=['GET', 'POST'])
def getMatriceSomme():
    if not session.get('logged_in'):
        abort(401)
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
    if not session.get('logged_in'):
        abort(401)
    #global Matr1,Matr2
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
    if not session.get('logged_in'):
        abort(401)
    return render_template('produit.html')

@app.route('/produit/getmatrices/', methods=['GET', 'POST'])
def getMatriceProduit():
    if not session.get('logged_in'):
        abort(401)
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
    if not session.get('logged_in'):
        abort(401)
    #global A,B
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
    if not session.get('logged_in'):
        abort(401)
    return render_template('inverse.html')

@app.route('/inverse/getmatrice/', methods=['GET', 'POST'])
def getMatriceInverse():
    if not session.get('logged_in'):
        abort(401)
    error = None
    if request.method == 'POST':
        if int(request.form['taille']) < 0 :
            error = 'Valeur incorrecte'
            return redirect(url_for('inverseMatrice'))
        else:
            n=int(request.form['taille'])
            return render_template('inverse1.html',n=n)


@app.route('/inverse/getmatrice/calculer', methods=['GET', 'POST'])
def calculInverse():
    if not session.get('logged_in'):
        abort(401)
    #global M
    error = None
    if request.method == 'POST':
        n=int(request.form['n']) 
        M=creer_matrice(n,n,0)
        Mat=creer_matrice(n,n,0)
        for i in range(n):
            for j in range(n):
                M[i][j]=float(request.form['case'+str(i)+''+str(j)])
                Mat[i][j]=float(request.form['case'+str(i)+''+str(j)])

        resultat = list()
        #resultat=creer_matrice(ligne,colonne,0)
        Matr=copy.deepcopy(M)
        det = Determinant(Matr)
        if det!=0:
            resultat = inversion(M)
        else:
            resultat="NON! Impossible d'inverser cette matrice. Son determinant est null"

        return render_template('inverse2.html',n=n,resultat=resultat,Mat=Mat)

####################################################### END ###########################################################
####################################################### Coefficients du polynome caracteristique###############################
@app.route('/vecteurpropre/')
def coeffMatrice():
    if not session.get('logged_in'):
        abort(401)
    return render_template('coeffMatrice.html')

@app.route('/vecteurpropre/getmatrice/', methods=['GET', 'POST'])
def getMatriceVecteur():
    if not session.get('logged_in'):
        abort(401)
    error = None
    if request.method == 'POST':
        if int(request.form['taille']) < 0 :
            error = 'Valeur incorrecte'
            return redirect(url_for('coeffMatrice'))
        else:
            n=int(request.form['taille'])
            return render_template('coeffMatrice1.html',n=n)


@app.route('/vecteurpropre/getmatrice/calculer', methods=['GET', 'POST'])
def calculCoeff():
    if not session.get('logged_in'):
        abort(401)
    #global M
    error = None
    if request.method == 'POST':
        n=int(request.form['n']) 
        M=creer_matrice(n,n,0)
        Mat=creer_matrice(n,n,0)
        for i in range(n):
            for j in range(n):
                M[i][j]=float(request.form['case'+str(i)+''+str(j)])
                Mat[i][j]=float(request.form['case'+str(i)+''+str(j)])

        resultat = list()
        #resultat=creer_matrice(ligne,colonne,0)
        resultat=PolyCarac(M)
        return render_template('coeffMatrice2.html',n=n,resultat=resultat,Mat=Mat)

####################################################### END ###########################################################

##################################################### Déterminant #####################################################
@app.route('/determinant/')
def determinantMatrice():
    if not session.get('logged_in'):
        abort(401)
    return render_template('determinant.html')

@app.route('/determinant/getmatrice/', methods=['GET', 'POST'])
def getMatriceDeterminant():
    if not session.get('logged_in'):
        abort(401)
    error = None
    if request.method == 'POST':
        if int(request.form['taille']) < 0 :
            error = 'Valeur incorrecte'
            return redirect(url_for('determinantMatrice'))
        else:
            n=int(request.form['taille'])
            return render_template('determinant1.html',n=n)


@app.route('/determinant/getmatrice/calculer', methods=['GET', 'POST'])
def calculDeterminant():
    if not session.get('logged_in'):
        abort(401)
    #global M
    error = None
    if request.method == 'POST':
        n=int(request.form['n']) 
        M=creer_matrice(n,n,0)
        Mat=creer_matrice(n,n,0)
        for i in range(n):
            for j in range(n):
                M[i][j]=float(request.form['case'+str(i)+''+str(j)])
                Mat[i][j]=float(request.form['case'+str(i)+''+str(j)])

        #resultat=creer_matrice(ligne,colonne,0)
        resultat = Determinant(M)
        return render_template('determinant2.html',n=n,resultat=resultat,Mat=Mat)



####################################################### END ###########################################################


####################################### Résolution des equations ##############################################
######## Récuperation des differents membres ####################

@app.route('/solveur/')
def solveur():
    if not session.get('logged_in'):
        abort(401)
    return render_template('solveur.html')


@app.route('/solveur/getmatrice/', methods=['GET', 'POST'])
def getEquation():
    if not session.get('logged_in'):
        abort(401)
    error = None
    if request.method == 'POST':
        if int(request.form['taille']) < 0 :
            error = 'Valeur incorrecte'
            return redirect(url_for('solveur'))
        else:
           n=int(request.form['taille'])
           return render_template('solveur1.html',n=n)

@app.route('/solveur/recuperationEquation/', methods=['GET', 'POST'])
def recupEquation():
    if not session.get('logged_in'):
        abort(401)
    #global Matrice,vecteur,n
    error = None
    if request.method == 'POST':
        taille=int(request.form['taille'])
        n=taille 
        Matrice=creer_matrice(taille,taille,0)
        vecteur=CreerListe(taille)
        for i in range(taille):
            for j in range(taille):
                Matrice[i][j]=float(request.form['case1_'+str(i)+''+str(j)])
        for i in range(taille):
            vecteur[i]=float(request.form['case2_'+str(i)])
        try:
            Monfichier=session.get('pseudo')
            Fichier = open(Monfichier,'wb')
            pickle.dump(Matrice, Fichier)
            pickle.dump(vecteur, Fichier)
            pickle.dump(taille, Fichier)
            Fichier.close()
        except:
            error="Impossible de creer le fichier"
        return render_template('solveur2.html',Matrice=Matrice,vecteur=vecteur,taille=taille)

################################################    END #######################################

################################################## GAUSS ###########################################
@app.route('/gauss/')
def resolutionGauss():
    if not session.get('logged_in'):
        abort(401)
    #récupération des élements de l'équation dans le fichier
    #global A,b,n
    Monfichier=session.get('pseudo')
    result=""
    tab=list()
    try:
        f=open(Monfichier,'rb')
        A=pickle.load(f)
        b=pickle.load(f)
        n=pickle.load(f)
        f.close()
        Matrice=A
        vecteur=b
        taille=n
        x,temps=solveSystGauss(A,b)

        for i in range(n):
            result = "\n X{} = {}\n".format(i+1, x[i])
            tab.append(result) 
    except :
        result+="Erreur Fichier"
    return render_template('resultatGauss.html',Matrice=Matrice,vecteur=vecteur,taille=taille,resultat=tab,temps=temps)

############################################ Cholesky ########################################

@app.route('/cholesky/')
def resolutionCholesky():
    if not session.get('logged_in'):
        abort(401)
    #récupération des élements de l'équation dans le fichier
    #global A,b,n
    Monfichier=session.get('pseudo')
    result=""
    tab=list()
    x=0
    try:
        fi=open(Monfichier,'rb')
        A=pickle.load(fi)
        b=pickle.load(fi)
        n=pickle.load(fi)
        fi.close()
        Matrice=A
        vecteur=b
        taille=n
        x,B,t=solveSystCholesky(A,b)

        for i in range(n):
            result = "\n X{} = {}\n".format(i+1, x[i])
            tab.append(result) 
    except :
        result+="Erreur Fichier"
    if x!=0:
        return render_template('resultatCholesky.html',Matrice=Matrice,vecteur=vecteur,taille=taille,resultat=tab,B=B)
    else:
        B="NON"
        tab="NON"
        return render_template('resultatCholesky.html',Matrice=Matrice,vecteur=vecteur,taille=taille,resultat=tab,B=B)


################################################ LU ##########################################

@app.route('/lu/')
def resolutionLU():
    if not session.get('logged_in'):
        abort(401)
    #récupération des élements de l'équation dans le fichier
    #global A,b,n
    Monfichier=session.get('pseudo')
    result=""
    tab=list()
    try:
        f=open(Monfichier,'rb')
        A=pickle.load(f)
        b=pickle.load(f)
        n=pickle.load(f)
        f.close()
        Matrice=copy.deepcopy(A)
        vecteur=copy.deepcopy(b)
        taille=copy.deepcopy(n)
        x,L,t=solveSystLU(A,b)
      
        if x!=0:
            for i in range(n):
                result = "\n X{} = {}\n".format(i+1, x[i])
                tab.append(result)
        else:
            tab="Ce systeme", "ne peut pas", "etre resolu par la methode LU" 
    except :
        result+="Erreur Fichier"
    return render_template('resultatLU.html',Matrice=Matrice,vecteur=vecteur,taille=taille,resultat=tab,temps=t,L=L,U=0)

######################################### Appel du programme #################################

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
