#!/usr/bin/python2.7
# -*-coding:Utf-8 -*
from flask import *
from werkzeug import secure_filename
import os
import pickle
import time
import copy
from erlan import *
####### Les Fonctions ###################

global lamda
global mu
global nb

def factoriel(n):
	res=1
	n=n+1
	for i in range(1,n):
		res=res*i
	return res


def puissance(p,n):
	res=1
	for i in range(n):
		res=res*p
	return res



def calcul_po():  #
	global lamda
	global mu
	global nb
	po1=0
	theta=float(lamda)/float(mu)
	for i in range(int(nb+1)):
		po1=po1+puissance(theta,i)/factoriel(i)
	po2=puissance(theta,int(nb+1)/(factoriel(int(nb)*(int(nb-theta)))))	
		
	po=1/(po1+po2)	
	return po
	
def calcul_nu():  #Le nombre moyen de clients dans la file d'attente
	global lamda
	global mu
	global nb
	theta=float(lamda)/float(mu)
	m1=puissance(theta,int(nb)+1)*calcul_po()
	m2=int(nb)*factoriel(int(nb))*puissance(1-theta/int(nb),2)	
	m=m1/m2
	return m

def calcul_n():  #Le nombre moyen de cloients dans le systemes
	global lamda
	global mu
	global nb
	theta=float(lamda)/float(mu)
	n1=calcul_nu()+theta
	return n1

def calcul_t(): #Temps moyen d'attente
	global lamda
	global mu
	global nb
	theta=float(lamda)/float(mu)
	tf=calcul_nu()/float(lamda)	
	return tf




################ Début ###############################s


app = Flask(__name__)
app.secret_key = 'd66HR8dç"f_-àgjYYnc*df'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recuperationVariables/', methods=['GET', 'POST'])
def recupVar():
    global lamda
    global mu
    global nb
    error = None
    if request.method == 'POST':
        lamda=int(request.form['lamda'])
        mu=int(request.form['mu'])
        nb=int(request.form['nb'])
        donne=str(lamda)+" "+str(mu)+" "+str(nb)
        try:
            Monfichier="donnees.txt"
            Fichier = open(Monfichier,'w')
            Fichier.write(donne)
            Fichier.close()

        except:
        	error="imposible de creer le fichier"
        return render_template('recuperation.html',lamda=lamda,mu=mu,nb=nb)

        
@app.route('/fileAttente/')
def attente():
       	try:
            Monfichier="donnees.txt"
            Fichier = open(Monfichier,'r')
            contenu=Fichier.read()
            Fichier.close()
            tab=contenu.split()
            lamda=int(tab[0])
            mu=int(tab[1])
            nb=int(tab[2])
            theta=float(lamda)/float(mu)
            nbs=nb
            rho=int(nbs-theta)
            if theta<1:
            	nu=calcul_nu()
            	tf=calcul_t()
            	n=calcul_n()
            else:
            	return redirect(url_for('index'))
            return render_template('solution.html',lamda=lamda,mu=mu,nb=nb,theta=theta,nbs=nbs,rho=rho,nu=nu,tf=tf,n=n)
        except:
        	error="Impossible d'ouvrir le fichier"
        
@app.route('/erlangB/')
def erlangB():
	try:
		Monfichier="donnees.txt"
		Fichier = open(Monfichier,'r')
		contenu=Fichier.read()
		Fichier.close()
		tab=contenu.split()
		lamda=int(tab[0])
		mu=int(tab[1])
		nb=int(tab[2])
		theta=float(lamda)/float(mu)
		nbs=nb
		probaPertB=B(theta,nbs)
		traficEcoule=TrafEc(theta,nbs)
		return render_template('solution1.html',lamda=lamda,mu=mu,nb=nb,probaPertB=probaPertB,traficEcoule=traficEcoule)
	except:
		error="Impossible d'ouvrir le fichier"


@app.route('/erlangC/')
def erlangC():
       	try:
            Monfichier="donnees.txt"
            Fichier = open(Monfichier,'r')
            contenu=Fichier.read()
            Fichier.close()
            tab=contenu.split()
            lamda=int(tab[0])
            mu=int(tab[1])
            nb=int(tab[2])
            theta=float(lamda)/float(mu)
            nbs=nb
            if theta<1:
            	probaAttenteC=C(theta,nbs)
            	nbrClientAttente=Q(theta,nbs)
            	tempMoyFil=tempMoy(theta,nbs,lamda)
            	tauxSejour=t(theta,nbs,mu,lamda)
            else:
            	return redirect(url_for('index'))
            return render_template('solution2.html',lamda=lamda,mu=mu,nb=nb,prob=probaAttenteC,nbcl=nbrClientAttente,temp=tempMoyFil,taux=tauxSejour)
        except:
        	error="Impossible d'ouvrir le fichier"
        
######################################### Appel du programme #################################

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

