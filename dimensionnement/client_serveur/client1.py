#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
 
from Tkinter import *
from socket import *
from threading import Thread

global hote
global port
global lamda
global mu
global nb
global connexion_avec_serveur
global appel

def traitement():
    global lamda
    global mu
    global nb
    global connexion_avec_serveur
    global fsortie
    lamda = str(lamda.get())
    mu = str(mu.get())
    nb = str(nb.get())
    msg = lamda + ':' + mu + ':' + nb
    msg = msg.encode()
    connexion_avec_serveur.send(msg)
    result = connexion_avec_serveur.recv(1024)
    result = result.decode()
    var = result.split(";")
    nu = var[0]
    tf = var[1]
    n = var[2]
    rho = var[3]
    fentree.destroy()
    fsortie=Frame(fcontenu, borderwidth=3,bg ='#80c0c0')
    fsortie.pack(padx=5,pady=5,expand="yes",fill="both")
    lfsortie=LabelFrame(fsortie,text="Les Résultats",font="arial 15 bold",labelanchor = N)
    lfsortie.pack(padx=5, pady=5, expand="yes")
    Label(lfsortie,text="La longueur moyenne de la file d'attente:", font=('Helvetica', 12)).grid(row=0, columnspan=2)
    Label(lfsortie,text="ν = ", font=('Helvetica', 12)).grid(padx=5, pady=20, row=1 ,column=0)
    Label(lfsortie,text="Le nombre moyen de clients dans le systéme:", font=('Helvetica', 12)).grid(row=2, columnspan=2)
    Label(lfsortie,text="n = ", font=('Helvetica', 12)).grid(padx=5, pady=20, row=3 ,column=0)
    Label(lfsortie,text="Le temps moyen d'attente dans la file d'attente:", font=('Helvetica', 12)).grid(row=4, columnspan=2)
    Label(lfsortie,text="tf = ", font=('Helvetica', 12)).grid(padx=5, pady=20, row=5 ,column=0)
    Label(lfsortie,text="Le nombre de serveurs inoccupés:", font=('Helvetica', 12)).grid(row=6, columnspan=2)
    Label(lfsortie,text="ρ = ", font=('Helvetica', 12)).grid(row=7 ,column=0)
    Label(lfsortie,text=nu, font=('Helvetica', 12)).grid(row=1 ,column=1)
    Label(lfsortie,text=n, font=('Helvetica', 12)).grid(row=3 ,column=1)
    Label(lfsortie,text=tf, font=('Helvetica', 12)).grid(row=5 ,column=1)
    Label(lfsortie,text=rho, font=('Helvetica', 12)).grid(row=7 ,column=1)
    b4=Button(lfsortie,text="RESSAYER",bg="white",font="arial 10 bold",width="15" ,command=requete)
    b4.grid(row=8, column=0)
    b3=Button(lfsortie,text="QUITTER",bg="white",font="arial 10 bold",width="15" ,command=fen.destroy)
    b3.grid(row=8, column=1)

def requete():
    global lamda
    global mu
    global nb
    global connexion_avec_serveur
    global fentree
    global fsortie
    global appel
    if appel > 0:
        fsortie.destroy()
    appel = appel + 1
    fentree=Frame(fcontenu,borderwidth=1,bg ='#80c0c0')
    fsortie=Frame(fcontenu, borderwidth=1,bg ='#80c0c0')
    lfentree=LabelFrame(fentree,text="Paramètrs d'entrée",font="arial 15 bold",labelanchor = N)
    fentree.pack(padx=5,pady=5,expand="yes",fill="both")
    lfentree.pack(padx=5, pady=6, expand="yes")
    Label(lfentree,text="Veuillez entrer le nombre de clients entrants/unité de temps:", font=('Helvetica', 12)).grid(padx=5, pady=5, row=0, columnspan=2)
    Label(lfentree,text="λ = ", font=('Helvetica', 12)).grid(padx=5, pady=5, row=1 ,column=0)
    lamda=Entry(lfentree,font="arial 15 ", width=10)
    Label(lfentree,text="Veuillez entrer le nombre de clients sortant/unité de temps:", font=('Helvetica', 12)).grid(padx=5, pady=5, row=4, columnspan=2)
    Label(lfentree,text="μ = ", font=('Helvetica', 12)).grid(padx=5, pady=5, row=5 ,column=0)
    Label(lfentree,text="Veuillez entrer le nombre de serveurs du systemes:", font=('Helvetica', 12)).grid(padx=5, pady=5, row=8, columnspan=2)
    Label(lfentree,text="N = ", font=('Helvetica', 12)).grid(padx=5, pady=5, row=9 ,column=0)
    lamda=Entry(lfentree,font="arial 15 ", width=10)
    lamda.grid(padx=5, pady=5, row=1 ,column=1)
    mu=Entry(lfentree,font="arial 15 ", width=10)
    mu.grid(padx=5, pady=5, row=5 ,column=1)
    nb=Entry(lfentree,font="arial 15 ", width=10)
    nb.grid(padx=5, pady=5, row=9 ,column=1)
    b2=Button(lfentree,text="RESULTAT",bg="white",font="arial 10 bold",width="15" ,command=traitement)
    b2.grid(padx=5,pady=5,row=10, columnspan=2)

def connexion():
    global connexion_avec_serveur
    connexion_avec_serveur = socket(AF_INET, SOCK_STREAM)
    connexion_avec_serveur.connect((str(hote.get()), int(port.get()))) 
    fconnexion.destroy()
    requete()

fen=Tk()
appel = 0
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


fcontenu=Frame(fen, borderwidth=3)
fcontenu.pack(padx=5,pady=5,expand="yes",fill="both")
fconnexion=Frame(fcontenu, borderwidth=1,bg ='#80c0c0')
lfconnexion=LabelFrame(fconnexion,text="CONNEXION",font="arial 15 bold",labelanchor = N,borderwidth=1,bg ='#80c0c0')
fconnexion.pack(padx=5,pady=5,expand="yes",fill="both")
lfconnexion.pack(padx=5, pady=6, expand="yes")
Label(lfconnexion,text="Adresse : ", font=('Helvetica', 12)).grid(padx=5, pady=20, row=0 ,column=0)
hote=Entry(lfconnexion,font="arial 15 ", width=10)
Label(lfconnexion,text="Port : ", font=('Helvetica', 12)).grid(padx=5, pady=20, row=1 ,column=0)
hote=Entry(lfconnexion,font="arial 15 ", width=10)
hote.grid(padx=5, pady=20, row=0 ,column=1)
port=Entry(lfconnexion,font="arial 15 ", width=10)
port.grid(padx=5, pady=20, row=1 ,column=1)
b1=Button(lfconnexion,bg="white",text='Connecter',font="arial 10 bold" ,command=connexion)
b1.grid(padx=5,pady=20,row=12, columnspan=2)

fen. mainloop()