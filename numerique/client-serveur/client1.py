#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Tkinter import *
from socket import *
from threading import Thread
from math import *
from time import *
import tkMessageBox
import pickle

global hote
global port
global ordreMat
global matA
global matB
matA=list()
matB=list()


def Apropos():
	Aproposfen = Tk()
	Aproposfen.configure(bg="white")
        s="Cette application a été réalisée dans le cadre \n du module de Calcul numérique. Ce module \n a été dispensé par le Docteur Samuel OUYA\n à l'école Supérieure Polytechnique de Dakar (Sénégal)."
        Labelapro = Label(Aproposfen, text=s,bg="white", font=("Arial", 12, "bold"))
        Boutonqt = Button(Aproposfen, text="Quitter", font=("Arial", 12, "bold"), fg='white', bg='red', command=Aproposfen.destroy)

        Labelapro.grid(row=0, column=0, padx=5, pady=5)
        Boutonqt.grid(row=2, column=0, padx=5, pady=5)

        Aproposfen.mainloop()

def erreur(info):
	faffiche=Frame(fsortie, borderwidth=1, bg="#80c0c0")
	faffiche.place(relx=0,rely=0.4,relwidth=1, relheight=0.6)
	faffichetext=Frame(faffiche, borderwidth=1, bg="#80c0c0")
	faffichetext.place(relx=0,rely=0,relwidth=1, relheight=0.2)
	Label(faffichetext,text=info,foreground="red", font="arial 14 bold", bg="#80c0c0").pack(anchor=CENTER)
	# boutons recommencer, quitter et apropos
	fafficheBut=Frame(faffiche, borderwidth=1, bg="#80c0c0")
	fafficheBut.place(relx=0,rely=0.8,relwidth=1, relheight=0.2)
	#Button(fafficheBut,text="Recommencer",bg="white",fg="green",font="arial 12 bold",width="15", command=recommencer).place(relx=0.45,rely=0.0)
	#Button(fafficheBut,text="Apropos",bg="white",fg="blue",font="arial 12 bold",width="5",command =Apropos).place(relx=0.72,rely=0.0)	
	Button(fafficheBut,text="Quitter",bg="white",fg="blue",font="arial 12 bold",width="5",command =quitter).place(relx=0.85,rely=0.0)

def afficheGauss():
	global resX
	ordre=int(ordreMat.get())
	faffiche=Frame(fsortie, borderwidth=1, bg="#80c0c0")
	faffiche.place(relx=0,rely=0.4,relwidth=1, relheight=0.6)
	faffichetext=Frame(faffiche, borderwidth=1, bg="#80c0c0")
	faffichetext.place(relx=0,rely=0,relwidth=1, relheight=0.2)
	fafficheMat=Frame(faffiche, borderwidth=1, bg="#80c0c0")
	fafficheMat.place(relx=0,rely=0.2,relwidth=1, relheight=0.6)
	fafficheMatcontenu=Frame(fafficheMat, borderwidth=1, background="#80c0c0")
	fafficheMatcontenu.pack(fill=Y,pady=10)
	Label(faffichetext,text="La solution obtenue par la méthode Gauss est:",foreground="blue", font="arial 14 bold", bg="#80c0c0").pack(anchor=CENTER)	
	for i in range(ordre):	
		Label(fafficheMatcontenu,text=round(resX[i],2),foreground="red", font="arial 12 bold",pady=0, background="#80c0c0",justify=CENTER).grid(padx=5, pady=5, row=i,column=1)
	#Creation des canvas de parentheses
        parA1 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        parA1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="[", font=("Arial", 24*ordre))
        parA2 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        parA2.create_text(5*ordre, 13*ordre, anchor=CENTER, text="]", font=("Arial", 24*ordre))
	parA1.grid(row=0, column=0, rowspan=ordre)
	parA2.grid(row=0, column=2, rowspan=ordre)
	# boutons recommencer, quitter et apropos
	fafficheBut=Frame(faffiche, borderwidth=1, bg="#80c0c0")
	fafficheBut.place(relx=0,rely=0.8,relwidth=1, relheight=0.2)
	#Button(fafficheBut,text="Recommencer",bg="white",fg="green",font="arial 12 bold",width="15", command=recommencer).place(relx=0.45,rely=0.0)
	#Button(fafficheBut,text="Apropos",bg="white",fg="blue",font="arial 12 bold",width="5",command =Apropos).place(relx=0.72,rely=0.0)	
	Button(fafficheBut,text="Quitter",bg="white",fg="blue",font="arial 12 bold",width="5",command =quitter).place(relx=0.85,rely=0.0)

def afficheLu():
	global resXLu
	ordre=int(ordreMat.get())
	faffiche=Frame(fsortie, borderwidth=1, bg="#80c0c0")
	faffiche.place(relx=0,rely=0.4,relwidth=1, relheight=0.6)
	faffichetext=Frame(faffiche, borderwidth=1, bg="#80c0c0")
	faffichetext.place(relx=0,rely=0,relwidth=1, relheight=0.2)
	fafficheMat=Frame(faffiche, borderwidth=1, bg="#80c0c0")
	fafficheMat.place(relx=0,rely=0.2,relwidth=1, relheight=0.8)
	fafficheMatcontenu=Frame(fafficheMat, borderwidth=1, background="#80c0c0")
	fafficheMatcontenu.pack(fill=Y,pady=10)
	Label(faffichetext,text="La solution obtenue par la factorisation LU est:",foreground="blue", font="arial 14 bold", bg="#80c0c0").pack(anchor=CENTER)	
	for i in range(ordre):	
		Label(fafficheMatcontenu,text=round(resXLu[i],2),foreground="red", font="arial 12 bold",pady=0, background="#80c0c0",justify=CENTER).grid(padx=5, pady=5, row=i,column=1)
	#Creation des canvas de parentheses
        parA1 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        parA1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="[", font=("Arial", 24*ordre))
        parA2 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        parA2.create_text(5*ordre, 13*ordre, anchor=CENTER, text="]", font=("Arial", 24*ordre))
	parA1.grid(row=0, column=0, rowspan=ordre)
        parA2.grid(row=0, column=2, rowspan=ordre)
	# boutons recommencer, quitter et apropos
	fafficheBut=Frame(faffiche, borderwidth=1, bg="#80c0c0")
	fafficheBut.place(relx=0,rely=0.8,relwidth=1, relheight=0.2)
	#Button(fafficheBut,text="Recommencer",bg="white",fg="green",font="arial 12 bold",width="15", command=recommencer).place(relx=0.45,rely=0.0)
	#Button(fafficheBut,text="Apropos",bg="white",fg="blue",font="arial 12 bold",width="5",command =Apropos).place(relx=0.72,rely=0.0)	
	Button(fafficheBut,text="Quitter",bg="white",fg="blue",font="arial 12 bold",width="5",command =quitter).place(relx=0.85,rely=0.0)

def afficheCholeski():
	global resXCh
	ordre=int(ordreMat.get())	
	faffiche=Frame(fsortie, borderwidth=1, bg="#80c0c0")
	faffiche.place(relx=0,rely=0.4,relwidth=1, relheight=0.6)
	faffichetext=Frame(faffiche, borderwidth=1, bg="#80c0c0")
	faffichetext.place(relx=0,rely=0,relwidth=1, relheight=0.2)
	fafficheMat=Frame(faffiche, borderwidth=1, bg="#80c0c0")
	fafficheMat.place(relx=0,rely=0.2,relwidth=1, relheight=0.8)
	fafficheMatcontenu=Frame(fafficheMat, borderwidth=1, background="#80c0c0")
	fafficheMatcontenu.pack(fill=Y,pady=10)
	Label(faffichetext,text="La solution obtenue par la factorisation Cholesky est:",foreground="blue", font="arial 14 bold", bg="#80c0c0").pack(anchor=CENTER)	
	for i in range(ordre):	
		Label(fafficheMatcontenu,text=round(resXCh[i],2),foreground="red", font="arial 12 bold",pady=0, background="#80c0c0",justify=CENTER).grid(padx=5, pady=5, row=i,column=1)
	#Creation des canvas de parentheses
        parA1 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        parA1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="[", font=("Arial", 24*ordre))
        parA2 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        parA2.create_text(5*ordre, 13*ordre, anchor=CENTER, text="]", font=("Arial", 24*ordre))
	parA1.grid(row=0, column=0, rowspan=ordre)
        parA2.grid(row=0, column=2, rowspan=ordre)
	# boutons recommencer, quitter et apropos
	fafficheBut=Frame(faffiche, borderwidth=1, bg="#80c0c0")
	fafficheBut.place(relx=0,rely=0.8,relwidth=1, relheight=0.2)
	#Button(fafficheBut,text="Recommencer",bg="white",fg="green",font="arial 12 bold",width="15", command=recommencer).place(relx=0.45,rely=0.0)
	#Button(fafficheBut,text="Apropos",bg="white",fg="blue",font="arial 12 bold",width="5",command =Apropos).place(relx=0.72,rely=0.0)	
	Button(fafficheBut,text="Quitter",bg="white",fg="blue",font="arial 12 bold",width="5",command =quitter).place(relx=0.85,rely=0.0)



def afficheInverse():
	global I
	ordre=int(ordreMat.get())
	faffiche=Frame(fsortie, borderwidth=1, bg="#80c0c0")
	faffiche.place(relx=0,rely=0.4,relwidth=1, relheight=0.6)
	faffichetext=Frame(faffiche, borderwidth=1, bg="#80c0c0")
	faffichetext.place(relx=0,rely=0,relwidth=1, relheight=0.2)
	fafficheMat=Frame(faffiche, borderwidth=1, bg="#80c0c0")
	fafficheMat.place(relx=0,rely=0.2,relwidth=1, relheight=0.8)
	fafficheMatcontenu=Frame(fafficheMat, borderwidth=1, background="#80c0c0")
	fafficheMatcontenu.pack(fill=Y,pady=10)
	Label(faffichetext,text="L'inverse de la matrice est :",foreground="blue", font="arial 14 bold", bg="#80c0c0").pack(anchor=CENTER)	
	for i in range(ordre):
		for j in range(ordre):		
			Label(fafficheMatcontenu,text=round(I[i][j],2),foreground="red", font="arial 12 bold",pady=0, background="#80c0c0",justify=CENTER).grid(padx=5, pady=5, row=i,column=j+1)
	#Creation des canvas de parentheses
        parA1 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        parA1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="(", font=("Arial", 24*ordre))
        parA2 = Canvas(fafficheMatcontenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        parA2.create_text(5*ordre, 13*ordre, anchor=CENTER, text=")", font=("Arial", 24*ordre))
	parA1.grid(row=0, column=0, rowspan=ordre)
        parA2.grid(row=0, column=ordre+1, rowspan=ordre)
	# boutons recommencer, quitter et apropos 
	fafficheBut=Frame(faffiche, borderwidth=1, bg="#80c0c0")
	fafficheBut.place(relx=0,rely=0.8,relwidth=1, relheight=0.2)
	Button(fafficheBut,text="Recommencer",bg="white",fg="green",font="arial 12 bold",width="15", command=recommencer).place(relx=0.45,rely=0.0)	
	#Button(fafficheBut,text="Apropos",bg="white",fg="blue",font="arial 12 bold",width="5",command =Apropos).place(relx=0.72,rely=0.0)	
	#Button(fafficheBut,text="Quitter",bg="white",fg="blue",font="arial 12 bold",width="5",command =quitter).place(relx=0.85,rely=0.0)

def quitter():
	fenetre.destroy()
	connexion_avec_serveur.send('0')

def recommencer():
	global fsortie
	fsortie.destroy()
	del(matA[:]) # permet de vider la liste matA
	del(matB[:])
	requete()

def recuperer1():
	ordre=int(ordreMat.get())
	try:
		for i in range(ordre):
			for j in range(ordre):
				matA[i][j]=int(matA[i][j].get())
	except:
		tkMessageBox.showinfo('Erreur Matrice',"n'adveuillez entrer des valeurs entieres")
def recuperer2():
	ordre=int(ordreMat.get())
	try:
		for i in range(ordre):
			matB[i]=int(matB[i].get())
			for j in range(ordre):
				matA[i][j]=int(matA[i][j].get())
	except:
		tkMessageBox.showinfo('Erreur Matrice',"veuillez entrer des valeurs entieres")



def beforeGauss():
	saisieMatrice2(1)
	
def beforeLu():
	saisieMatrice2(2)

def beforeCholeski():
	saisieMatrice2(3)

def beforeInverse():
	saisieMatrice1()


def Gauss():
	global matA
	global matB
	global resX
	global connexion_avec_serveur
	recuperer2()
	msg ='gauss'+ ':'+ pickle.dumps(matA) + ':' + pickle.dumps(matB)
	connexion_avec_serveur.send(msg)
	result = connexion_avec_serveur.recv(1024)
	var = result.split(";")	
	ok_or_no=var[0]	
	if ok_or_no =='O':
		resX = pickle.loads(var[1])
		afficheGauss()
	else:
		info = var[1]		
		erreur(info)

def Lu():
	global matA
	global matB
	global resXLu
	global connexion_avec_serveur
	recuperer2()
	msg = 'lu'+ ':' + pickle.dumps(matA) + ':' + pickle.dumps(matB)
	connexion_avec_serveur.send(msg)
	result = connexion_avec_serveur.recv(1024)
	var = result.split(";")	
	ok_or_no=var[0]	
	if ok_or_no =='O':
		resXLu = pickle.loads(var[1])
		afficheLu()	
	else :
		info = var[1]
		erreur(info)
def Choleski():
	global matA
	global matB
	global resXCh
	global connexion_avec_serveur
	recuperer2()
	msg = 'choleski' + ':' + pickle.dumps(matA) + ':' + pickle.dumps(matB)
	connexion_avec_serveur.send(msg)
	result = connexion_avec_serveur.recv(1024)
	var = result.split(";")
	ok_or_no=var[0]	
	if ok_or_no =='O':
		resXCh = pickle.loads(var[1])
		afficheCholeski()
	else :
		info = var[1]
		erreur(info)

def Inverse():
	global matA
	global I
	global connexion_avec_serveur
	recuperer1()
	msg = 'inverse' + ':' +pickle.dumps(matA)
	connexion_avec_serveur.send(msg)
	result = connexion_avec_serveur.recv(1024)
	var = result.split(";")
	ok_or_no=var[0]	
	if ok_or_no =='O':
		I = pickle.loads(var[1])
		afficheInverse()
	else :
		info = var[1]
		erreur(info)

	

def menu(): 
  global fsaisie
  fsaisie=Frame(fentree, borderwidth=1, bg="azure")
  fsaisie.place(relx=0,rely=0.3,relwidth=1, relheight=0.7)
  #Button(fsaisie,text='Résolution Gauss',bg="#80c0c0",fg="blue",font="arial 12 bold",width=40,pady=20,command=beforeGauss).pack(pady=2)
  #Button(fsaisie,text='Résolution LU',bg="#80c0c0",fg="blue",font="arial 12 bold",width=40,pady=20,command=beforeLu).pack(pady=2)
  #Button(fsaisie,text='Résolution Cholesky',bg="#80c0c0",fg="blue",font="arial 12 bold",width=40,pady=20,command=beforeCholeski).pack(pady=2)
  Button(fsaisie,text='Inverse de Matrice',bg="#80c0c0",fg="blue",font="arial 12 bold",width=40,pady=20,command=beforeInverse).pack(pady=2)




def saisieMatrice1():
	global fsortie	
	fsortie1=Frame(fsortie, borderwidth=1, background="#80c0c0")
	fsortie1.place(relx=0.0,rely=0,relwidth=1, relheight=0.4)
	fsortie1contenu=Frame(fsortie1, borderwidth=1, background="#80c0c0")
	fsortie1contenu.pack(fill=Y,pady=10)	
	try:
		ordre=int(ordreMat.get())
	except:
		tkMessageBox.showinfo('Erreur de taille',"La taille de la matrice doit avoir une valeur entiere")
	if ordre<=0:		
		tkMessageBox.showinfo('Erreur de taille',"La taille de la matrice doit est etre positive")
	else:
		for i in range(ordre):
			matcol=list()
			for j in range(ordre):
		    		p=Entry(fsortie1contenu,width=5,relief='raised',justify=CENTER)
		    		#p.insert(0,'(%s;%s)' % (i,j))
		    		p.grid(row=i,column=j+1,padx=5, pady=5)
		    		matcol.append(p)
			matA.append(matcol)
		#Creation des canvas de parentheses
        	parA1 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        	parA1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="(", font=("Arial", 24*ordre))
        	parA2 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        	parA2.create_text(5*ordre, 13*ordre, anchor=CENTER, text=")", font=("Arial", 24*ordre))
		parA1.grid(row=0, column=0, rowspan=ordre)
        	parA2.grid(row=0, column=ordre+1, rowspan=ordre)
		
		Button(fsortie1,text="calculer",bg="white",fg="blue",font="arial 12 bold",width="5",command=Inverse).place(relx=0.4,rely=0.8)
		

def saisieMatrice2(z):	
	fsortie1=Frame(fsortie, borderwidth=1, background="#80c0c0")
	fsortie1.place(relx=0.0,rely=0,relwidth=1, relheight=0.4)
	fsortie1contenu=Frame(fsortie1, borderwidth=1, background="#80c0c0")
	fsortie1contenu.pack(fill=Y,pady=10)
	try:
		ordre=int(ordreMat.get())
	except:
		tkMessageBox.showinfo('Erreur de taille',"La taille de la matrice doit avoir une valeur entiere")
	if ordre<=0:
		tkMessageBox.showinfo('Erreur de taille',"La taille de la matrice doit est etre positive")
	else:
		for i in range(ordre):
			matcol=list()
			for j in range(ordre):
		    		p=Entry(fsortie1contenu,width=5,relief='raised',justify=CENTER)
		    		#p.insert(0,'(%s;%s)' % (i,j))
		    		p.grid(row=i,column=j+1,padx=5, pady=5)
		    		matcol.append(p)
			matA.append(matcol)
		for i in range(ordre):
		    	p=Entry(fsortie1contenu,width=5,relief='raised',justify=CENTER)
		    	#p.insert(0,'(%s)' % (i))
		    	p.grid(row=i,column=ordre+7, padx=5, pady=5)
		    	matB.append(p)
		
		#Crearion des labels X
		xlabel = list()
        	texteX = list()
		for i in range(ordre):
            		xlabel.append([])
            		texteX.append([])
        	for i in range(ordre):
            		texteX[i] = StringVar()
            		texteX[i].set("x"+str(i+1))
            		xlabel[i] = Label(fsortie1contenu, textvariable=texteX[i], bg='#80c0c0',highlightbackground='#80c0c0',font=("Arial", 14, "bold"))
			xlabel[i].grid(row=i, column=ordre+3)
		#Creation des canvas de parentheses
        	parA1 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        	parA1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="(", font=("Arial", 24*ordre))
        	parA2 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        	parA2.create_text(5*ordre, 13*ordre, anchor=CENTER, text=")", font=("Arial", 24*ordre))
 
        	parX1 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        	parX1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="(", font=("Arial", 24*ordre))
        	parX2 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        	parX2.create_text(5*ordre, 13*ordre, anchor=CENTER, text=")", font=("Arial", 24*ordre))
        
        	parB1 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        	parB1.create_text(5*ordre, 13*ordre, anchor=CENTER, text="(", font=("Arial", 24*ordre))
        	parB2 = Canvas(fsortie1contenu, width=10*ordre, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        	parB2.create_text(5*ordre, 13*ordre, anchor=CENTER, text=")", font=("Arial", 24*ordre))

        	#canvas Egalité
        	egalite = Canvas(fsortie1contenu, width=20, height=30*ordre, bg='#80c0c0',highlightbackground='#80c0c0')
        	egalite.create_text(21, 15*ordre, anchor=CENTER, text="=", font=("Arial", 20*ordre))	

		parA1.grid(row=0, column=0, rowspan=ordre)
        	parA2.grid(row=0, column=ordre+1, rowspan=ordre)
		parX1.grid(row=0, column=ordre+2, rowspan=ordre)
        	parX2.grid(row=0, column=ordre+4, rowspan=ordre)
        	egalite.grid(row=0, column=ordre+5, rowspan=ordre)
        	parB1.grid(row=0, column=ordre+6, rowspan=ordre)
        	parB2.grid(row=0, column=ordre+8, rowspan=ordre)	
		

		choix=int(z)
		if (choix==1):
			Button(fsortie1,text="calculer",bg="white",fg="blue",font="arial 12 bold",width="5",command= Gauss).place(relx=0.4,rely=0.8)
		elif (choix==2):
			Button(fsortie1,text="calculer",bg="white",fg="blue",font="arial 12 bold",width="5",command= Lu).place(relx=0.4,rely=0.8)
		elif (choix==3):
			Button(fsortie1,text="calculer",bg="white",fg="blue",font="arial 12 bold",width="5",command= Choleski).place(relx=0.4,rely=0.8)

def requete():
	
	global connexion_avec_serveur
	global fcontenu
	global fentree
	global fsortie
	global appel
	global ordreMat
	if appel > 0:
		fsortie.destroy()
	appel = appel + 1
	### definition du cadre effectif post connexion fils de la conteneuse principale ###
	fentree=Frame(fcontenu, borderwidth=1, background="azure") 
	fsortie=Frame(fcontenu, borderwidth=1, background="#80c0c0")
	Frame(fcontenu, borderwidth=1,background="azure").place(relx=0,rely=0,relwidth=0.02,relheight=1)
	#Frame(fcontenu, borderwidth=1, background="indian red").place(relx=0.98,rely=0,relwidth=0.02, relheight=1)
	fentree.place(relx=0.02,rely=0,relwidth=0.4, relheight=1)
	fsortie.place(relx=0.44,rely=0,relwidth=0.56, relheight=1)
	Label(fentree,text="La taille de la matrice:", foreground="blue", font="arial 14 bold", bg="azure").grid(row=0 ,column=0,ipadx=10)
	ordreMat=Entry(fentree,font="arial 16 ", width=5)
	ordreMat.grid(padx=20, pady=10, row=0 ,column=1)
	bu1=Button(fentree,text="valider",bg="white",fg="blue",font="arial 12 bold",width="5",command = menu)
	bu1.grid(padx=20,pady=10,row=0,column=2)


def connexion():
	try :
		global connexion_avec_serveur
		connexion_avec_serveur = socket(AF_INET, SOCK_STREAM)
		connexion_avec_serveur.connect((str(hote.get()), int(port.get()))) 
		fconnexion.destroy()
		requete()
	except:
		tkMessageBox.showinfo("Erreur Connexion","Connexion refusée: Verifiez les parametres de connexion")
		
            
fenetre = Tk()
fenetre.title("Calcul Numerique")
fenetre.geometry("1200x800")
fenetre.configure(background = "azure")

#L'entete
f0 = Frame( fenetre, bg ='#80c0c0', bd =5, relief =RAISED)
f0.pack(side=TOP)
Entete=Label(f0,text='UNIVERSITE CHEIKH ANTA DIOP\nECOLE SUPERIEURE POLYTECHNIQUE DE DAKAR\nPROGRAMME DE CALCUL NUMERIQUE', width=100, height=5, bd=5, relief=RAISED, bg='white',font=('Helvetica', 10))
Entete.grid(row =1, column =1, columnspan =3, padx =10, pady =5)
texte = Label( f0, text ='Serigne Fallou NDIAYE\nDIC-1 Télécoms&Réseaux 2014/2015\nProfesseur: Dr. OUYA\n****Client-Serveur****', width='60', height=5, bd=5, bg='white',font=('Helvetica', 12))
texte.grid(row =2, column =2, padx =5, pady =5)
    
#Images de l'entete   
image = PhotoImage(file ="me.gif")
canIm = Canvas( f0, height = "130", width = "130", bg= "green")
canIm.create_image(90, 90, image =  image)
canIm.grid(row =2, column =3, sticky=E, rowspan =3, padx =10, pady =5)
     
image2 = PhotoImage(file ="logoesp.gif")
canIm2 = Canvas( f0, height = "130", width = "130", bg= "green")
canIm2.create_image(90, 90, image =  image2)
canIm2.grid(row =2, column =1, sticky=W, rowspan =3, padx =10, pady =5)

### definition de la conteneuse principale ###
global fcontenu
fcontenu=Frame(fenetre, borderwidth=1)
fcontenu.pack(expand="yes",fill="both")
fcontenu.configure(background="#80c0c0")

### cadre de connexion fils de la conteneuse principale ###
fconnexion=Frame(fcontenu, borderwidth=3,bg="#80c0c0")
fconnexion.pack(padx=5,pady=5,expand="yes",fill="both")
lfconnexion=LabelFrame(fconnexion,text="CONNEXION AU SERVEUR",labelanchor = N,borderwidth=3,foreground="blue", font="arial 14 bold", bg="azure")
fconnexion.pack(padx=5,pady=5,expand="yes",fill="both")
lfconnexion.pack(padx=5, pady=6, expand="yes")
Label(lfconnexion,text="Adresse : ", font="arial 12 bold", bg="azure").grid(padx=5, pady=20, row=0 ,column=0)
hote=Entry(lfconnexion,font="arial 15 ", width=10)
Label(lfconnexion,text="Port : ", font="arial 12 bold", bg="azure").grid(padx=5, pady=20, row=1 ,column=0)
hote=Entry(lfconnexion,font="arial 15 ", width=10)
hote.grid(padx=5, pady=20, row=0 ,column=1)
port=Entry(lfconnexion,font="arial 15 ", width=10)
port.grid(padx=5, pady=20, row=1 ,column=1)
Button(lfconnexion,text="Connexion",bg="white",fg="blue",font="arial 12 bold" ,command=connexion).grid(padx=5,pady=20,row=12, columnspan=2)


appel =0
fenetre.mainloop()

