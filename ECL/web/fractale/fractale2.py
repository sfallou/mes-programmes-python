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
import math
import time
import sqlite3

class PercolationCentre:
    def __init__(self,R,couleur):    # R:rayon de l'etoile
        self.__rayon = R
        self.__r = couleur[0]
        self.__g = couleur[1]
        self.__b = couleur[2]
        self.__couleur = (self.__r,self.__g,self.__b,255)
        self.__image = Image.new("RGBA",(2*R+1,2*R+1),(255,255,255,255))
        self.__pixels = self.__image.load()
        self.__nomImage="imgcentre_"+str(R)+"_"+str(couleur[0])+"_"+str(couleur[1])+"_"+str(couleur[2])+".png"
        self.__pixelsPercolated=[]
        self.__lcentre = 3
        for i in range(R-self.__lcentre,R+self.__lcentre):
            for j in range(R-self.__lcentre,R+self.__lcentre):
                self.__pixels[i+1,j+1] = (100,30,0,255)
        
    def getPercolatedPixels(self):
        return self.__pixelsPercolated
        
    def placerPixel(self,r,i,j):
        a = r/self.__rayon
        
#        print(self.__r)
        self.__pixels[i,j] = (int(self.__r*a),int(self.__g*a),int(self.__b*a),255)
        self.__pixelsPercolated.append((i,j))
        
        
    def detecter(self,x,y):
        flag = True
#        print(x,y)
        if x <= 0:
            for i in [0,1]:
                for j in [-1,0,1]:
                    if i == 0 and j == 0:
                        flag = flag
                    elif self.__pixels[x+i,y+j][0]==0 or self.__pixels[x+i,y+j][1]==0 or self.__pixels[x+i,y+j][2]==0:
                        flag = False            
        elif x >= 2*self.__rayon-2:
            for i in [-1,0]:
                for j in [-1,0,1]:
                    if i == 0 and j == 0:
                        flag = flag
                    elif self.__pixels[x+i,y+j][0]==0 or self.__pixels[x+i,y+j][1]==0 or self.__pixels[x+i,y+j][2]==0:
                        flag = False
        elif y <= 0:
            for i in [-1,0,1]:
                for j in [0,1]:
                    if i == 0 and j == 0:
                        flag = flag
                    elif self.__pixels[x+i,y+j][0]==0 or self.__pixels[x+i,y+j][1]==0 or self.__pixels[x+i,y+j][2]==0:
                        flag = False      
        elif y >= 2*self.__rayon-1:
            for i in [-1,0,1]:
                for j in [-1,0]:
                    if i == 0 and j == 0:
                        flag = flag
                    elif self.__pixels[x+i,y+j][0]==0 or self.__pixels[x+i,y+j][1]==0 or self.__pixels[x+i,y+j][2]==0:
                        flag = False
        else:
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if i == 0 and j == 0:
                        flag = flag
                    elif self.__pixels[x+i,y+j][0]==0 or self.__pixels[x+i,y+j][1]==0 or self.__pixels[x+i,y+j][2]==0:
                        flag = False
        return flag
       
    def converge(self):
        flag1 = True
        while flag1 == True:
            r = self.__rayon
            ang1 = choice(range(360))*(math.pi)/180  #diviser le tour en 360 degree angle initiel
#            print(ang1)
            x = int(self.__rayon+r*math.cos(ang1))
            y = int(self.__rayon+r*math.sin(ang1))
            flag2 = True
            while flag2 == True:
                r = r-1
#                print(r)
                n = 100
                ang2 = choice(range(-n,n))*math.pi/(2*n*20)  #prendre un angle dans pi/20, ca determine la densite
                ang1 = ang1+ang2    #nouveau angle
                x = int(self.__rayon+r*math.cos(ang1))
                y = int(self.__rayon+r*math.sin(ang1))
#                print(x,y)
                flag2 = self.detecter(x,y)
                if int(abs(r*math.cos(ang1)-1))<=3 and int(abs(r*math.sin(ang1)-1))<=3:
#                    print(x,y)
                    flag2 = False
            self.placerPixel(r,x,y)
            if r >= self.__rayon-1:
                flag1 = False
#                print(self.__rayon)
#                print(r)
#                print(flag1)
        self.sauvegarderBDD()

    def sauvegarderBDD(self):
        
        chemin='client/images/'+self.__nomImage
        self.__image.save(chemin, "PNG")
        #self.ajusterImage(chemin)
        conn = sqlite3.connect('percolation.sqlite')
        c = conn.cursor()
        c.execute('INSERT INTO image VALUES (NULL,?,?)',(self.__nomImage,chemin))
        conn.commit()
        conn.close()

def existeDansBDD(nom):
    
    conn = sqlite3.connect('percolation.sqlite')
    c = conn.cursor()
    c.execute("""SELECT * FROM image WHERE nom_image=?""",(nom,))
    lignes = c.fetchall()
    # on n'a rien trouvé
    if not len(lignes):
        return False
    return True

def creerImage(R,r,g,b):
    
    t0=time.clock()
    if (r,g,b)!=(255,255,55): # si la couleur des feuilles n'est pas blanche
        couleur = (r,g,b)
        im="imgcentre_"+str(R)+"_"+str(r)+"_"+str(g)+"_"+str(b)+".png"
        if existeDansBDD(im):
            print("Temps d'execution: ",time.clock()-t0)
            return 1    #on envoie 1 pour informer que ça vient de la BDD
        else:
            P=PercolationCentre(R,couleur)
            P.converge()
            print("Temps d'execution: ",time.clock()-t0)
            return 2  
        

if __name__ == '__main__':
    creerImage(55,0,255,0)