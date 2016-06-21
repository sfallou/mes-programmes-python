# -*- coding: utf-8 -*-
from Tkinter import *

n = 0 # Init matrix size (Global Variable)

def recherchepivot(k,A):
    i = k
    while i != n and A[i][k] == 0:
        i+=1
    if i != n:
        return i
    else:
        return -1

def permutation(i0,i,A,b):
    A[i],A[i0] = A[i0],A[i]
    b[i],b[i0] = b[i0],b[i]
    return A,b

def elimination(k,A,b):
    i=k+1
    while i < n:
        r = A[i][k]/A[k][k]        
        b[i] -= r*b[k]
        j=k
        while j < n:
            A[i][j] -= r*A[k][j]
            j+=1
        i+=1    
    return A,b

def remonte(A,b):
    x = []
    i = 0
    while i<n:
        x.append(0)
        i+=1        
    x[n-1] = b[n-1]/A[n-1][n-1]
    i = n-2
    while i>=0:    
        x[i] = b[i]            
        j = i+1
        while j<n:
            x[i] -= A[i][j]*x[j]
            j+=1            
        x[i]/=A[i][i]
        i-=1
    return x
    
# GRAPHIC USER INTERFACE USING TKINTER
class MainGUI:   
    def __init__ (self):
        #on cree notre fenetre
        windows = Tk()
        windows.title("Linear Equation Solver")
        # header
        header = Frame(windows)
        header.grid(row=0, column=0)
        #
        text="Donner la taille de la matrice"
        Label(header, text=text,  font="arial 13", padx=10, pady=20).grid(row=0, column=0)
        #
        self.tailleMatrice = IntVar()
        self.tailleMatrice.set(1)
        Entry(header, textvariable=self.tailleMatrice, width=5, font="arial 13", 
              justify=CENTER).grid(row=0, column=1)
        #
        Button(header, text="OK", width=3, bg="royal blue", fg="white",
               font=("Arial", 8, "bold"), command=self.matrixLen).grid(row=0, column=2)
        # zone saisie matrice
        self.matrixWindows = Frame(windows)
        self.matrixWindows.grid(row=1, column=0)
        self.selectedCase = ""
        #
        def click(event):
            self.selectedCase = event.widget
            self.selectedCase.focus_set()
            
        def press(event):
            oldValue = self.selectedCase["text"]
            if event.keysym == "BackSpace":
                newValue = oldValue[:-1]
            else:
                newValue = "{}{}".format(oldValue,eval(repr(event.char)))
                self.selectedCase.config(text=newValue)
            self.selectedCase.config(text=newValue)
                    
        def disableBinding(event):
            windows.unbind("<Key>")
        
        def enableBinding(event):
            windows.bind("<Key>", press)
            
        # binding event
        windows.bind("<Button-1>", click)
        header.bind("<Enter>", disableBinding)
        self.matrixWindows.bind("<Enter>", enableBinding)
        # footer
        self.footer = Frame(windows)
        self.footer.grid(row=2, column=0, padx=8, pady=8)
        #
        footerText = "Solveur d'un sytème d'équations linéaires"
        self.footerLabel = Label(self.footer, text=footerText, font="arial 10", fg="white", bg="black",
              width=55)
        self.footerLabel.grid(row=0, column=0)
        # Create an event loop
        windows.mainloop()
        
    ##### Class methods
    #
    def matrixLen(self):
        self.footerText = "Cliquer sur les X pour saisir"
        color = "blue"
        try:
            global n
            n = int(self.tailleMatrice.get())
            if n == 0:
                self.footerText = "* La taille de la matrice doit est être non nulle"
                color = "red"
            else:
                self.buildMatrix()
        except:
            self.footerText = "* La taille de la matrice doit être un entier"
            color = "red"
        # affichage message
        self.footerLabel.config(text=self.footerText, fg=color)
    #
    def buildMatrix(self):
        # matrice A     
        self.caseA = {}
        for i in range(n*n):
            # convert to string because backspace deal with string
            self.caseA[i] = Label(self.matrixWindows, text="X", font=("arial", 16), width=5)
            self.caseA[i].grid(row=int(i/n), column=1+i%n)
        # creation des parenthèses  
        bracket1 = Canvas(self.matrixWindows, width=10*n, height=30*n)
        bracket1.create_text(5*n, 13*n, anchor=CENTER, text="(", font=("Calibri Light", 24*n))
        bracket1.grid(row=0, column=0, rowspan=n)
        #
        bracket2 = Canvas(self.matrixWindows, width=10*n, height=30*n)
        bracket2.create_text(5*n, 13*n, anchor=CENTER, text=")", font=("Calibri Light", 24*n))
        bracket2.grid(row=0, column=n+1, rowspan=n)        
        #
        bracket3 = Canvas(self.matrixWindows, width=10*n, height=30*n)
        bracket3.create_text(5*n, 13*n, anchor=CENTER, text="(", font=("Calibri Light", 24*n))
        bracket3.grid(row=0, column=n+2, rowspan=n)
        # inconnues xi
        caseX = {}
        for i in range(n):
            caseX[i] = Label(self.matrixWindows, text="x{}".format(i+1), font=("arial", 16), width=5)
            caseX[i].grid(row=i, column=n+3)
        #
        bracket4 = Canvas(self.matrixWindows, width=10*n, height=30*n)
        bracket4.create_text(5*n, 13*n, anchor=CENTER, text=")", font=("Calibri Light", 24*n))
        bracket4.grid(row=0, column=n+4, rowspan=n)
        # signe égalité
        equalSymbol = Canvas(self.matrixWindows, width=40, height=30*n)
        equalSymbol.create_text(21, 15*n, anchor=CENTER, text="=", font=("arial", 8*n))
        equalSymbol.grid(row=0, column=n+5, rowspan=n)
        #
        bracket5 = Canvas(self.matrixWindows, width=10*n, height=30*n)
        bracket5.grid(row=0, column=n+6, rowspan=n)
        bracket5.create_text(5*n, 13*n, anchor=CENTER, text="(", font=("Calibri Light", 24*n))
        # vecteur b
        self.caseB = {}
        for i in range(n):
            self.caseB[i] = Label(self.matrixWindows, text="X", font=("arial", 16), width=5)
            self.caseB[i].grid(row=i, column=n+7)
        #
        bracket6 = Canvas(self.matrixWindows, width=10*n, height=30*n)
        bracket6.create_text(5*n, 13*n, anchor=CENTER, text=")", font=("Calibri Light", 24*n))
        bracket6.grid(row=0, column=n+8, rowspan=n)
        # solve button
        Button(self.footer, text="Résoudre", height=2, bg="royal blue", fg="white",
               font=("Arial", 10, "bold"), command=self.solveEquation).grid(row=0, column=1)
    #
    def solveEquation(self):
        # eval matrix elements
        A = []
        b = []
        for i in range(n):
            error = "ERREURS !"  
            # adding vector b elem
            try:            
                if self.caseB[i]["text"] == "X":
                    error += "\n * Remplacer tous les X par des nombres"     
                    self.footerLabel.config(text=error, fg="red", font="arial 10")                    
                    return 0  # stopping programm
                b.append(eval(self.caseB[i]["text"]))
            except:
                error += "\n * Tous les éléments de la matrice doivent être des nombres" 
                self.footerLabel.config(text=error, fg="red", font="arial 10")                
                return 0  # stopping programm
            # adding matrix A elem   
            A.append([])
            for j in range(n):
                try:
                    if self.caseA[i*n+j]["text"] == "X":
                        error += "\n * Remplacer tous les X par des nombres"     
                        self.footerLabel.config(text=error, fg="red", font="arial 10")                    
                        return 0  # stopping programm
                    A[i].append(eval(self.caseA[i*n+j]["text"]))
                except:
                    error += "\n * Tous les éléments de la matrice doivent être des nombres"
                    self.footerLabel.config(text=error, fg="red", font="arial 10")                  
                    return 0  # stopping programm
        # solve equation by GAUSS method
        k = 0
        arret = 0
        while k!=n and arret!=1:
            i0 = recherchepivot(k,A)
            if i0 == -1:
                arret = 1
            else:
                if i0 == k:
                    A,b = elimination(k,A,b)
                    k+=1
                else: 
                    A,b = permutation(i0,k,A,b)
                    A,b = elimination(k,A,b)
                    k+=1
        if k==n and A[n-1][n-1]!=0:
            # equation solutions
            x = remonte(A,b)
            result = "Ce système admet pour solution :"
            for i in range(n):
                result += "\n x{} = {}".format(i+1, x[i])          
        else:
            # no unique solution
            result = "Ce système n'admet pas de solution unique"
        # Showing results
        self.footerLabel.config(text=result, fg="blue", font="Helvetica 10 bold", justify=LEFT)
# run graphic user interface
MainGUI()
        
        
        
   
