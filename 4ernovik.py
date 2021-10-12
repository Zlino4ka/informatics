from tkinter import *
from random import randrange as rnd, choice
import time

import pyautogui

root = Tk()
root.geometry('1080x720')
canv = Canvas(root, bg='#581845')
canv.pack(fill=BOTH, expand = 1)
canv2 = Canvas(root, bg='#581845')
canv2.pack()

colors = ['#DAF7A6', '#FFC300', '#FF5733', '#C70039', '#900C3F']

def printtext(score):
    print('YOUR SCORE', score)

def new_ball():
    """otrisovyvaet sharik"""
    global x, y, r
    play_zone.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)
    root.after(1000, new_ball)

def score(event):
    sc = 0
    while sc != 10:
        if (event.x < x+r or event.x > x-r) and (event.y < y+r or y > y-r):
            sc = sc + 1
        else:
            sc = sc + 0
        print(sc)

printtext(score)
new_ball()
canv2.create_text(100, 100, text='YOUR SCORE', fill='#DAF7A6', font='Helvetica 100 bold')
canv.bind('<Button-1>', score)

root.mainloop()



def score(event):
    global x,y,r
    n = 0
    while n != 100:
        getx, gety = pyautogui.position()
        sc = 0
        if (x+r > getx) and (getx > x-r) and (y+r > gety) and (gety > y-r):
            sc = sc + 1
            n = n + 1
        else:
            sc = sc + 0
            n = n + 0
    print(sc)