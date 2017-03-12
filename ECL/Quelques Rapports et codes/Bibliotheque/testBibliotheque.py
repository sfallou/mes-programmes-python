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
from Bibliotheque import *

"""
-----------------------------------------------------------
Teste de la classe Lecteur                                |
-----------------------------------------------------------
"""
############## Lecteur 1 ############
nom1="Konan"
prenom1="Jordan"
adresse1="U412 Comparat"
numeroLecteur1=1
lecteur1=Lecteur(nom1,prenom1,adresse1,numeroLecteur1)
############## Lecteur 2 ###########
nom2="Ndiaye"
prenom2="Fallou"
adresse2="X112 Comparat"
numeroLecteur2=2
lecteur2=Lecteur(nom2,prenom2,adresse2,numeroLecteur2)
############ On teste les méthodes de la classe Lecteur ############
print("******** Test de la classe Lecteur ****************")
print("******* Lecteur 1 **********")
print(lecteur1)
print("\n******* Lecteur 2 **********")
print(lecteur2)
######## on applique les méthodes au lecteur1 #############
lecteur1.setNom("Abba")
lecteur1.setPrenom("Ama")
lecteur1.setNumero(10)
lecteur1.setNbEmprunt(3)
lecteur1.setAdresse("Ecully")
print("\n********** Lecteur 1 après application des méthodes **********")
print(lecteur1)
print("\n************* FIN de la classe Lecteur ********************\n\n")


"""
-----------------------------------------------------------
Test de la classe Livre                                  |
-----------------------------------------------------------
"""
################### Classe Livre ##################
auteur="Olivier"
titre="Terre des hommes"
numeroLivre=5
nb_total=15
Livre1=Livre(auteur,titre,numeroLivre,nb_total)
print("******** Test de la classe Livre ****************\n")
print("******* Livre crée **********")
print(Livre1)
######## on applique les méthodes au livre #############
Livre1.setAuteur("Albert")
Livre1.setTitre("Terre des femmes")
Livre1.setNumeroLivre(25)
Livre1.setNbDispo(13)
print("\n********** Livre après application des méthodes **********")
print(Livre1)
print("\n************* FIN de la classe Livre***********\n")

"""
-----------------------------------------------------------
Test de la classe Bibliothèque                            |                 
-----------------------------------------------------------
"""
B=Bibliotheque("Michelle Serras")
B.ajouterLecteur("Ndiaye","Serigne","Comparat",50)
B.ajouterLivre("Hugo","Les misérables",30,8)
print("******** Test de la classe Bibliothèque ****************\n")
print(B)
print("Chercher Lecteur par son numéro (50) :",B.chercherLecteurByNumero(50))
print("Chercher Lecteur par son numéro (51) :",B.chercherLecteurByNumero(51))
print("Chercher Lecteur par son nom (Ndiaye):",B.chercherLecteurByNom("Ndiaye"))
print("Chercher Lecteur par son nom (Dupont):",B.chercherLecteurByNom("Dupont"))
print("Chercher Livre par son numéro (10):",B.chercherLivreByNumero(30))
print("Chercher Livre par son numéro (100):",B.chercherLivreByNumero(100))
print("Chercher Livre par son Titre (Les misérables): ",B.chercherLivreByTitre("Les misérables"))
print("Chercher Livre par son Titre (La nuit des tambours): ",B.chercherLivreByTitre("La nuit des tambours"))
print("\n")
print("Afficher Livres:",B.afficherLivres())
print("\n")
print("Afficher Lecteurs:",B.afficherLecteurs())
print("\n")
print("Afficher Emprunt:",B.afficherEmprunts())
print("\n")
print("Ajout Emprunt avec les bons numéros () :",B.ajouterEmprunt(30,50))
print("Ajout Emprunt avec de mauvais numéros () :",B.ajouterEmprunt(38,550))
print("\n")
print("Afficher Emprunt: ",B.afficherEmprunts())
print("\n")
print("Supprimer un Emprunt qui n'existe pas: ",B.supprimerEmprunt(15,50))
print("Supprimer un Emprunt qui existe : ",B.supprimerEmprunt(30,50))
print("\n")
print("Afficher Emprunt ",B.afficherEmprunts())
print("\n")
print("Retirer un Lecteur qui n'existe pas  (520):",B.retraitLecteur(520))
print("Retirer un Lecteur qui existe  (50):",B.retraitLecteur(50))
print(B)
