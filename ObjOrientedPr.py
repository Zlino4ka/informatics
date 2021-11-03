from random import randrange as rnd, choice
import tkinter as tk
from tkinter import *
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='#B7C88E')
canv.pack(fill=tk.BOTH, expand=1)

l = Label(root, bg='#B7C88E', fg='white', width=20)

l.pack()

usernameEntry = Entry(root, width=50)
usernameEntry.pack()

t = ''

def to_label(event):
    '''
    Функция считывает имя пользователя и помещает его на отдельный label
    '''
    global t
    t = usernameEntry.get()
    usernameLabel.configure(text=t)
    usernameEntry.destroy()


usernameEntry.bind('<Return>', to_label)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.color = choice(['#FED67E', '#FDF8E8'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 80

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        global balls
        self.live -= 1
        self.vy -= abs(10 / 24)

        if self.x > 750 or self.x < 0:
            self.vx = -  self.vx

        if self.y > 500 or self.y < 50:
            self.vy = -  self.vy

        self.x += self.vx
        self.y -= self.vy
        self.set_coords()
        if self.live < 0:
            canv.delete(self.id)
            balls.pop(balls.index(self))

    def hittest(self, object):

        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """

        if ((self.x - object.x) ** 2 + (self.y - object.y) ** 2) ** 0.5 <= self.r + object.r:
            return True
        else:
            return False


class gun():
    def __init__(self):
        '''
       Инициализация пушки
        '''
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():

    def __init__(self):
        """ Инициализация новой цели. """
        self.dx = rnd(-10, 10)
        self.dy = rnd(-10, 10)

        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)

        x = self.x = rnd(600, 750)
        y = self.y = rnd(300, 400)
        r = self.r = rnd(20, 70)
        color = self.color = '#ECE5D1'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.delete(self.id)

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):

        if self.x > 700:
            self.dx = -self.dx
        if self.y > 450:
            self.dy = - self.dy
        if self.x < 100:
            self.dx = - self.dx
        if self.y < 100:
            self.dy = - self.dy
        self.y += self.dy
        self.x += self.dx
        self.set_coords()


screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
score = 0
n = 0


def new_game(event=''):
    global gun, t1, screen1, balls, bullet, score, n

    t1 = target()
    t2 = target()

    t1.live = 1
    t2.live = 1
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    while t1.live or t2.live or balls:
        t1.move()
        t2.move()
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                score += t1.points
                n += 1
                l['text'] = str(score)
                canv.itemconfig(screen1,
                                text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                bullet = 0
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                score += t2.points
                n += 1
                l['text'] = str(score)
                canv.itemconfig(screen1,
                                text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                bullet = 0
        canv.update()
        time.sleep(z)
        g1.targetting()
        g1.power_up()

    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(10, new_game)

new_game()

root.mainloop()

string = 'Игрок ' + t + ' уничтожил ' + str(score) + ' мишени(ей)' + '\n'
with open('results.txt', 'a') as f:
    f.write(string)