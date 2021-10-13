from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='#FFC300')
canv.pack(fill=BOTH, expand=1)

colors = ['#DAF7A6', '#FF5733', '#C70039', '#900C3F']

def new_ball():
    global x,y,r,ball,x1,y1,r1,ball1
    canv.delete(ball)
    canv.delete(ball1)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    x1 = rnd(100, 700)
    y1 = rnd(100, 500)
    r1 = rnd(30, 50)
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    ball1 = canv.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill=choice(colors), width=0)
    root.after(1500,new_ball)

def move():
    global x, y, r, ball, x1, y1, r1, ball1
    for i in range(100):
        p = rnd(10,100)
        q = rnd(10,100)
        canv.move(ball,x-r+p,y-r+q)
        canv.move(ball1, x1 - r1 + p, y1 - r1 + q)
        canv.update()

def click(event):
    global points, x, x1, y, y1, r, r1, text
    if (event.y - y) ** 2 + (event.x - x) ** 2 <= r ** 2:
        points += 1
        x = -1000
        canv.delete(text)
        canv.delete(ball)
        text = canv.create_text(420, 20, text='YOUR SCORE: ' + str(points), font='Helvetica 20 bold', fill='#581845')
    elif (event.y - y1) ** 2 + (event.x - x1) ** 2 <= r1 ** 2:
        points += 1
        x = -1000
        canv.delete(text)
        canv.delete(ball1)
        text = canv.create_text(420, 20, text='YOUR SCORE: '+str(points), font='Helvetica 20 bold', fill='#581845')

ball = canv.create_oval(-100, 0, 0, 0)
ball1 = canv.create_oval(-100, 0, 0, 0)
text = canv.create_text(420, 20, text=0, font='Helvetica 20 bold', fill='#581845')
points = 0
new_ball()
canv.bind('<Button-1>', click)

mainloop()