from tkinter import *

def  effacer():
    EDIT.delete('1.0',END)

root = Tk()
EDIT = Text(root, width = 20, height=10)
EDIT.pack(pady=10)

Button(root, text='CLEAR 1', command = effacer).pack(pady=10)
Button(root, text='CLEAR 2', command = lambda: EDIT.delete('1.0',END)).pack(pady=10)
Button(root, text = 'EXIT', command = root.destroy).pack(pady = 10)
root.mainloop()
