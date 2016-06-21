#! /usr/bin/python
# -*- coding: UTF-8 -*-
# Traitement des données transmises par un formulaire HTML
 
import cgi                        # Module d'interface avec le serveur web
form = cgi.FieldStorage()         # Réception de la requête utilisateur :
                                   # il s'agit d'une sorte de dictionnaire
if form.has_key("phrase"):        # La clé n'existera pas si le champ
	text = form["phrase"].value    # correspondant est resté vide
else:
	text ="*** le champ phrase était vide ! ***"

if form.has_key("visiteur"):      # La clé n'existera pas si le champ
	nomv = form["visiteur"].value  # correspondant est resté vide
else:
	nomv ="mais vous ne m'avez pas indiqué votre nom"
 
print "Content-Type: text/html\n"
print """
<H3>Merci, %s !</H3>
<H4>La phrase que vous m'avez fournie était : </H4>
<H3><FONT Color="red"> %s </FONT></H3>""" % (nomv, text)
  
