# Q3-5.py

import http.server
import socketserver
import os

# définition du nouveau handler
class RequestHandler(http.server.SimpleHTTPRequestHandler):
  
  # sous-répertoire racine des documents statiques
  static_dir = '/client'

  # on utilise le nom de fichier pour identifier le serveur
  server_version = os.path.basename(__file__)+'/0.1'
  
  # on surcharge la méthode qui traite les requêtes GET
  def do_GET(self):
    if self.path.startswith('/time'):
      self.send_time()
    else:
      self.send_static()

  def send_time(self):
     # on récupère l'heure
    time = self.date_time_string()
    corps="Bonjour, voici l'heure du serveur : {}".format(time)
    header=[('Content-Type','text/html;charset=UTF-8')]
    self.send(corps)

  # on surcharge la méthode qui traite les requêtes HEAD
  def do_HEAD(self):
    self.send_static()

  # on envoie le document statique demandé
  def send_static(self):

    # on modifie le chemin d'accès en insérant un répertoire préfixe
    self.path = self.static_dir + self.path

    # on calcule le nom de la méthode parent à appeler (do_GET ou do_HEAD)
    # à partir du verbe HTTP (GET ou HEAD)
    method = 'do_{}'.format(self.command)
    
    # on traite la requête via la classe parent
    getattr(http.server.SimpleHTTPRequestHandler,method)(self)

  def send(self,body,headers=[]):

    # on encode la chaine de caractères à envoyer
    encoded = bytes(body, 'UTF-8')

    # on envoie la ligne de statut
    self.send_response(200)

    # on envoie les lignes d'entête et la ligne vide
    [self.send_header(*t) for t in headers]
    self.send_header('Content-Length',int(len(encoded)))
    self.end_headers()

    # on envoie le corps de la réponse
    self.wfile.write(encoded)


# instanciation et lancement du serveur
httpd = socketserver.TCPServer(("", 8080), RequestHandler)
httpd.serve_forever()
