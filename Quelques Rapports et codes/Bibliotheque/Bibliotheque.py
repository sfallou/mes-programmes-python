# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------
@Authors: Serigne Fallou NDIAYE  & Jordan N'Guessan Ziahi KONAN   |
@From: Ecole Centrale de Lyon                                     |
@Prog: POO : Bibliothèque                                         |
@Date: 05 - 04 - 2016                                             |	
-------------------------------------------------------------------
"""
########################## Début du programme  #################################

"""
-----------------------------------------------------------
Importation des bibliothèques utilisées dans ce programme |
-----------------------------------------------------------
"""
from datetime import *

"""
-----------------------------------------------------------
					Classe Personne                       |
-----------------------------------------------------------
"""

class Personne:
	def __init__(self,nom,prenom,adresse):
		self.__nom=nom
		self.__prenom=prenom
		self.__adresse=adresse

	def getNom(self):
		return self.__nom

	def getPrenom(self):
		return self.__prenom

	def getAdresse(self):
		return self.__adresse

	def setNom(self,new_nom):
		self.__nom=new_nom

	def setPrenom(self,new_prenom):
		self.__prenom=new_prenom

	def setAdresse(self,new_adresse):
		self.__adresse=new_adresse

############################################################	
	
"""
-----------------------------------------------------------
			Classe Lecteur héritant de Personne           |
-----------------------------------------------------------
"""


class Lecteur(Personne):
	def __init__(self,nom,prenom,adresse,numero):
		Personne.__init__(self,nom,prenom,adresse)
		#if isinstance(numero,int):
		self.__numero=numero
		self.__nbEmprunt=0

	def getNumero(self):
		return self.__numero

	def getNbEmprunt(self):
		return self.__nbEmprunt

	def setNumero(self,new_num):
		self.__numero=new_num

	def setNbEmprunt(self,new_nbEmprunt):
		self.__nbEmprunt=new_nbEmprunt

	def __str__(self):
		return '\n Numero={}|Nom={}|Prenom={}|Adresse={}|Nb Emprunt={}\n'.format(self.getNumero(),self.getNom(),self.getPrenom(),self.getAdresse(),self.getNbEmprunt())

###############################################################################

"""
-----------------------------------------------------------
					Classe Livre                          |
-----------------------------------------------------------
"""

class Livre:
	def __init__(self,auteur,titre,numeroLivre,nbTotal):
		self.__auteur=auteur
		self.__titre=titre
		self.__numeroLivre=numeroLivre
		self.setNbTotal(nbTotal)
		self.setNbDispo(nbTotal)

	def getAuteur(self):
		return self.__auteur

	def getTitre(self):
		return self.__titre

	def getNumeroLivre(self):
		return self.__numeroLivre

	def getNbTotal(self):
		return self.__nbTotal

	def getNbDispo(self):
		return self.__nbDispo

	def setAuteur(self,new_auteur):
		self.__auteur=new_auteur

	def setTitre(self,new_titre):
		self.__titre=new_titre

	def setNumeroLivre(self,new_numeroLivre):
		self.__numeroLivre=new_numeroLivre

	def setNbTotal(self,nb):
		self.__nbTotal=nb

	def setNbDispo(self,new_nbDispo):
		self.__nbDispo=new_nbDispo

	def __str__(self):
		return '\n Numero={}|Titre={}|Auteur={}|Nb Total={}|Nombre_Disponible={}\n'.format(self.__numeroLivre,self.__titre,self.__auteur,self.__nbTotal,self.__nbDispo)


##################################################################################

"""
-----------------------------------------------------------
					Classe Emprunt                        |
-----------------------------------------------------------
"""


class Emprunt():
	def __init__(self,numeroLivre,numeroLecteur):
		self.__numeroLivre=numeroLivre
		self.__numeroLecteur=numeroLecteur
		self.__date=date.isoformat(date.today())

	def getNumeroLivre(self):
		return self.__numeroLivre

	def getNumeroLecteur(self):
		return self.__numeroLecteur

	def getDate(self):
		return self.__date

	def setNumeroLivre(self,no_livre):
		self.__numeroLivre=no_livre

	def setNumeroLecteur(self,no_lecteur):
		self.__numeroLecteur=no_lecteur

	def __str__(self):
		return'\n Date:{}|N°Livre={}|N°Lecteur={} '.format(self.__date,self.__numeroLivre,self.__numeroLecteur)
#################################################################################

"""
-----------------------------------------------------------
					Classe Bibliotheque                   |
-----------------------------------------------------------
"""

class Bibliotheque:
	def __init__(self,nomBiblio):
		self.__nomBiblio=nomBiblio
		# On préfère utiliser les dictionnaires pour matérialiser la relation 
		# de composition qui lie la classe Bibliotheque aux autres classes
		self.__Lecteurs={}
		self.__Livres={}
		self.__Emprunts={}

########### Getters #################
	def getNomBiblio(self):
		return self.__nomBiblio

	def getLivres(self):
		return self.__Livres

	def getLecteurs(self):
		return self.__Lecteurs

	def getEmprunts(self):
		return self.__Emprunts

########### Setters ##################
	def setNomBiblio(self,nom_biblio):
		self.__nomBiblio=nom_biblio

########## Autres methodes ###########

	def ajouterLecteur(self,nom,prenom,adresse,numero):
		if type(numero)==int:
			l=Lecteur(nom,prenom,adresse,numero)
			self.__Lecteurs[numero]=l
			return True
		return False

	def ajouterLivre(self,auteur,titre,numeroLivre,nbTotal):
		if type(numeroLivre)==int:
			livr=Livre(auteur,titre,numeroLivre,nbTotal)
			self.__Livres[numeroLivre]=livr
			return True
		return False
	
	def ajouterEmprunt(self,numeroLivre,numeroLecteur): 
		if type(numeroLivre)==int and type(numeroLecteur)==int: # on vérifie que les numeros sont des entiers
			rep,livre=self.chercherLivreByNumero(numeroLivre) # on cherche si le livre existe
			rep2,Lecteur=self.chercherLecteurByNumero(numeroLecteur) #on vérifie si le lecteur existe
			if rep and rep2 and livre.getNbDispo()>=1:  # on s'assure que le livre et le lecteur existent et que le nombre d'exemplaire dispo > 0
				empr=Emprunt(numeroLivre,numeroLecteur) # on crée un objet emprunt qu'on va ajouter dans la liste emprunt
				self.__Emprunts[(empr.getDate(),numeroLecteur,numeroLivre)]=empr
				livre.setNbDispo(livre.getNbDispo()-1) # on décrémente le nombre d'exemplaire disponible
				return True
		return False

	def supprimerEmprunt(self,numeroLivre,numeroLecteur):
		if type(numeroLivre)==int and type(numeroLecteur)==int: # on vérifie que les numeros sont entiers
				empr=Emprunt(numeroLivre,numeroLecteur) # on crée un objet emprunt 
				if (empr.getDate(),empr.getNumeroLecteur(),empr.getNumeroLivre()) in self.__Emprunts:  # on verifie que le livre est dans la liste des emprunts
					del self.__Emprunts[(empr.getDate(),empr.getNumeroLecteur(),empr.getNumeroLivre())]
					rep,livre=self.chercherLivreByNumero(numeroLivre) # on récupère l'objet livre correspondant
					livre.setNbDispo(livre.getNbDispo()+1) # on incrémente le nombre d'exemplaire disponible
					return True
		return False

	def chercherLecteurByNumero(self,num):
		if num in self.__Lecteurs:
			return True,self.__Lecteurs.get(num)
		return False,None

	def chercherLecteurByNom(self,nom):
		LesLect=[]        # on renvoie une liste car il peut y avoir plusieurs lecteurs de même nom
		booleen=False
		for num in self.__Lecteurs.keys():
			if nom==self.__Lecteurs.get(num).getNom():
				LesLect.append(str(self.__Lecteurs.get(num)))
		if len(LesLect)!=0:
			booleen=True
		return booleen,LesLect

	def chercherLivreByNumero(self,num):
		if num in self.__Livres:
			return True,self.__Livres.get(num)
		return False,None

	def chercherLivreByTitre(self,titre):
		for num in self.__Livres.keys():
			if titre==self.__Livres.get(num).getTitre():
				return True,str(self.__Livres.get(num))
		return False,None
	

	def retraitLecteur(self,numLecteur):
		rep,l=self.chercherLecteurByNumero(numLecteur)
		if not rep:
			return 0 # on renvoie 0 comme code d'erreur pour dire que l'utilisateur n'existe pas
		if numLecteur not in self.__Emprunts:
			del self.__Lecteurs[numLecteur]
			return 1 # on renvoie 1 comme code de réponse pour dire que le retrait s'est bien effectué
		else:
			return -1 # on renvoie -1 pour dire que l'utisateur ne peut pas etre supprimé car il a des emprunts
	
	def afficherLivres(self):
		Liste=list(self.__Livres.values())
		n=len(Liste)
		L=[]
		for i in range(n):
			L.append(str(Liste[i]))
		return L

	def afficherLecteurs(self):
		Liste=list(self.__Lecteurs.values())
		n=len(Liste)
		L=[]
		for i in range(n):
			L.append(str(Liste[i]))
		return L

	def afficherEmprunts(self):
		Liste=list(self.__Emprunts.values())
		n=len(Liste)
		L=[]
		for i in range(n):
			L.append(str(Liste[i]))
		return L

	def __str__(self):
		return '\n\nNom Bibliotheque: {}\nNombre de livres:{}\nNombre de Lecteurs:{}\nNombre emprunt:{}\n'.format(self.__nomBiblio,len(self.__Livres),len(self.__Lecteurs),len(self.__Emprunts))