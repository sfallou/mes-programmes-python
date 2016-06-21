#! /usr/bin/python
# -*- coding: UTF-8 -*-
import os
import pickle
import time
import copy
from erlan import *
import cgi                        # Module d'interface avec le serveur web
from fonction import *
form = cgi.FieldStorage()         # Réception de la requête utilisateur :
sms = form["sms"].value
phone = form["phone"].value

tab=sms.split(" ")
#msg="vous avez envoyé: "+tab[0]+" , "+tab[1]+" , "+tab[2]
print ("Content-Type: text/html\n")
try:
    lamda=int(tab[1])
    mu=int(tab[2])
    nb=int(tab[3])
    theta=float(lamda)/float(mu)
    nbs=nb
    if theta<1:
        probaAttenteC=round(C(theta,nbs),5)
        nbrClientAttente=round(Q(theta,nbs),5)
        tempMoyFil=round(tempMoy(theta,nbs,lamda),5)
        tauxSejour=round(t(theta,nbs,mu,lamda),5)
        resultat="Pour Lamda="+str(lamda)+",mu="+str(mu)+"et nb="+str(nb)+" on a: probaAttente="+str(probaAttenteC)+", client en attente="+str(nbrClientAttente)+", tempMoyFil="+str(tempMoyFil)+", tempsSejour="+str(tauxSejour)
    else:
        resultat="Il faut que lamda soit inferieur a mu"
    print(resultat)
except:
    print("erreur dans la synthaxe du message")

