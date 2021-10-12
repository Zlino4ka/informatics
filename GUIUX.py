
from tkinter import *

root = Tk()

e = Entry(root, width=100)
b = Button(root, text="Преобразовать")
l = Label(root, bg='black', fg='white', width=100)

e.pack()
b.pack()
l.pack()

def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)

b.bind('<Button-1>', strToSortlist)

root.mainloop()

