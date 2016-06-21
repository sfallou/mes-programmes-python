# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------
    @Authors                                                      |
             Serigne Fallou NDIAYE  & Chuhan WANG                 |
             Jordan N'Guessan KONAN & Mingshan  ZHG               |
    @From: Ecole Centrale de Lyon                                 |
    @Prog: Projet d'Application web en Python                     |
    @Date: 08 - 06 - 2016                                         | 
-------------------------------------------------------------------
"""
########################## Début du programme  #################################

"""
-----------------------------------------------------------
Importation des bibliothèques utilisées dans ce programme |
-----------------------------------------------------------
"""
import fractale as F1
import fractale2 as F2
import socketserver
import os
import json
from datetime import datetime

#
# Définition du nouveau handler
#
import generic 

PORT=8080
# Définition du nouveau handler
#
class RequestHandler(generic.RequestHandler):
  
  # sous-répertoire racine des documents statiques
  static_dir = '/client'
  # on utilise le nom de fichier pour identifier le serveur
  server_version = os.path.basename(__file__)+'/0.1'
  # On surcharge la méthode qui traite les requêtes GET
  

   #
  # initialisation noms du fichier image
  #
  def init_vars(self):
    generic.RequestHandler.init_vars(self)
    c=self.path_info[1]
    c=eval(c)
    if self.path_info[0] == 'percolation':
      w=int(self.path_info[2])
      h=int(self.path_info[3])
      nom="img_"+str(w)+"_"+str(h)+"_"+str(c[0])+"_"+str(c[1])+"_"+str(c[2])+".png"
    elif self.path_info[0] == 'percolation2':
      rayon=self.path_info[2]
      nom="imgcentre_"+str(rayon)+"_"+str(c[0])+"_"+str(c[1])+"_"+str(c[2])+".png"
    self.nom_image=nom
    #self.imagepath = '../images/{}'.format(''.join(nom_image))

 
  #
  # On crée la méthode qui traite les requetes POST
  #
  def do_POST(self):
    # on initialise nos variables d'instance
    self.init_vars()
    if self.path_info[0] == 'percolation':
      self.send_params()
    elif self.path_info[0] == 'percolation2':
      self.send_params2()
    else:
      self.send_error(405)
      
 
  # On envoie un document avec les données
  #
  def send_params(self):
    # on récupère les inforamtions données par l'utilisateur
    color=self.path_info[1]
    height=int(self.path_info[3])
    width=int(self.path_info[2])
    color=eval(color)
    # on fait appelle à la métohde creerImage définis dans le dossier fractale.py
    info=F1.creerImage(width,height,color)
    print('../images/'+self.nom_image)
    headers = [('Content-Type','application/json')];
    body = json.dumps({'image':'images/'+self.nom_image,'alt':'Image generee','title':'Fractale'})           
    # on envoie
    self.send(body,headers)

   # On envoie un document avec les données
  #
  def send_params2(self):
    # on récupère les inforamtions données par l'utilisateur
    color=self.path_info[1]
    R=int(self.path_info[2])
    color=eval(color)
    # on fait appelle à la métohde creerImage définis dans le dossier fractale.py
    info=F2.creerImage(R,color[0],color[1],color[2])
    headers = [('Content-Type','application/json')];
    body = json.dumps({'image':'images/'+self.nom_image,'alt':'Image generee','title':'Fractale'})           
    # on envoie
    self.send(body,headers)
#
# Instanciation et lancement du serveur
#
httpd = socketserver.TCPServer(("", PORT), RequestHandler)
print("Serveur démarré sur le port:",PORT)
httpd.serve_forever()