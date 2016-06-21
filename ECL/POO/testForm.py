# -*- coding: utf-8 -*-
from Forme import *
from Dessin import *

x=0
y=0
c="rouge"
l=10
h=5
d=8
######### Forme############
"""forme=Forme(x,y,c)
print(forme.getCentre())
print(forme.getCouleur())

forme.setCentre(-5,25)
forme.setCouleur("bleu")
print(forme.getCentre())
print(forme.getCouleur())

forme.deplacement(1,1)
print(forme.getCentre())"""

###### Rectangle #########
r=Rectangle(x,y,c,l,h)
"""print(r.getCentre())
print(r.getCouleur())
print(r.getDim())
print(r.perimetre())
print(r.surface())
print(r)
r.setCentre(5,25)
r.setCouleur("bleu")
r.setDim(100,52)
print(r.getCentre())
print(r.getCouleur())
print(r.getDim())
print(r.perimetre())
print(r.surface())
print(r)"""

###### Cercle #########
cer=Cercle(x,y,c,d)
"""print(cer.getCentre())
print(cer.getCouleur())
print(cer.getDim())
print(cer.perimetre())
print(cer.surface())
cer.setCentre(5,25)
cer.setCouleur("bleu")
cer.setDim(-5)
print(cer.getCentre())
print(cer.getCouleur())
print(cer.getDim())
print(cer.perimetre())
print(cer.surface())"""

###### Rectangle #########
carr=Carre(x,y,c,l)
"""print(carr.getCentre())
print(carr.getCouleur())
print(carr.getDim())
print(carr.perimetre())
print(carr.surface())
carr.setCentre(5,25)
carr.setCouleur("bleu")
carr.setDim(100)
print(carr.getCentre())
print(carr.getCouleur())
print(carr.getDim())
print(carr.perimetre())
print(carr.surface())"""
d=Dessin()
d.printForme()
print("************************")
d.addForme(r)
d.printForme()
print("************************")
d.addForme(cer)
d.printForme()
print("************************")
d.addForme(carr)
d.printForme()
print("************************")