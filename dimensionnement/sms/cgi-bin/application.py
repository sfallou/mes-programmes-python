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
    probaPertB=B(theta,nbs)
    traficEcoule=TrafEc(theta,nbs)
    resultat="Pour Lamda="+str(lamda)+",mu="+str(mu)+"et nb="+str(nb)+" on a: probaPerte="+str(probaPertB)+" et traficEcoule="+str(traficEcoule)
    print(resultat)
except:
    print("erreur dans la synthaxe du message")

