
from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x600')

def main():
    """главная функция, запускает игру"""
    if rnd(0, 20) == 1: new_ball()
    motion()
    if notf:
        root.after(50, main)

def quit(event):
    """записывает результат и имя в таблицу, крашит главное окно"""
    global notf
    name = e.get()
    file = open('results.txt', 'a')
    file.write(name + ' ' + str(score) + "\n")
    file.close()
    notf = False
    root.destroy()

def new_ball():
    """рисует новые шарики, x,y - координаты появления, rx,ry - отвечают за перемещение + визуальная скорость"""
    global allBset
    x = rnd(100, 700)
    y = rnd(100, 400)
    r = rnd(30, 50)
    col = choice(colors)
    rx = rnd(-7, 7)
    ry = rnd(-7, 7)
    allBset.append([x, y, r, col, rx, ry]) #добавить значения нового шарика в сет
    currentBset.add(len(allBset) - 1) #минус от количества айтемов в сете после клика

def bombball(x, y, r):
    """рисует бомбу красивешной"""
    canv.create_oval(x - r, y - r, x + r, y + r, fill='black', width=0)
    canv.create_line(x, y, x + r, y - r, x + 2 * r, y - r, x + r, y - r // 7, x + 2 * r, y, smooth=1, width=3)
    canv.create_polygon(x + 2 * r // 3, y - r, x + r, y - 2 * r // 3, x + 2 * r // 3, y - r // 3, x + r // 3,
                        y - 2 * r //3, x + 2 * r // 3, y - r, fill='black', width=0)

def click(event):
    """считает поинты при клике; если цвет шара любой, кроме черного - +1, если цвет шара черный(бомба) - поинты 0"""
    global score, text, text1, canvb
    destrBset = set() #сет кликнутых шариков
    for n in currentBset: #для энного элемента в сете присутствующих шариков, далее [n]-номер элемента, [0]-номер позиции в сете
        x = allBset[n][0]
        y = allBset[n][1]
        r = allBset[n][2]
        col = allBset[n][3]
        if (x - event.x)**2 + (y - event.y)**2 <= r**2:
            if col == 'black':
                score = 0
                text = canv.create_text(420, 20, text='YOUR SCORE: ' + str(score), font='Helvetica 20 bold', fill='#581845')
                canvb = Canvas(root, bg='#FFC300', width=800, height=600) #канва для месседжа
                canvb.place(x=0, y=0)
                label2 = Label(canvb, bg='#FFC300', fg='#581845', font='Helvetica 30 bold', width=30) #лейбл месседжа
                label2['text'] = 'DO NOT CLICK ON BOMBS!'
                label2.place(x=60, y=280)
                root.after(1000, destroymes) #после 1000 убрать канву месседжа
            else:
                score += 1
                text = canv.create_text(420, 20, text='YOUR SCORE: ' + str(score), font='Helvetica 20 bold', fill='#581845')
            destrBset.add(n) #добавить новый кликнутый шарик элементом в сет кликнутых шариков
    currentBset.difference_update(destrBset) #обновить сет существующих шариков после клика

def destroymes():
    """убирает канву месседжа о клике по бомбе"""
    canvb.destroy()

def motion():
    """отрисовывает шарики, обновляет экран с учетом координат и направления"""
    global allBset, text
    canv.delete(ALL)
    text = canv.create_text(420, 20, text='YOUR SCORE: ' + str(score), font='Helvetica 20 bold', fill='#581845')
    for n in currentBset: #для энного элемента в сете существующих шариков
        rx = allBset[n][4]
        ry = allBset[n][5]
        allBset[n][0] = allBset[n][0] + rx
        allBset[n][1] = allBset[n][1] + ry
        x = allBset[n][0]
        y = allBset[n][1]
        r = allBset[n][2]
        if y - r <= 40 or y + r >= 450:
            allBset[n][5] = -ry
        if x - r <= 10 or x + r >= 790:
            allBset[n][4] = -rx
        col = allBset[n][3]
        if col == 'black':
            bombball(x, y, r)
        else:
            canv.create_oval(x-r, y-r, x+r, y+r, fill=col, width=0)


canv = Canvas(root, bg='#FFC300')
canv.pack(fill=BOTH, expand=1)
q = Button(root, text='QUIT THE GAME')
q.place(x=365, y=560)
label = Label(root, bg='#FFC300', fg='#581845', font='Helvetica 20 bold', width=40)
label['text'] = 'ENTER YOUR NICKNAME'
label.place(x=80, y=500)
e = Entry(root, width=30, bg='#581845', fg='#FFC300', font='Helvetica 10 bold')
e.place(x=315, y=535)

text = canv.create_text(420, 20, text=0, font='Helvetica 20 bold', fill='#581845')
text1 = canv.create_text(20, 220, font='Helvetica 40 bold', fill='#581845')
canv.bind('<Button-1>', click)
q.bind('<Button-1>',quit)

allBset = [] #все шарики
currentBset = set() #присутствующие шарики

notf = True #введен для куит-алгоритма

colors = ['#DAF7A6', '#FF5733', '#C70039', '#900C3F', 'black']
score = 0

main()

mainloop()