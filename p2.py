#!/usr/bin/python3

from tkinter import *
root = Tk()
W1 = Toplevel(root, bg='gold', cursor = 'X_cursor')
W2 = Toplevel(root, bg='azure', cursor = 'man', pady=10)    
root.geometry('400x100+100+100')
W1.geometry('400x100+100+250')
W2.geometry('400x200+100+400') 
root.title('Fenêtre Principale')
W1.title('Fenêtre 1')
W2.title('Fenêtre 2')   
B1 = Button(root, text= ' BOUTON FP').pack(pady = 10)
B2 = Button(W1, text= ' BOUTON W1').pack(pady = 10)
B3 = Button(W2, text= ' BOUTON W2').pack(pady = 10)    
W1.maxsize(500, 400)
W2.minsize(150, 100)    
root. mainloop()

    
    

