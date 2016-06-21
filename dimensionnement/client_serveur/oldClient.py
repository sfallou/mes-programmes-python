#!/usr/bin/python2.7
#-*-coding:utf8-*-
 
import socket;
import sys;
from Tkinter import *;
global lamda,mu,nb
################ Fonctions ##################
"""def traiter():
    lamda=float(lamda.get())
    m=float(mu.get())
    n=int(nb.get())"""

# Définition d'un client réseau gérant en parallèle l'émission
# et la réception des messages (utilisation de 2 THREADS).
 
host = 'localhost'
port = 20005
 
import socket, sys, threading
 
class ThreadReception(threading.Thread):
    """objet thread gérant la réception des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
 
    def run(self):
        while 1:
            message_recu = self.connexion.recv(1024)
            print "*** "  + message_recu +   "***"
            if message_recu =='' or message_recu.upper() == "FIN":
                break
        # Le thread <réception> se termine ici.
        # On force la fermeture du thread <émission> :
        print u"Client arrêté. Connexion interrompue."
        self.connexion.close()
 

    def fenetre(self):
       
        fen=Tk()
        fen.title("Dimensionnement")
        fen.geometry("1150x650")
        fen.resizable(True, True)
        
        #L'entete
        f0 = Frame( fen, bg ='#80c0c0', bd =5, relief =RAISED)
        f0.pack(side=TOP)
        Entete=Label( f0,text='UNIVERSITE CHEIKH ANTA DIOP\nECOLE SUPERIEURE POLYTECHNIQUE DE DAKAR\nDimensionnement Réseaux', width=100, height=5, bd=5, relief=RAISED, bg='white',font=('Helvetica', 10))
        Entete.grid(row =1, column =1, columnspan =3, padx =10, pady =5)
        texte = Label( f0, text ='Serigne Fallou NDIAYE\nDIC-1 Télécoms&Réseaux 2014/2015\nProfesseur: Dr. OUYA\n Phénomene d\'attente avec plusieurs serveurs\nCLIENT-SERVEUR', width='60', height=5, bd=5, bg='white',font=('Helvetica', 12))
        texte.grid(row =2, column =2, padx =5, pady =5)
        
       
     
        image2 = PhotoImage(file ="logoesp.gif")
        canIm2 = Canvas( f0, height = "130", width = "130", bg= "green")
        canIm2.create_image(90, 90, image =  image2)
        canIm2.grid(row =2, column =1, sticky=W, rowspan =3, padx =10, pady =5)

        # Conteneur du body
        body= Frame( fen, bg ='#80c0c0', bd =5, relief =RAISED,  width=100,)
        body.pack(pady=10)

        #Contenu de gauche
        f1 = Frame( body, bg = 'royal blue')
        f1.grid(row=1, column=1, padx =5)

        fcontenu=Frame(f1, borderwidth=1,bg ='#80c0c0')
        fcontenu.pack(padx=5,pady=5,expand="yes",fill="both",)
        fentree=Frame(fcontenu, borderwidth=1,bg ='#80c0c0')
        lfentree=LabelFrame(fentree,text="Les entrées",font="arial 12 bold italic",labelanchor = N,bg='white')
        fentree.grid(pady=5, row=0,column=0)
        lfentree.pack(padx=3, pady=5, expand="yes")
        Label(lfentree,text="λ (Nombre de clients entrants/seconde):", font="arial 12 bold",bg='white').grid(padx=5, pady=10, row=0 ,column=0)
        self.lamda=Entry(lfentree,font="arial 15 ", width=10)
        Label(lfentree,text="μ (Nombre de clients sortant/seconde):", font="arial 12 bold",bg='white').grid(padx=5, pady=10, row=1 ,column=0)
        Label(lfentree,text="N (Nombre de serveurs du systemes):", font="arial 12 bold",bg='white').grid(padx=5, pady=10, row=2 ,column=0)
        self.lamda=Entry(lfentree,font="arial 15 ", width=10)
        self.lamda.grid(padx=5, pady=20, row=0 ,column=1)
        self.mu=Entry(lfentree,font="arial 15 ", width=10)
        self.mu.grid(padx=5, pady=20, row=1 ,column=1)
        self.nb=Entry(lfentree,font="arial 15 ", width=10)
        self.nb.grid(padx=5, pady=20, row=2 ,column=1)
        b1=Button(lfentree,text='Calculer',bd=2, relief=RAISED,  bg ='royal blue', width=3, overrelief=RIDGE ,command=self.send_many)
        b1.grid(padx=5,pady=20,row=4,column=0)
        b2=Button(lfentree,text='Deconnecter',bd=2, relief=RAISED,  bg ='royal blue', width=9, overrelief=RIDGE ,command=self.send_FIN)
        b2.grid(padx=5,pady=20,row=4,column=1)

        
        # L'interface des saisies et des affichages a droite
        f2 = Frame( body, bg = 'royal blue', bd =2, relief =GROOVE)
        f2.grid(row=1, column=2, padx =5)
        fcontenu2=Frame(f2, borderwidth=1,bg ='#80c0c0')
        fcontenu2.pack(padx=5,pady=5,expand="yes",fill="both")
        fsortie=Frame(fcontenu2, borderwidth=1,bg ='#80c0c0')
        fsortie.grid(pady=5, row=0,column=1)
        fen.mainloop()
 
    def send_many(self):
        l=float(self.lamda.get())
        m=float(self.mu.get())
        n=int(self.nb.get())
        many = send_coucou(connexion,l,m,n)
        many.start()
 
    def send_FIN(self):
        connexion.send('FIN')
 
class send_coucou(threading.Thread):
    def __init__(self, connexion,l,m,n):
        threading.Thread.__init__(self)
        self.connexion = connexion
        self.l=l
        self.m=m 
        self.n=n
 
    def run(self):
        #for i in xrange(1, 2):
        #    self.connexion.send('coucou %s\r\n' % i)
        #msg="5 6 8"
        #l,m,n=traiter()
        msg=str(self.l)+" "+str(self.m)+" "+str(self.n)
        self.connexion.send(msg)
 
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
#fen = fenetre()
#fen.start()
