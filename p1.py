#!/usr/bin/python3


class Salut(object):

    def __init__(self, mot="Bonjour"):
        self.mot=mot

    def francais(self):
        print("Bonjour")
        
    def anglais(self):
        print("Good morning!")
        
    def arabe(self):
        print("Merhaba!")
        
    def allemand(self):
        print("Gouteune tagg!")
                    

if __name__=="__main__":
    s1=Salut();
    s1.francais();
    s1.anglais();
    s1.allemand();
    s1.arabe();
    

