#! /usr/bin/python
# -*- coding: UTF-8 -*-
import cgi                        # Module d'interface avec le serveur web
from fonction import *
form = cgi.FieldStorage()         # Réception de la requête utilisateur :
sms = form["sms"].value
phone = form["phone"].value

tab=sms.split(" ")
#msg="vous avez envoyé: "+tab[0]+" , "+tab[1]+" , "+tab[2]
print ("Content-Type: text/html\n")
try:
	trafic=teta(int(tab[1]), int(tab[2]))
	if(trafic>int(tab[3])):
		print("error! Le trafic ne doit pas être supérieur au nombre de circuit")
	else:
		serv=ServeurInoccuper(trafic, int(tab[3]))
		longueur=longMoy(trafic, int(tab[3]))
		client=NombreMoyClient(serv, trafic)
		temps=TempsMoyenAttente(serv, int(tab[1]))
	#print("le trafic est: "+ str(trafic)+" la longueur moyenne de la file est: "+)
	
except:

	print("erreur dans la synthaxe du message")
