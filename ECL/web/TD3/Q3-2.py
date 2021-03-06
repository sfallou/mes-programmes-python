# TD3/serveur.py

import http.server
import socketserver
import os
from datetime import datetime
from pytz import timezone
import pytz
from urllib.parse import urlparse, parse_qs
import json

class RequestHandler(http.server.SimpleHTTPRequestHandler):

  # sous-répertoire racine des documents statiques
  static_dir = '/client'

  # on utilise le nom de fichier pour identifier le serveur
  server_version = os.path.basename(__file__)+'/0.1'


  #
  # On surcharge la méthode qui traite les requêtes GET
  #
  def do_GET(self):

    # le chemin d'accès commence par /time
    if self.path.startswith('/time'):
      self.send_time()

    # ou pas...
    else:
      self.send_static()

  #
  # On surcharge la méthode qui traite les requêtes HEAD
  #
  def do_HEAD(self):
    self.send_static()

  #
  # On envoie le document statique demandé
  #
  def send_static(self):

    # on modifie le chemin d'accès en insérant un répertoire préfixe
    self.path = self.static_dir + self.path

    # on calcule le nom de la méthode parent à appeler (do_GET ou do_HEAD)
    # à partir du verbe HTTP (GET ou HEAD)
    method = 'do_{}'.format(self.command)
    
    # on traite la requête via la classe parent
    getattr(http.server.SimpleHTTPRequestHandler,method)(self)


  #
  # On envoie un document avec l'heure
  #
  def send_time(self,timer):

    # on récupère le fuseau horaire demandé
    tz_name = timer
    try:
      tz = timezone(tz_name)
    except(pytz.exceptions.UnknownTimeZoneError):
      self.send_error(400,'Unknown Time Zone')
      return

    # on récupère la date et l'heure
    time = datetime.utcnow()

    # on convertit vers le fuseau demandé
    tz_time = tz.normalize(pytz.utc.localize(time).astimezone(tz))

    # on génère le style
    style = ''
    for k in self.params:
      if k and not k == 'timezone':
        style = style + '{}:{};'.format(k,self.params[k][0])
        
    # on génère un document
    utctime=style,tz_time.strftime('%A %d %B %Y, %H:%M:%S')

    body =json.dumps({
      'utctime':time.strftime('%A %d %B %Y, %H:%M:%S'),
      'tzname':tz_name,
      'tztime':tz_time.strftime('%A %d %B %Y, %H:%M:%S')
      })

    # on envoie
    self.send(body)
    # on envoie la réponse

  #
  # On envoie le corps fourni
  #
  def send(self,body):

    # on envoie la ligne de statut
    self.send_response(200)

    # on envoie les lignes d'entête par défaut et la ligne vide
    self.end_headers()

    # on encode la chaine de caractères à envoyer
    encoded = bytes(body, 'UTF-8')

    # on envoie le corps de la réponse
    self.wfile.write(encoded)

 
#
# Instanciation et lancement du serveur
#
httpd = socketserver.TCPServer(("", 8080), RequestHandler)
httpd.serve_forever()
