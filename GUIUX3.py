
from tkinter import *
from random import randrange as rnd, choice
import pyautogui

def start(event):
    play_zone.place(x=0,y=0)
    play_zone.mainloop()

def quit(event):
    play_zone.destroy()

def score(event):
    getx, gety = pyautogui.position()
    print(getx, gety)
    sc = 0
    if (p+r > getx > p-r) and (q+r > gety > q-r):
        sc = sc + 1
        print(sc)
    else:
        sc = sc + 0
        print(sc)

def new_ball():
    """otrisovyvaet sharik"""
    global p, q, r
    play_zone.delete(ALL)
    play_zone.create_text(520, 50, text='your score:', fill='#581845', font='Helvetica 20 bold')
    play_zone.create_text(520, 50, text=str(score), fill='#581845', font='Helvetica 20 bold')

    quitb = Button(play_zone, text='quit game')
    quitb.bind('<Button-1>', quit)
    quitb.place(x=540, y=700)

    p = rnd(100, 700)
    q = rnd(100, 500)
    r = rnd(30, 50)
    play_zone.create_oval(p-r, q-r, p+r, q+r, fill=choice(colors), width=0)
    root.after(2000, new_ball)


root = Tk()
root.geometry('1080x720')

start_canv = Canvas(root, bg='#581845')
start_canv.create_text(540, 300, text='click to start a game', fill='#DAF7A6', font='Helvetica 40 bold')
start_canv.pack(fill='both', expand=1)

sb = Button(start_canv, text='START')
sb.place(x=540, y=360)

play_zone = Canvas(root, bg='#FFC300', width=1080, height=720)

colors = ['#DAF7A6', '#FF5733', '#C70039', '#900C3F']

sb.bind('<Button-1>', start)

play_zone.bind('<Button-1>', score)

new_ball()

root.mainloop()