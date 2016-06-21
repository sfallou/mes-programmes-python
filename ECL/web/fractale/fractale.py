# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------
    @Authors                                                      |
             Serigne Fallou NDIAYE  & Chuhan WANG                 |
             Jordan N'Guessan KONAN & Mingshan  ZHG               |
    @From: Ecole Centrale de Lyon                                 |
    @Prog: Projet d'Application web en Python                     |
    @Date: 08 - 06 - 2016                                         | 
-------------------------------------------------------------------
"""
########################## Début du programme  #################################

"""
-----------------------------------------------------------
Importation des bibliothèques utilisées dans ce programme |
-----------------------------------------------------------
"""
from PIL import Image
from PIL import ImageDraw
from random import *
import time
import sqlite3
import numpy as np

"""
-----------------------------------------------------------
                    Classe Percolation                    |
-----------------------------------------------------------
"""
class Percolation:
    def __init__(self,w,h,couleur): # initialisation de l'image
        self.__largeur=h            # sa taille w et h
        self.__hauteur=w
        self.__couleur=couleur      # la couleur des feuiles
        self.__image=Image.new("RGB",(w, h),"white") # l'image de la percolation
        self.__pixels = self.__image.load() # create the pixel map
        self.__nomImage="img_"+str(w)+"_"+str(h)+"_"+str(couleur[0])+"_"+str(couleur[1])+"_"+str(couleur[2])+".png"
        self.__pixelsPercolate=[]
        #initialisation de la derniere ligne
        #par contre l'image sera inclinée de 90° mais sera retournée a sa position avant l'enregistrement
        for k in range(self.__largeur):
            self.__pixels[self.__hauteur-1,k]=self.__couleur # initialisation 
    
    #envoie la liste des pixels percolorés
    def getPercolatedPixels(self):
        return self.__pixelsPercolate

    #Fonction qui change la couleur d'un pixel 
    def placerPixel(self,i,j):
        self.__pixels[i,j] = self.__couleur
        self.__pixelsPercolate.append((i,j))

    #Fonction qui verifie si le pixel est de couleur voulue
    def nonIdentique(self,i,j):
        if self.__image.getpixel((i,j))!=self.__couleur:
            return True
        return False

    #Fonction qui verifie si deux pixels sont voisins ou pas
    def estAcote(self,i,j,k,l):
        if (i+1,j)==(k,j) or (i-1,j)==(k,j) or (i,j+1)==(i,l):
            return True
        return False
    # Fonction descente
    def descente(self):
        stop=False # on atteint le haut de l'image
        while stop!=True:
            i=0
            j=choice([k for k in range((self.__largeur//2)-self.__largeur//3,(self.__largeur//2)+self.__largeur//3)])
            stop2=False # on pose le pixel
            while stop2!=True: # phase de descente
                if j>=self.__largeur-2:
                    if self.nonIdentique(i+1,j) and self.nonIdentique(i+1,j-1) and i!=self.__hauteur-1:
                        i=i+1 # on descend d'un cran                 
                        j=choice([j-1,j-2,j,j]) # on change de colonne aléatoirement
                    else: # on pose le pixel et on recommence
                        self.placerPixel(i,j)
                        stop2=True
                elif j<=1:
                    if self.nonIdentique(i+1,j) and self.nonIdentique(i+1,j+1) and i!=self.__hauteur-1: # on regarde dans les 3 cases inf
                        i=i+1 # on descend d'un cran            
                        j=choice([j,j+1,j+2]) # on change de colonne aléatoirement
                    else: # on pose le pixel et on recommence
                        self.placerPixel(i,j)
                        stop2=True
                else:
                    if self.nonIdentique(i+1,j) and self.nonIdentique(i+1,j-1) and self.nonIdentique(i+1,j+1) and i!=self.__hauteur-1:
                        i=i+1 # on descend d'un cran  
                        j=choice([j-2,j-1,j,j+1,j+2]) # on change de colonne aléatoirement
                    else: # on pose le pixel et on recommence
                        self.placerPixel(i,j)
                        stop2=True
            if i<self.__hauteur*0.2: # condition si on atteint le haut de l'image
                stop=True
        self.sauvegarderBDD()

    #Fonction qui sauvegarde l'image dans un dossier et dans la bdd
    def sauvegarderBDD(self):
        #self.__image=self.__image.rotate(-90,expand=1)
        self.__image=self.__image.transpose(Image.ROTATE_270)
        chemin='client/images/'+self.__nomImage
        self.__image.save(chemin, "PNG")
        #self.ajusterImage(chemin)
        conn = sqlite3.connect('percolation.sqlite')
        c = conn.cursor()
        c.execute('INSERT INTO image VALUES (NULL,?,?)',(self.__nomImage,chemin))
        conn.commit()
        conn.close()
        #self.__image.show()

#
########################## Fin de la classe #############################################

######### Fonction qui va vérifier si l'image demandée existe dans la base de données
def existeDansBDD(nom):
    conn = sqlite3.connect('percolation.sqlite')
    c = conn.cursor()
    c.execute("""SELECT * FROM image WHERE nom_image=?""",(nom,))
    lignes = c.fetchall()
    # on n'a rien trouvé
    if not len(lignes):
        return False
    return True
    
########### La fonction creerImage qui va renvoyer à l'utilisateur une image
########### provenant de la base de données si elle existe. Sinon la creer avec la classe 
########### Percolation définit ci dessus
def creerImage(w,h,couleur):
    r,g,b=couleur
    t0=time.clock()
    if (r,g,b)!=(255,255,55): # si la couleur des feuilles n'est pas blanche
        im="img_"+str(w)+"_"+str(h)+"_"+str(r)+"_"+str(g)+"_"+str(b)+".png"
        if existeDansBDD(im):
            print("Temps d'execution: ",time.clock()-t0)
            return 1    #on envoie 1 pour informer que ça vient de la BDD
        else:
            P=Percolation(w,h,(r,g,b))
            P.descente()
            print("Temps d'execution: ",time.clock()-t0)
            return 2    #on envoie 2 pour informer que ça a été générée
#########################################################################################
#                            Execution du programme principale                           #
##########################################################################################  
if __name__ == '__main__':
  creerImage(100,25,(5,255,5))
   