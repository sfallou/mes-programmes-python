#-*- coding: utf-8 -*- 
 
from decimal import *

########### les fonctions ######################
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



def calcul_po(lamda,mu,nb):  #
    po1=0
    theta=float(lamda)/float(mu)
    for i in range(int(nb+1)):
        po1=po1+puissance(theta,i)/factoriel(i)
    po2=puissance(theta,int(nb+1)/(factoriel(int(nb)*(int(nb-theta))))) 
        
    po=1/(po1+po2)  
    return po
    
def calcul_nu(lamda,mu,nb):  #Le nombre moyen de clients dans la file d'attente
    theta=float(lamda)/float(mu)
    m1=puissance(theta,int(nb)+1)*calcul_po(lamda,mu,nb)
    m2=int(nb)*factoriel(int(nb))*puissance(1-theta/int(nb),2)  
    m=m1/m2
    return m

def calcul_n(lamda,mu,nb):  #Le nombre moyen de cloients dans le systemes
    theta=float(lamda)/float(mu)
    n1=calcul_nu(lamda,mu,nb)+theta
    return n1

def calcul_t(lamda,mu,nb): #Temps moyen d'attente
    theta=float(lamda)/float(mu)
    tf=calcul_nu(lamda,mu,nb)/float(lamda)  
    return tf

def traitement(lamda,mu,nb):
    theta=float(lamda)/float(mu)
    rho=int(nb-theta)
    if theta<1:
        nu=calcul_nu(lamda,mu,nb)
        tf=calcul_t(lamda,mu,nb)
        n=calcul_n(lamda,mu,nb)
        #msg="Lamda="+str(lamda)+", mu="+str(mu)+", nb="+str(nb)+"\nnu="+str(nu)+", tf="+str(tf)+", n="+str(n)
        msg=str(nu)+" "+str(tf)+" "+str(n)+" "+str(rho)
        msg=str(msg)
        return msg
######################################################


# Définition d'un serveur réseau gérant un système de CHAT simplifié.
# Utilise les threads pour gérer les connexions clientes en parallèle.
 
HOST = 'localhost'
PORT = 20005
 
import socket, sys, threading
 
class ThreadClient(threading.Thread):
    '''dérivation d'un objet thread pour gérer la connexion avec un client'''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
 
    def run(self):
        # Dialogue avec le client :
        nom = self.getName()        # Chaque thread possède un nom
        while 1:
            msgClient = self.connexion.recv(1024)
            if msgClient.upper() == "FIN" or msgClient =="":
                break
            message = "%s> %s" % (nom, msgClient)
            msg_recu = msgClient.decode()
            valeur=msg_recu.split()
            lamda=float(valeur[0])
            mu=float(valeur[1])
            nb=float(valeur[2])
            msg=traitement(lamda,mu,nb)
            print message
            print msg
            # Faire suivre le message à tous les autres clients :
            for cle in conn_client:
#                if cle != nom:      # ne pas le renvoyer à l'émetteur
                conn_client[cle].send(msg)
 
        # Fermeture de la connexion :
        self.connexion.close()      # couper la connexion côté serveur
        del conn_client[nom]        # supprimer son entrée dans le dictionnaire
        print u"Client %s déconnecté." % nom
        # Le thread se termine ici    
 
# Initialisation du serveur - Mise en place du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print u"La liaison du socket à l'adresse choisie a échoué."
    sys.exit()
print u"Serveur prêt, en attente de requêtes sur le port %s..."%\
           (PORT)
mySocket.listen(5)
 
# Attente et prise en charge des connexions demandées par les clients :
conn_client = {}                # dictionnaire des connexions clients
while 1:    
    connexion, adresse = mySocket.accept()
    # Créer un nouvel objet thread pour gérer la connexion :
    th = ThreadClient(connexion)
    th.start()
    # Mémoriser la connexion dans le dictionnaire : 
    it = th.getName()        # identifiant du thread
    conn_client[it] = connexion
    print u"Client %s connecté, adresse IP %s, port %s." %\
           (it, adresse[0], adresse[1])
    # Dialogue avec le client :
    connexion.send("Vous êtes connecté. Envoyez vos messages.")