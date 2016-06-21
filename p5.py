from tkinter import *

fp = Tk()                  # fenêtre principale
fp.title("Evénement Clavier et souris")

def clavier(ev):
    text1.insert(END, '<' + ev.keysym + '>\n')
    text1.see(END)
    return "break"          #pour que le caractère tapé ne soit pas affiché

def souris(ev):
    text1.insert(END,"[bouton , x , y] -->  " + str([ev.num, ev.x, ev.y])+'\n')
    text1.see(END)

def clrscr():
    text1.delete(1.0, END)

text1= Text(fp, width=30, height =20)

text1.bind("<Key>", clavier)
text1.bind("<Button>", souris)

text1.pack(fill='both', expand=1)
Button(fp, text='CLEAR', command = clrscr).pack(pady=5)
Button(fp, text='EXIT', command=fp.destroy).pack()
fp.mainloop()
