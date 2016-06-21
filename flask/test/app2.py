#!/usr/bin/env python
# -*- coding:utf-8 -*-
from MesFonctionsMaths import *
from flask import *
from werkzeug import secure_filename
import os
import pickle
import time
import copy

################ Début ###############################s


app = Flask(__name__)
app.secret_key = 'd66HR8dç"f_-àgjYYic*df'




@app.route('/')
def index():
    
    pseudo=pseudo.upper()
    return render_template('accueil2.html')

####################################################### INVERSE ###########################################################
@app.route('/inverse/')
def inverseMatrice():
    
    return render_template('inverse.html')

@app.route('/inverse/getmatrice/', methods=['GET', 'POST'])
def getMatriceInverse():
    
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
        det = Determinant(M)
        if det!=0:
            resultat = inverser(M,n,n)
        else:
            resultat="NON! Impossible d'inverser cette matrice. Son determinant est null"

        return render_template('inverse2.html',n=n,resultat=resultat,Mat=Mat)

####################################################### END ###########################################################


####################################### Résolution des equations ##############################################
######## Récuperation des differents membres ####################

@app.route('/solveur/')
def solveur():
    return render_template('solveur.html')


@app.route('/solveur/getmatrice/', methods=['GET', 'POST'])
def getEquation():
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
            Monfichier="matrice"
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
    
    Monfichier="matrice"
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
    
    Monfichier="matrice"
    result=""
    tab=list()
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
    return render_template('resultatCholesky.html',Matrice=Matrice,vecteur=vecteur,taille=taille,resultat=tab,temps=t,B=B)

################################################ LU ##########################################

@app.route('/lu/')
def resolutionLU():
    
    Monfichier="matrice"
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
    app.run(debug=True)
