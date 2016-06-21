# -*- coding: utf-8 -*-
from Tkinter import *

def aide(root,scrollbar):
    liste = Listbox(root, yscrollcommand = scrollbar.set )
    liste.insert(END, "Texte")
    liste.insert(END, "Via SMS")
    liste.insert(END, "Page web")
    liste.grid(row=0, column=0)
    #liste.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command =liste.yview )

def texte(footLab):
    result = "Pour saisir cliquer sur les X\n ensuite donner la taille de la matrice\npuis cliquer sur OK" 
    footLab.config(text=result, fg="blue", font="Helvetica 10 bold", justify=LEFT) 
    
    
def sms():
    reponse = askyesno("Il semble que vous etes presse",
       "Donner votre telephone\u00a0? \n cliquer «oui» pout finir")
    if reponse :
        fen = Tk()
        Entry(fen,text= "", command= envoieSms)
        
def envoieSms():
    print "hello"