# -*- coding: utf-8 -*-

from PIL import Image
from math import sqrt



im = Image.open("Image8.bmp")
px = im.load()
w,h = im.size

L_regions=[]



def split (px,x1,x2,y1,y2, seuil):
    """split est la fonction principale pour la partie split"""
    if x2-x1<4 or y2-y1<4:
        """Si la taille de la région est trop petite,
        on fait comme si elle était déjà homogène."""
        moyenne=moyenne_px(px,x1,x2,y1,y2)
        affect_couleur_image(px,x1,x2,y1,y2,moyenne)

    else:
        if homogene(px,x1,x2,y1,y2, seuil):
            """Si la région est suffisement homogène, on fusionne"""
            couleur = moyenne_px(px,x1,x2,y1,y2)
            affect_couleur_image(px,x1,x2,y1,y2,couleur)

        else:
            """sinon, on divise en 4 et on recommence"""
            (a1,b1,c1,d1) = (x1,x1 +int((x2-x1)/2)  ,  y1,y1 +int((y2-y1)/2))
            (a2,b2,c2,d2) = (x1+int((x2-x1)/2)+1,x2  ,  y1,y1 +int((y2-y1)/2))
            (a3,b3,c3,d3) = (x1,x1+int((x2-x1)/2)  ,  y1 +int((y2-y1)/2)+1,y2)
            (a4,b4,c4,d4) = (x1+int((x2-x1)/2)+1,x2  ,  y1 +int((y2-y1)/2)+1,y2)
            
            
            print((a1,b1,c1,d1),(a2,b2,c2,d2), (a3,b3,c3,d3),(a4,b4,c4,d4))
            
            
            split(px,a1,b1,c1,d1,seuil)
            split(px,a2,b2,c2,d2,seuil)
            split(px,a3,b3,c3,d3,seuil)
            split(px,a4,b4,c4,d4,seuil)
    

def moyenne_px(px,x1,x2,y1,y2):
    """renvoie la moyenne de r,v,b pour la région sélectionnée"""
    moyenne = [0,0,0]
    for i in range (x1,x2+1):
        for j in range (y1,y2+1):
            moyenne[0]+=px[i,j][0]
            moyenne[1]+=px[i,j][1]
            moyenne[2]+=px[i,j][2]
    
    moyenne[0]=moyenne[0]/((x2+1-x1)*(y2+1-y1))
    moyenne[1]=moyenne[1]/((x2+1-x1)*(y2+1-y1))
    moyenne[2]=moyenne[2]/((x2+1-x1)*(y2+1-y1))

    return(moyenne)
    
    
def ecart_type(px,x1,x2,y1,y2):
    """renvoie l'écart-type de r,v,b pour la région sélectionnée"""
    moyenne= moyenne_px(px,x1,x2,y1,y2)
    
    variance=[0,0,0]
    for i in range (x1,x2+1):
        for j in range (y1,y2+1):
            variance[0]+=(moyenne[0]-px[i,j][0])**2
            variance[1]+=(moyenne[1]-px[i,j][1])**2
            variance[2]+=(moyenne[2]-px[i,j][2])**2
    
    ecart_type=[0,0,0]
    ecart_type[0]=sqrt(variance[0]/((x2+1-x1)*(y2+1-y1)))
    ecart_type[1]=sqrt(variance[1]/((x2+1-x1)*(y2+1-y1)))
    ecart_type[2]=sqrt(variance[2]/((x2+1-x1)*(y2+1-y1)))
    
    return(ecart_type)


def homogene(px,x1,x2,y1,y2,seuil):
    """ définit l'homogénéité d'une région en fonction de seuil"""
    [r,g,b]=ecart_type(px,x1,x2,y1,y2)
    if (r+g+b)/3<seuil:
        return True 
    else:
        return False
        
        
def lecture (px,x,y):   #unused
    return px[x,y]

def affect_couleur(px,x,y,couleur):
    px[x,y]=int(couleur[0]),int(couleur[1]),int(couleur[2])
    
def affect_couleur_image(px,x1,x2,y1,y2,couleur):   #couleur est une matrice 1x3
    for i in range (x1,x2+1):
        for j in range (y1,y2+1):
            affect_couleur(px,i,j,couleur)

    if L_regions==[]:
        L_regions.append([0,x1,y1,x2,y2,couleur])
    else:
        L_regions.append([L_regions[-1][0]+1,x1,y1,x2,y2,couleur])


##################################################################
##################################################################
##################################################################


        
def homogene_region(region1,region2,seuil):
    [id1,x1,y1,x1p,y1p,[r1,v1,b1]]=region1
    [id2,x2,y2,x2p,y2p,[r2,v2,b2]]=region2
    
    moyenne=[(r1+r2)/2,(v1+v2)/2,(b1+b2)/2]
    ecart_type=[0,0,0]
    ecart_type[0]=sqrt(((moyenne[0]-r1)**2+(moyenne[0]-r2)**2)/2)
    ecart_type[1]=sqrt(((moyenne[1]-v1)**2+(moyenne[1]-v2)**2)/2)
    ecart_type[2]=sqrt(((moyenne[2]-b1)**2+(moyenne[2]-b2)**2)/2)
    
    
    [r,v,b]=ecart_type
    if (r+v+b)/3<seuil:
        return True 
    else:
        return False
        
    
    
def is_region_adj(region1,region2):
    """teste l'adjacence de deux regions de la forme : voir ci-dessous"""
    [id1,x1,y1,x1p,y1p,coul1]=region1
    [id2,x2,y2,x2p,y2p,coul2]=region2
    
    pix1=[x1-x2p+x2-1,y1-(x2p-x2+1)]
    pix_possible=[]
    for i in range (pix1[0],pix1[0]+(x2p-x2+1)+(x2p-x2+1)+1):
        pix_possible.append([i,y1-(x2p-x2+1)])   
        pix_possible.append([i,y1+1])
    
    for j in range (pix1[1]+1,pix1[1]+(x2p-x2+1)+(x1p-x1+1)):
        pix_possible.append([x1-(x2p-x2+1),j])   
        pix_possible.append([x1+(x1p-x1+1),j])
        
    return([x2,y2] in pix_possible)
      
        
def adjacences(L_regions,i):
    """retourne une liste de regions adjacentes à la region d'indice i"""
    adjacence = [i]    
    for region2 in L_regions:
        if region2[0]!=i and is_region_adj(region2,L_regions[i]):
            adjacence.append(region2[0])
    return adjacence
    
    

def RAL(L_regions):
    """retourne le RAL de l'image, sans souci de la couleur des régions"""
    liste = []
    for region1 in L_regions:
        liste.append(adjacences(L_regions,region1[0]))
    return liste
    
    




def nettoyer(region,seuil):    #region est un élément de RAL du type [0, 1, 2, 3]
    """nettoyer est une sous-fonction de modif_RAL"""
    def enlever_doublons(liste):
        
        element =liste[0]  #technique pour laisser le premier element en premiere position à la fin
        liste[1:]=liste
        
        aEnlever = []
        for i in liste:
            if i not in aEnlever and liste.count(i)>1:
                aEnlever.append(i)
        
        for j in aEnlever:
            for k in range (liste.count(j)-1):
                liste.remove(j)
                
                
        for k in range (liste.count(element)):
            liste.remove(element)       
                    
        return [element] + liste
    """supprimer les doublons dans region et""" 
    region = enlever_doublons(region)

    """enleve ceux de mauvaise couleur"""
    id_region_travail = region[0]
    liste=[]   #contient les id des regions qu'on souhaite remettre dans la liste a  faire
    new_region = [id_region_travail]
    
    for i in region[1:]:
        if homogene_region(L_regions[id_region_travail],L_regions[i],seuil):
            new_region.append(i)
        else:
            liste.append(i)
    return (new_region,liste)
    

def modif_RAL(L_regions, seuil):
    """transforme le RAL qui ne tient pas compte des couleurs 
    en RAL qui tient compte des couleurs"""
    
    liste_RAL = RAL(L_regions)  #[[0, 1, 2, 3], [1, 0, 2, 3]]
    liste_a_faire=list(range(0,len(liste_RAL)))   #liste numeros à faire  [0,1,2,3,4]
    id_region = 0
    liste_RAL2=[]
    
    while id_region<len(liste_RAL):
        if id_region in liste_a_faire:
            region = liste_RAL[id_region]

            
            for j in range (3):    #je fais 10 itérations naives
                for i in region[1:]:
                    if homogene_region(L_regions[i],L_regions[id_region],seuil):
                        region+= liste_RAL[i]
                [region,liste] = nettoyer(region,seuil)    
                    

                for i in range(0,len(liste_RAL)):
                    if i in region[1:]:
                        liste_a_faire[i]="D"

            liste_RAL2.append(region)
            
            print(region)
        
        id_region+=1
    
    print("Il y a désormais ",len(liste_RAL2), " régions.")
    
    return(liste_RAL2)



def merge(px,L_regions, seuil):
    
    def affect_couleur2(px,L_regions):
        for region in L_regions:     #region de la forme[1,23,23,42,45,[1,1,1]]
            for i in range(region[1],region[3]+1):
                for j in range(region[2], region[4]+1):
                    affect_couleur(px,i,j,region[-1])
                
    def niveler(element_ral2):
        data=[]
        for i in element_ral2:
            data.append(L_regions[i][-1])
        
        r,v,b=0,0,0
        for i in data:
            r+=i[0]
            v+=i[1]
            b+=i[2]
        r/=len(data)
        v/=len(data)
        b/=len(data)
    
        for i in element_ral2:
            L_regions[i][-1]=[r,v,b]
        
        
        
    ral2 = modif_RAL(L_regions, seuil)
    for element_ral2 in ral2:
        niveler(element_ral2)
        
    affect_couleur2(px,L_regions)

    print("Il y avait ",len(L_regions), " régions.")


##################################################################
##################################################################
##################################################################



seuil_split = 25
seuil_merge = 25


print("--------------------------------------------------------")
print("-------------DECOUPAGE DES ZONES : SPLIT----------------")
print("--------------------------------------------------------")

#mon ordinateur met 33 secondes pour faire cette phase avec image8 pour seuil = 25

split(px,0,w-1,0,h-1,seuil_split)


im.show()
im.save("test.jpg")



print("--------------------------------------------------------")
print("--------------------PHASE MERGE ------------------------")
print("--------------------------------------------------------")

merge(px,L_regions, seuil_merge)

im.show()
im.save("test2.jpg")

print("--------------------------------------------------------")
print("----------------FIN DE L'EXECUTION !!-------------------")
print("--------------------------------------------------------")