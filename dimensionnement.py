# -*- encoding: utf-8 -*-

from Tkinter import *
from math import *
from os import *


def puissance(a, n):
    if(n==0):
        return 1
    else:
        p = a
        for i in range(1, n):
            p = p*a
        return p

def factoriel(x):
    if(x==0):
        return 1
    else:
        fact = 1
        for i in range(1, x+1):
            fact = fact*i
        return fact

def  erlangB(A,N):
	a=0
	for i in range(N+1):
		a+=puissance(A,i)/factoriel(i)
	An=puissance(A,N)
	Nfact=factoriel(N)
	r=An/Nfact
	pb=r/a
	return pb

def nbCircuits(A, a, pb, c):
	i = 1
	j = 0
	for j in range(c):
		if A[j][0]==pb:
			for i in range(53):
				print(str(i))
				if A[j][i]==a or (A[j][i]<a and A[j][i+1]>a) :
					print(str(i))
					break
				#i = i+1
		#j = j+1
	return i

def nbCircuitsC(A, a, pb, c):
	i = 1
	j = 0
	for j in range(c):
		if A[j][0]==pb:
			for i in range(51):
				print(str(i))
				if A[j][i]==a or (A[j][i]<a and A[j][i+1]>a) :
					print(str(i))
					break
				#i = i+1
		#j = j+1
	return i

def traficB(A,N,pb,c):
	i = 0
	while(i<=(c-1)) and (A[i][0]!=pb):
		i=i+1
	return A[i][N]

def erlangC(A,N):
	a=0
	for k in range(N):
		a+=puissance(A,k)/factoriel(k)
	a+=puissance(A,N)/(factoriel(N)*(1-A/N))
	p0=1/a
	A=puissance(A,N)/(factoriel(N)*(1-A/N))
	r=A*p0
	return r

def fileAttente(A,N):
	if((A/N)<1):
		#calcul de Po
		p0=0
		for i in range(N+1):
			p0+=(puissance(A,i))/(factoriel(i))
		p0+=(puissance(A,N+1))/(factoriel(N)*(N-A))
		p0=1/p0
		#calcul de la longueur moyenne de la file d'attente
		nu=factoriel(N)*N*puissance((1-A/N),2)
		nu=(puissance(A,N+1)*p0)/nu
		return nu

class Dimensionnement:

	def __init__(self):
		self.debut()

	def debut(self):
		self.Window = Tk()
		self.Window.title("Outil de dimensionnement Réseaux")
		self.Window.geometry("+50+50")
        #self.Window.title("Résolution de Systèmes Linéaires")
        #self.Window.geometry("+50+50")

        #Création de l'image
		self.canvasPhoto = Canvas(self.Window, width=500)
		"""self.photoPr = PhotoImage(file = 'Capture.GIF')
		self.itemPr = self.canvasPhoto.create_image(250, 120, image=self.photoPr)"""

		#creation des frames
		self.frameBouton = Frame(self.Window)

		#Création des boutons
		self.Filedattente = Button(self.frameBouton, width=12, text="File d'attente", fg='white', bg='blue', font=("Arial", 15, "bold"), command=self.file_dattente)
		self.Erlang = Button(self.frameBouton, width=12, text="Lois d'Erlang", fg='white', bg='blue', font=("Arial", 15, "bold"), command=self.Erlang) 
		self.Quitter = Button(self.frameBouton, width=12, text="Quitter", fg='white', bg='red', font=("Arial", 15, "bold"), command=self.Window.destroy)

		#Disposition des widgets
		self.canvasPhoto.grid(row=0)
		self.frameBouton.grid(row=1)

		self.Filedattente.grid(row=0)
		self.Erlang.grid(row=1, pady=5)
		self.Quitter.grid(row=2, pady=20, sticky=S)

		self.Window.mainloop()

	def file_dattente(self):
		self.FramePr = Frame(self.Window)
		FrameSaisi = Frame(self.FramePr)
		FrameBouton = Frame(self.FramePr)

		"""can = Canvas(FramePr, width=500)
		photo = PhotoImage(file = 'Capturetout.GIF')
		item = can.create_image(250, 100, image=photo)"""

		#Création des labels de saisi
		LabelMsg = Label(FrameSaisi, text="Lambda (clients/seconde)", font=("Arial", 12, "bold"))
		LabelTservice = Label(FrameSaisi, text="Mu", font=("Arial", 12, "bold"))
		LabelServeurs = Label(FrameSaisi, text="Nombre de serveurs", font=("Arial", 12, "bold"))

		#Création des champs
		self.ChampMsg = Entry(FrameSaisi, font=("Arial", 10, "bold"), justify=CENTER)
		self.ChampTservice = Entry(FrameSaisi, font=("Arial", 10, "bold"), justify=CENTER)
		self.ChampServeurs = Entry(FrameSaisi, font=("Arial", 10, "bold"), justify=CENTER)
		self.ChampMsg.focus_set()

		#Creation du Frame
		self.FrameRes = Frame(self.FramePr, bg='white')

		#Création des Boutons
		BoutonResultat = Button(FrameBouton, text="Résultat", fg='white', bg='gray', font=("Times New Roman", 13, "bold"), command=self.Resultat)
		BoutonQuitter = Button(FrameBouton, text="Retour", fg='white', bg='red', font=("Times New Roman", 13, "bold"), command=self.Restart)

		#Disposition des widgets de saisi
		LabelMsg.grid(row=0)
		LabelTservice.grid(row=1)
		LabelServeurs.grid(row=2)
		self.ChampMsg.grid(row=0, column=1, padx=10, pady=5)
		self.ChampTservice.grid(row=1, column=1, padx=10, pady=5)
		self.ChampServeurs.grid(row=2, column=1, padx=10, pady=5)

		#Disposition des boutons
		BoutonResultat.grid(row=0, padx=5, pady=20)
		BoutonQuitter.grid(row=0, column=2, padx=5)

		#Disposition
		#can.pack()
		FrameSaisi.pack()
		FrameBouton.pack()
		self.FramePr.grid(row=1)

	def Resultat(self):
		note = 0
		try:
			l = int(self.ChampMsg.get())
			h = int(self.ChampTservice.get())
			S = int(self.ChampServeurs.get())

			note = 1

		except:
			self.err()

		if (note==1):
			teta = l/h
			TETsurS = teta/S
			self.BoutonRecommencer = Button(self.FramePr, text="Recommencer", fg='white', bg='gray', font=("Times New Roman", 13, "bold"), command=self.Recommencer)

			#Création des chaines variables
			StringPo = StringVar()
			StringN = StringVar()
			StringNu = StringVar()
			StringRh = StringVar()
			StringR = StringVar()
			StringTemps = StringVar()

			#Creation des labels de resultat
			LabelPo = Label(self.FrameRes, text="Probabilité Po", bg='white', font=("Arial", 13, "bold"), fg='blue')
			LabelN = Label(self.FrameRes, text="Nombre moyen de clients dans le\n système", bg='white', font=("Arial", 13, "bold"), fg='blue')
			LabelNu = Label(self.FrameRes, text="Longueur de la file d'attente", bg='white', font=("Arial", 13, "bold"), fg='blue')
			LabelRh = Label(self.FrameRes, text="Nombre de serveurs inoccupés", bg='white', font=("Arial", 13, "bold"), fg='blue')
			LabelR = Label(self.FrameRes, text="Temps moyen (non converti)", bg='white', font=("Arial", 13, "bold"), fg='blue')
			LabelTserv = Label(self.FrameRes, text="Temps moyen (converti)", bg='white', font=("Arial", 13, "bold"), fg='blue')

			#Creation ds labels blancs
			LabelBPo = Label(self.FrameRes, textvariable=StringPo, bg='white', width=15, font=("Arial", 13, "bold"))
			LabelBN = Label(self.FrameRes, textvariable=StringN, bg='white', width=15, font=("Arial", 13, "bold"))
			LabelBNu = Label(self.FrameRes, textvariable=StringNu, bg='white', width=15, font=("Arial", 13, "bold"))
			LabelBRh = Label(self.FrameRes, textvariable=StringRh, bg='white', width=15, font=("Arial", 13, "bold"))
			LabelBR = Label(self.FrameRes, textvariable=StringR, bg='white', width=15, font=("Arial", 13, "bold"))
			LabelBTemps = Label(self.FrameRes, textvariable=StringTemps, bg='white', width=15, font=("Arial", 13, "bold"))

			if(TETsurS<1):
				p1 = 0
				for i in range(0, S+1):
					p1 += (puissance(teta, i)/factoriel(i))
				Po = p1
				Po += (puissance(teta, (S+1))/(factoriel(S)*(S-teta)))
				Po = 1/Po
				nu = puissance(teta, S+1)*Po
				nu = nu/(factoriel(S)*S*(1-teta/S)*(1-teta/S))
				tf1 = nu/l
				tf2 = nu//1
				tf3 = ((tf1-tf2)*60)//1

				n = nu+teta
				r = S-teta

				StringPo.set(""+str(round(Po,6)))
				StringN.set(""+str(round(n, 6)))
				StringNu.set(""+str(round(nu,6)))
				StringRh.set(""+str(r))
				StringR.set(""+str(round(tf1, 5)))
				StringTemps.set(""+str(tf2)+" min "+str(tf3)+" sec")

				#Disposition dse widgets resultat
				LabelPo.grid(row=0)
				LabelN.grid(row=1)
				LabelNu.grid(row=2)
				LabelRh.grid(row=3)
				LabelR.grid(row=4)
				LabelTserv.grid(row=5)
				LabelBPo.grid(row=0, column=1, padx=10, pady=5)
				LabelBN.grid(row=1, column=1, padx=10, pady=5)
				LabelBNu.grid(row=2, column=1, padx=10, pady=5)
				LabelBRh.grid(row=3, column=1, padx=10, pady=5)
				LabelBR.grid(row=4, column=1, padx=10, pady=5)
				LabelBTemps.grid(row=5, column=1, padx=10, pady=5)
			else:
				FenErreurk = Tk()
				FenErreurk.geometry("+100+100")

				#Creation label ERREUR
				LabelErreurk = Label(FenErreurk, width=50, font=("Arial", 15, "bold"), text="Une erreur est survenue.\n Le rapport Intensité du trafic sur le Nombre de serveurs\n doit être inférieur à 1.", fg='red', bg='white')

				BoutonQuitterk = Button(FenErreurk, text="Ok", bg='red', fg='white', font=("Arial", 12, "bold"), command=FenErreurk.destroy)

				LabelErreurk.pack()
				BoutonQuitterk.pack()
				FenErreurk.mainloop()

			self.BoutonRecommencer.pack()
			self.FrameRes.pack()

	def err(self):
		FenErreur = Tk()
		FenErreur.geometry("+100+100")

		#Creation label ERREUR
		LabelErreur = Label(FenErreur, width=50, font=("Arial", 15, "bold"), text="Une erreur est survenue.\nVeuillez entrer des valeurs normales.", fg='red', bg='white')

		BoutonQuitter = Button(FenErreur, text="Ok", bg='red', fg='white', font=("Arial", 12, "bold"), command=FenErreur.destroy)
		LabelErreur.pack()
		BoutonQuitter.pack()
		FenErreur.mainloop()

	def Recommencer(self):
		self.ChampMsg.delete(0, END)
		self.ChampTservice.delete(0, END)
		self.ChampServeurs.delete(0, END)
		self.ChampMsg.focus_set()
		self.BoutonRecommencer.destroy()
		self.FrameRes.destroy()

	def Restart(self):
		python = sys.executable
		execl(python, python, * sys.argv)

	def ErlangB(self):
		self.frameBouton.destroy()
		self.frameBoutonEr.destroy()
		self.FrameP = Frame(self.Window)
		#les 3 Frames
		self.Frame1 = Frame(self.FrameP, borderwidth=2, bd=2, relief=SUNKEN)
		self.Frame2 = Frame(self.FrameP, borderwidth=2, bd=2, relief=SUNKEN)
		self.Frame3 = Frame(self.FrameP, borderwidth=2, bd=2, relief=SUNKEN)

		self.FrameResultat = Frame(self.FrameP, bg='white')

		self.RecommencerMenu = Button(self.Window, text="Retour au menu", bg='green', fg='white', font=("Arial", 13, "bold"), command=self.Restart)
		self.BoutonQuitterPrincipal = Button(self.Window, text="Quitter", bg='red', fg='white', font=("Arial", 13, "bold"), command=self.Window.destroy)


		#Frame 1
		#Les labels
		self.LabelTete1 = Label(self.Frame1, text="Probabilité de Blocage", font=("Arial", 17, "bold"))
		self.LabTraficOffert1 = Label(self.Frame1, text='Traffic Offert', font=("Arial", 13, "bold"))
		self.LabNbCircuits1 = Label(self.Frame1, text="Circuits", font=("Arial", 13, "bold"))
		#Les champs de texte
		self.ChampTrafic1 = Entry(self.Frame1, width=7, font=("Arial", 13, "bold"), justify=CENTER)
		self.ChampCircuits = Entry(self.Frame1, width=7, font=("Arial", 13, "bold"), justify=CENTER)
		#Bouton
		self.Calculer1 = Button(self.Frame1, text="Calculer", bg='blue', fg='white', font=("Arial", 12, "bold"), command=self.Calculer1)
		#Dispositions
		self.LabelTete1.grid(row=0, columnspan=2, ipady=7)
		self.LabTraficOffert1.grid(row=1, column=0)
		self.LabNbCircuits1.grid(row=2, column=0)
		self.ChampTrafic1.grid(row=1, column=1)
		self.ChampCircuits.grid(row=2, column=1)
		self.Calculer1.grid(row=3, columnspan=2)

		#Frame 2
		#Les labels
		self.LabelTete2 = Label(self.Frame2, text="Trafic Offert", font=("Arial", 17, "bold"))
		self.LabProbaBloc2 = Label(self.Frame2, text='Probabilité de Blocage', font=("Arial", 13, "bold"))
		self.LabNbCircuits2 = Label(self.Frame2, text="Circuits", font=("Arial", 13, "bold"))
		#Les champs de texte
		self.ChampProbaBloc2 = Entry(self.Frame2, width=7, font=("Arial", 13, "bold"), justify=CENTER)
		self.ChampCircuits2 = Entry(self.Frame2, width=7, font=("Arial", 13, "bold"), justify=CENTER)
		#Bouton
		self.Calculer2 = Button(self.Frame2, text="Calculer", bg='blue', fg='white', font=("Arial", 12, "bold"), command=self.Calculer3)
		#Dispositions
		self.LabelTete2.grid(row=0, columnspan=2, ipady=7)
		self.LabProbaBloc2.grid(row=1, column=0)
		self.LabNbCircuits2.grid(row=2, column=0)
		self.ChampProbaBloc2.grid(row=1, column=1)
		self.ChampCircuits2.grid(row=2, column=1)
		self.Calculer2.grid(row=3, columnspan=2)

		#Frame 3
		#Les labels
		self.LabelTete3 = Label(self.Frame3, text="Nombre de Circuits", font=("Arial", 17, "bold"))
		self.LabProbaBloc3 = Label(self.Frame3, text='Probabilité de Blocage (en %)', font=("Arial", 13, "bold"))
		self.LabTraficOffert3 = Label(self.Frame3, text="Trafic Offert", font=("Arial", 13, "bold"))
		#Les champs de texte
		self.ChampProbaBloc3 = Entry(self.Frame3, width=7, font=("Arial", 13, "bold"), justify=CENTER)
		self.ChampTraficOffert3 = Entry(self.Frame3, width=7, font=("Arial", 13, "bold"), justify=CENTER)
		#Bouton
		self.Calculer3 = Button(self.Frame3, text="Calculer", bg='blue', fg='white', font=("Arial", 12, "bold"), command=self.Calcul)
		#Dispositions5
		self.LabelTete3.grid(row=0, columnspan=2, ipady=7)
		self.LabProbaBloc3.grid(row=1, column=0)
		self.LabTraficOffert3.grid(row=2, column=0)
		self.ChampProbaBloc3.grid(row=1, column=1)
		self.ChampTraficOffert3.grid(row=2, column=1)
		self.Calculer3.grid(row=3, columnspan=2)


		#Dispositions des frames
		self.Frame1.grid(row=0, column=0)
		self.Frame2.grid(row=0, column=1)
		self.Frame3.grid(row=0, column=2)
		self.BoutonQuitterPrincipal.grid(row=3, pady=15)
		self.RecommencerMenu.grid(row=1,pady=5)
		self.FrameP.grid(row=2)

	def Erlang(self):
		#creation des frames
		self.frameBoutonEr = Frame(self.Window)

		#Création des boutons
		self.BoutonErB = Button(self.frameBoutonEr, width=12, text="Erlang B", fg='white', bg='blue', font=("Arial", 15, "bold"), command=self.ErlangB)
		self.BoutonErC = Button(self.frameBoutonEr, width=12, text="Erlang C", fg='white', bg='blue', font=("Arial", 15, "bold"), command=self.ErlangC) 
		self.RetourM = Button(self.frameBoutonEr, width=12, text="Retour", fg='white', bg='red', font=("Arial", 15, "bold"), command=self.Restart)

		#Disposition des widgets
		self.frameBoutonEr.grid(row=1)

		self.BoutonErB.grid(row=0)
		self.BoutonErC.grid(row=1, pady=5)
		self.RetourM.grid(row=2, pady=20, sticky=S)

	def Calculer1(self):
		self.FrameResultat.destroy()
		self.FrameResultat = Frame(self.FrameP, bg='white')
		inote = 0
		#labels de résultats
		self.LabProbaBlocage = Label(self.FrameResultat, text="Probabilité de Blocage (en %)", bg='white', fg='blue', font=("Arial", 13, "bold"))
		self.LabTraficEcoule = Label(self.FrameResultat, text="Trafic écoulé (Erlang)", bg='white', fg='blue', font=("Arial", 13, "bold"))
		self.LabPourcPerte = Label(self.FrameResultat, text="Pourcentage de perte (en %)", bg='white', fg='blue', font=("Arial", 13, "bold"))
		#Variables
		StringPb = StringVar()
		StringTE = StringVar()
		StringPert = StringVar()
		#Labels blancs
		self.LabNProbaBloc = Label(self.FrameResultat, textvariable=StringPb, bg='white', fg='blue', font=("Arial", 13, "bold"))
		self.LabNTraficEcoule = Label(self.FrameResultat, textvariable=StringTE, bg='white', fg='blue', font=("Arial", 13, "bold"))
		self.LabNPourcPerte = Label(self.FrameResultat, textvariable=StringPert, bg='white', fg='blue', font=("Arial", 13, "bold"))

		try:
			A = float(self.ChampTrafic1.get())
			N = int(self.ChampCircuits.get())
			inote = 1
		except:
			self.err()

		if (inote==1):
			Pb = erlangB(A, N)
			Ae = A*(1-Pb)
			perte = (A-Ae)/A

			StringPb.set(""+str(round(Pb*100, 2)))
			StringTE.set(""+str(round(Ae, 2)))
			StringPert.set(""+str(round(perte*100, 2)))

			self.LabProbaBlocage.grid(row=0, column=0, padx=5, pady=5)
			self.LabTraficEcoule.grid(row=1, column=0, padx=5, pady=5)
			self.LabPourcPerte.grid(row=2, column=0, padx=5, pady=5)
			self.LabNProbaBloc.grid(row=0, column=1, pady=5)
			self.LabNTraficEcoule.grid(row=1, column=1, pady=5)
			self.LabNPourcPerte.grid(row=2, column=1, pady=5)


			self.FrameResultat.grid(row=1, columnspan=3, pady=10)
			

	def Calcul(self):
		self.FrameResultat.destroy()
		self.FrameResultat = Frame(self.FrameP, bg='white')
		#labels de résultats
		self.LabNbrCir = Label(self.FrameResultat, text="Le nombre de Circuits est ", bg='white', fg='blue', font=("Arial", 15, "bold"))
		#Variables
		StringNc = StringVar()
		#Labels blancs
		self.LabNbrCirB = Label(self.FrameResultat, textvariable=StringNc, bg='white', fg='blue', width=15, font=("Arial", 15, "bold"))
		#Récupération des entrees
		ino = 0
		try:
			pb=float(self.ChampProbaBloc3.get())
			traf = float(self.ChampTraficOffert3.get())
			#print(str(pb)+" "+str(traf))
			ino = 1
		except:
			self.err()
		if (ino==1):
			A = list()
			for k in range(5):
				A.append([])
				for l in range(53):
					A[k].append([])
			for k in range(5):
				for l in range(53):
					A[k][l] = 0
			fich = open("erlangB.txt", "r")
			for i in range(5):
				for j in range(53):
					A[i][j] = float(fich.readline())
			nbCir = nbCircuits(A, traf, pb, 5)
			StringNc.set(""+str(nbCir))
			self.LabNbrCir.grid(row=0, column=0, padx=5, pady=5)
			self.LabNbrCirB.grid(row=0, column=1, padx=5, pady=5)


		self.FrameResultat.grid(row=2, columnspan=3, pady=10)


	def Calculer3(self):
		self.FrameResultat.destroy()
		self.FrameResultat = Frame(self.FrameP, bg='white')
		#labels de résultats
		self.LabTrafB = Label(self.FrameResultat, text="Le Trafic offert est ", bg='white', fg='blue', font=("Arial", 15, "bold"))
		#Variables
		StringtrafB = StringVar()
		#Labels blancs
		self.LabNTrafB = Label(self.FrameResultat, textvariable=StringtrafB, bg='white', fg='blue', width=15, font=("Arial", 15, "bold"))
		#Récupération des entrees
		ino = 0
		
		try:
			pb=float(self.ChampProbaBloc2.get())
			Nbcr = int(self.ChampCircuits2.get())
			ino = 1
		except:
			self.err()
		if(ino==1):
			A = list()
			for k in range(5):
				A.append([])
				for l in range(53):
					A[k].append([])
			for k in range(5):
				for l in range(53):
					A[k][l] = 0
			fich = open("erlangB.txt", "r")
			for i in range(5):
				for j in range(53):
					A[i][j] = float(fich.readline())
			tr = traficB(A, Nbcr, pb, 5)
			StringtrafB.set(""+str(round(tr, 2)))
			self.LabTrafB.grid(row=0, column=0, padx=5, pady=5)
			self.LabNTrafB.grid(row=0, column=1, padx=5, pady=5)

		self.FrameResultat.grid(row=2, columnspan=3, pady=10)


	def ErlangC(self):
		self.frameBouton.destroy()
		self.frameBoutonEr.destroy()
		self.FramePC = Frame(self.Window)
		#les 3 Frames
		self.FrameErlC = Frame(self.FramePC, borderwidth=2, bd=2, relief=SUNKEN)
		self.FrameErlC2 = Frame(self.FramePC, borderwidth=2, bd=2, relief=SUNKEN)
		self.FrameErlC3 = Frame(self.FramePC, borderwidth=2, bd=2, relief=SUNKEN)

		self.FrameResultat = Frame(self.FramePC, bg='white')
		self.RecommencerMenu2 = Button(self.Window, text="Retour au menu", bg='green', fg='white', font=("Arial", 13, "bold"), command=self.Restart)

		#Labels 1
		self.LabelTeteC = Label(self.FrameErlC, text="Probabilité de Mise en attente", font=("Arial", 15, "bold"))
		self.LabTrafC = Label(self.FrameErlC, text='Trafic offert', font=("Arial", 11, "bold"))
		self.LabNbrCirC = Label(self.FrameErlC, text='Nombre de Circuits', font=("Arial", 11, "bold"))

		self.ChampTrafC = Entry(self.FrameErlC, width=10, font=("Arial", 11, "bold"), justify=CENTER)
		self.ChampTrafC.focus_set()
		self.ChampNbrCirC = Entry(self.FrameErlC, width=10, font=("Arial", 11, "bold"), justify=CENTER)

		#labels 2
		#Labels
		self.LabelTeteC2 = Label(self.FrameErlC2, text="Nombre de Circuits", font=("Arial", 15, "bold"))
		self.LabProbaAt = Label(self.FrameErlC2, text='Probabilité de mise en attente (%)', font=("Arial", 11, "bold"))
		self.LabTrafBt = Label(self.FrameErlC2, text='Trafic offert', font=("Arial", 11, "bold"))

		self.ChampProbaAt = Entry(self.FrameErlC2, width=10, font=("Arial", 11, "bold"), justify=CENTER)
		#self.ChampTrafC.focus_set()
		self.ChampTrafBt = Entry(self.FrameErlC2, width=10, font=("Arial", 11, "bold"), justify=CENTER)
		self.BoutonCalculerC2 = Button(self.FrameErlC2, text="Calculer", bg='blue', fg='white', font=("Arial", 12, "bold"), command=self.CalculerC2)

		#Boutotnt
		self.BoutonCalculerC = Button(self.FrameErlC, text="Calculer", bg='blue', fg='white', font=("Arial", 12, "bold"), command=self.CalculerC)
		self.BoutonQuitterC = Button(self.Window, text="Quitter", bg='red', fg='white', font=("Arial", 12, "bold"), command=self.Restart)

		#label 3
		#Labels
		self.LabelTeteC3 = Label(self.FrameErlC3, text="Trafic offert", font=("Arial", 15, "bold"))
		self.LabProbaAt3 = Label(self.FrameErlC3, text='Probabilité de mise en attente (%)', font=("Arial", 11, "bold"))
		self.LabNBc3 = Label(self.FrameErlC3, text='Nombre de circuits', font=("Arial", 11, "bold"))
		self.ChampProbaAt3 = Entry(self.FrameErlC3, width=10, font=("Arial", 11, "bold"), justify=CENTER)
		#self.ChampTrafC.focus_set()
		self.ChampNBc3 = Entry(self.FrameErlC3, width=10, font=("Arial", 11, "bold"), justify=CENTER)
		self.BoutonCalculerC3 = Button(self.FrameErlC3, text="Calculer", bg='blue', fg='white', font=("Arial", 12, "bold"), command=self.CalculerC3)

		#Dispositions 1
		self.LabelTeteC.grid(row=0, column=0, padx=7, pady=7, columnspan=2)
		self.LabTrafC.grid(row=1, column=0, padx=5, pady=5)
		self.ChampTrafC.grid(row=1, column=1, padx=5, pady=5)
		self.LabNbrCirC.grid(row=2, column=0, padx=5, pady=5)
		self.ChampNbrCirC.grid(row=2, column=1, padx=5, pady=5)
		#Dispositions 2
		self.LabelTeteC2.grid(row=0, column=0, padx=7, pady=7, columnspan=2)
		self.LabProbaAt.grid(row=1, column=0, padx=5, pady=5)
		self.ChampProbaAt.grid(row=1, column=1, padx=5, pady=5)
		self.LabTrafBt.grid(row=2, column=0, padx=5, pady=5)
		self.ChampTrafBt.grid(row=2, column=1, padx=5, pady=5)
		self.BoutonCalculerC2.grid(row=3, pady=15, columnspan=2)
		#dispositions 3
		self.LabelTeteC3.grid(row=0, column=0, padx=7, pady=7, columnspan=2)
		self.LabProbaAt3.grid(row=1, column=0, padx=5, pady=5)
		self.ChampProbaAt3.grid(row=1, column=1, padx=5, pady=5)
		self.LabNBc3.grid(row=2, column=0, padx=5, pady=5)
		self.ChampNBc3.grid(row=2, column=1, padx=5, pady=5)
		self.BoutonCalculerC3.grid(row=3, pady=15, columnspan=2)

		self.BoutonCalculerC.grid(row=3, pady=15, columnspan=2)
		self.BoutonQuitterC.grid(row=3, pady=15)
		
		self.RecommencerMenu2.grid(row=1,pady=5)
		self.FrameErlC.grid(row=0, column=0)
		self.FrameErlC2.grid(row=0, column=1)
		self.FrameErlC3.grid(row=0, column=2)
		self.FramePC.grid(row=2)

	def CalculerC(self):
		self.FrameResultat.destroy()
		self.FrameResultat = Frame(self.FramePC, bg='white')
		#labels de résultats
		self.LabProbaMiseAtt = Label(self.FrameResultat, text="Probabilité de MiseEn attente (%)", bg='white', fg='blue', font=("Arial", 13, "bold"))
		self.LabNbrMoyenClients = Label(self.FrameResultat, text="Nombre Moyen de clients", bg='white', fg='blue', font=("Arial", 13, "bold"))
		
		#Variables
		StringPbC = StringVar()
		StringNbM = StringVar()

		#Labels blancs
		self.LabNProbaMiseAt = Label(self.FrameResultat, textvariable=StringPbC, bg='white', font=("Arial", 13, "bold"))
		self.LabNMoyen = Label(self.FrameResultat, textvariable=StringNbM, bg='white', font=("Arial", 13, "bold"))

		

		inoo = 0
		try:
			trC = float(self.ChampTrafC.get())
			nbC = int(self.ChampNbrCirC.get())
			inoo = 1
		except:
			self.err()
		if(inoo==1):
			pb = erlangC(trC, nbC)
			f = fileAttente(trC, nbC)
			StringPbC.set(""+str(round(pb*100, 2)))
			StringNbM.set(""+str(round(f)))
			self.LabProbaMiseAtt.grid(row=0, column=0, padx=5, pady=5)
			self.LabNbrMoyenClients.grid(row=1, column=0, padx=5, pady=5)
			self.LabNProbaMiseAt.grid(row=0, column=1, pady=5)
			self.LabNMoyen.grid(row=1, column=1, pady=5)

			
			self.FrameResultat.grid(row=3, columnspan=3, pady=10)

	def CalculerC2(self):
		self.FrameResultat.destroy()
		self.FrameResultat = Frame(self.FramePC, bg='white')
		#labels de résultats
		self.LabNbrCir2 = Label(self.FrameResultat, text="Le nombre de Circuits est ", bg='white', fg='blue', font=("Arial", 15, "bold"))
		#Variables
		StringNc2 = StringVar()
		#Labels blancs
		self.LabNbrCirB2 = Label(self.FrameResultat, textvariable=StringNc2, bg='white', fg='blue', width=15, font=("Arial", 15, "bold"))
		
		#Récupération des entrees
		ino = 0
		try:
			pb = float(self.ChampProbaAt.get())
			traf = float(self.ChampTrafBt.get())
			#print(str(pb)+" "+str(traf))
			ino = 1
		except:
			self.err()
		if (ino==1):
			A = list()
			for k in range(9):
				A.append([])
				for l in range(51):
					A[k].append([])
			for k in range(9):
				for l in range(51):
					A[k][l] = 0
			fich = open("erlangC.txt", "r")
			for i in range(9):
				for j in range(51):
					A[i][j] = float(fich.readline())
			nbCir = nbCircuitsC(A, traf, pb, 9)
			StringNc2.set(""+str(nbCir))
			self.LabNbrCir2.grid(row=0, column=0, padx=5, pady=5)
			self.LabNbrCirB2.grid(row=0, column=1, padx=5, pady=5)


		self.FrameResultat.grid(row=2, columnspan=3, pady=10)

	def CalculerC3(self):
		self.FrameResultat.destroy()
		self.FrameResultat = Frame(self.FramePC, bg='white')
		#labels de résultats
		self.LabTrafB3 = Label(self.FrameResultat, text="Le Trafic offert est ", bg='white', fg='blue', font=("Arial", 15, "bold"))
		#Variables
		StringtrafB3 = StringVar()
		
		#Labels blancs
		self.LabNTrafB3 = Label(self.FrameResultat, textvariable=StringtrafB3, bg='white', fg='blue', width=15, font=("Arial", 15, "bold"))
		#Récupération des entrees
		ino = 0
		try:
			pb = float(self.ChampProbaAt3.get())
			Nbcr = int(self.ChampNBc3.get())
			ino = 1
		except:
			self.err()
		if(ino==1):
			A = list()
			for k in range(9):
				A.append([])
				for l in range(51):
					A[k].append([])
			for k in range(5):
				for l in range(51):
					A[k][l] = 0
			fich = open("erlangC.txt", "r")
			for i in range(5):
				for j in range(51):
					A[i][j] = float(fich.readline())
			tr = traficB(A, Nbcr, pb, 9)
			StringtrafB3.set(""+str(round(tr, 3)))
			self.LabTrafB3.grid(row=0, column=0, padx=5, pady=5)
			self.LabNTrafB3.grid(row=0, column=1, padx=5, pady=5)

		self.FrameResultat.grid(row=2, columnspan=3, pady=10)
		

dim = Dimensionnement()
