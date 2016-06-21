#!/usr/bin/python2.7
#-*-coding:utf8-*-
 
import socket;
import sys;
import Tkinter;
 
 
# Définition d'un client réseau gérant en parallèle l'émission
# et la réception des messages (utilisation de 2 THREADS).
 
host = 'localhost'
port = 40000
 
import socket, sys, threading
 
class ThreadReception(threading.Thread):
    """objet thread gérant la réception des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
 
    def run(self):
        while 1:
            message_recu = self.connexion.recv(1024)
            print "*" + message_recu + "*"
            if message_recu =='' or message_recu.upper() == "FIN":
                break
        # Le thread <réception> se termine ici.
        # On force la fermeture du thread <émission> :
        print u"Client arrêté. Connexion interrompue."
        self.connexion.close()
 
class fenetre(threading.Thread):
    def run(self):
        Tkinter.Label(text = "Welcome!").pack();
        Tkinter.Button(text = "Send coucou", command = self.send_many).pack();
        Tkinter.Button(text = "Se déconnecter", command = self.send_FIN).pack();
        Tkinter.mainloop();
 
    def send_many(self):
        many = send_coucou(connexion)
        many.start()
 
    def send_FIN(self):
        connexion.send('FIN')
 
class send_coucou(threading.Thread):
    def __init__(self, connexion):
        threading.Thread.__init__(self)
        self.connexion = connexion
 
    def run(self):
        for i in xrange(1, 2):
            self.connexion.send('coucou %s\r\n' % i)
 
# Programme principal - Établissement de la connexion :
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion.connect((host, port))
except socket.error:
    print u"La connexion a échoué."
    sys.exit()    
print u"Connexion établie avec le serveur."
Connected = False;
 
# Dialogue avec le serveur : on lance deux threads pour gérer
# indépendamment l'émission et la réception des messages :
th_R = ThreadReception(connexion)
th_R.start()
fen = fenetre()
fen.start()
