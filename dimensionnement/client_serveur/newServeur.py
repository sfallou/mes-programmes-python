#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
 
from Tkinter import *
from socket import *
from threading import Thread
from erlan import *

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
    po1=0
    theta=float(lamda)/float(mu)
    for i in range(int(nb)+1):
        po1=po1+puissance(theta,i)/factoriel(i)
    po2=puissance(theta,int(nb)+1)/(factoriel(int(nb))*(int(nb)-theta)) 
        
    po=1/(po1+po2)  
    return po
    
def calcul_nu():  #Le nombre moyen de clients dans la file d'attente
    theta=float(lamda)/float(mu)
    m1=puissance(theta,int(nb)+1)*calcul_po()
    m2=int(nb)*factoriel(int(nb))*puissance(1-theta/int(nb),2)  
    m=m1/m2
    return m

def calcul_n():  #Le nombre moyen de cloients dans le systemes
    theta=float(lamda)/float(mu)
    n1=calcul_nu()+theta
    return n1

def calcul_t(): #Temps moyen d'attente
    theta=float(lamda)/float(mu)
    tf=calcul_nu()/float(lamda) 
    return tf
          
class Serveur(Thread):
    def __init__(self, fen) :
        Thread.__init__(self)
        self.fen = fen
          
    def run(self) :
        global lamda
        global mu
        global nb
        hote = ""
        port = 8080
          
        connexion_principale = socket(AF_INET, SOCK_STREAM)
        connexion_principale.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        connexion_principale.bind((hote, port))
        connexion_principale.listen(5)
        text1 = Label(self.fen, text = "Le serveur écoute sur le port {}".format(port) ).pack()
        connexion_avec_client, infos_client = connexion_principale.accept()
        text2 = Label(self.fen, text = "Connexion avec le client {} établie.".format(infos_client)).pack()

        while 1:
            msg = connexion_avec_client.recv(1024)
            msg = msg.decode()
            variables = msg.split(":")
            lamda = variables[0]
            mu = variables[1]
            nb = variables[2]
            theta=float(lamda)/(float(mu)*int(nb))
            nbs=int(nb)
            rho=float(nbs-theta)
            if theta<1:
                nu=calcul_nu()
                tf=calcul_t()
                n=calcul_n()
                probaAttenteC=round(C(theta,nbs),5)
                nbrClientAttente=round(Q(theta,nbs),5)
                tempMoyFil=5#round(tempMoy(theta,nbs,lamda),5)
                tauxSejour=round(t(theta,nbs,mu,lamda),5)
                resultat = str(nu) + ';' + str(tf) + ';' + str(n) + ';' + str(rho)+';'+str(probaAttenteC)+';'+str(nbrClientAttente)+';'+str(tempMoyFil)+';'+str(tauxSejour)
                resultat = resultat.encode()
                connexion_avec_client.send(resultat)
 
fenetre_principale = Tk()
fenetre_principale.title("Serveur") 
 
ouvrir_serveur = Serveur(fenetre_principale)
ouvrir_serveur.start()
 
fenetre_principale.mainloop()