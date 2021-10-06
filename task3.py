
import pygame
from pygame.draw import *

def main():
    """запускает отрисовку изображения"""
    # Fill
    filling(screen, 204, 255, 204)
    # Sky
    sky(screen, 204, 255, 255, 0, 0, 1080, 400)

    # House
    house(screen, 255, 204, 153, 153, 204, 255, 255, 128, 128, 150, 500, 300, 200)
    house_m(screen, 255, 204, 153, 153, 204, 255, 255, 128, 128, 450, 330, 200, 100)
    # Cloud
    cloud_animated(screen, 255, 255, 255, 400, 200, 40)
    cloud_animated(screen, 255, 255, 255, 100, 100, 40)
    cloud_animated_g(screen, 51, 102, 153, 700, 100, 35)
    rain(screen, 51, 102, 153, 800, 100, 800, 400)
    # Tree
    stvol_animated(screen, 51, 51, 0, 700, 330, 50, 120)
    tree_animated(screen, 153, 204, 0, 690, 330, 30)
    stvol_animated(screen, 51, 51, 0, 900, 500, 50, 150)
    tree_animated(screen, 153, 204, 0, 890, 500, 40)
    # Sun
    screen2 = pygame.Surface((720, 1080), 32)
    screen.blit(screen2, (0, 0))
    #screen2.set_alpha(0)
    sun(screen2, 255, 255, 153, 850, 120)
    sun_animated(screen2)

def filling(surface, r, g, b):
    """заливка холста; red, green, blue - цвет по RGB"""
    pygame.Surface.fill(surface, (r, g, b))

def base(surface, red, green, blue, x1, y1, x2, y2):
    """отрисовка основания дома; red, green, blue - цвет по RGB, (x1, y1, x2, y2) - (left, top, width, height)"""
    rect(surface, (red, green, blue), (x1, y1, x2, y2))

def sky(surface, red, green, blue, x1, y1, x2, y2):
    """отрисовка сегмента окна; red, green, blue - цвет по RGB, (x1, y1, x2, y2) - (left, top, width, height)"""
    rect(surface, (red, green, blue), (x1, y1, x2, y2))

def win(surface, red, green, blue, x1, y1, x2, y2):
    """отрисовка сегмента окна; red, green, blue - цвет по RGB, (x1, y1, x2, y2) - (left, top, width, height)"""
    rect(surface, (red, green, blue), (x1, y1, x2, y2))
    rect(surface, (51, 102, 204), (x1, y1, x2, y2), 4)

def roof(surface, red, green, blue, x1, y1, x2, y2):
    """отрисовка крыши; red, green, blue - цвет по RGB, (x1, y1, x2, y2) - координаты основания крыши"""
    polygon(surface, (red, green, blue), [(x1, y1), (x1 + x2, y1), (x1 + x2 // 2, y1 - 50)])

def house(surface, r_base, g_base, b_base, r_win, g_win, b_win, r_roof, g_roof, b_roof, x1, y1, x2, y2):
    """отрисовка дома; red, green, blue - цвет по RGB, (x1, y1, x2, y2) - координаты"""
    base(surface, r_base, g_base, b_base, x1, y1, x2, y2)
    roof(surface, r_roof, g_roof, b_roof, x1, y1, x2, y2)
    win(surface, r_win, g_win, b_win, (x1 + 80), (y1 + 50), (x2 // 4), (y2 // 4))
    win(surface, r_win, g_win, b_win, (x1 + 155), (y1 + 50), (x2 // 4), (y2 // 4))
    win(surface, r_win, g_win, b_win, (x1 + 80), (y1 + 100), (x2 // 4), (y2 // 4))
    win(surface, r_win, g_win, b_win, (x1 + 155), (y1 + 100), (x2 // 4), (y2 // 4))

def cloud(surface, r, g, b, x1, y1, rad):
    """отрисовка облака; red, green, blue - цвет по RGB, (x1, y1) - координаты центра, радиус"""
    n = 0
    while n != 4:
        circle(surface, (r, g, b), (x1, y1), rad)
        x1 = x1 + rad
        n = n + 1
    n = 0
    x1 = x1 - 3 * rad
    while n != 2:
        circle(surface, (r, g, b), (x1, y1 - rad), rad)
        x1 = x1 + rad
        n = n + 1

def cloud_animated(surface, r, g, b, x1, y1, rad):
    n = 0
    while n != 1:
        for i in range(-50, 1200):
            x = i
            rect(screen, (204, 255, 255), (0, y1 - 80, 1080, 130))
            cloud(surface, r, g, b, x, y1, rad)
            pygame.display.update()
            clock.tick(300)
        x = 0
        n = n + 1

def cloud_animated_g(surface, r, g, b, x1, y1, rad):
    n = 0
    while n != 1:
        for i in range(-50, 800):
            x = i
            rect(screen, (204, 255, 255), (0, y1 - 80, 1080, 130))
            cloud(surface, r, g, b, x, y1, rad)
            pygame.display.update()
            clock.tick(300)
        x = 0
        n = n + 1

def rain(surface, r, g, b, x1, y1, x2, y2):
    n = 0
    while n != 4:
        for i in range(100, 450):
            line(surface, (r, g, b), (x1, y1), (x2 - 30, y2), 2)
            pygame.display.update()
            clock.tick(800)
        n = n + 1
        x1 = x1 + 30
        x2 = x2 + 30

def tree(surface, r, g, b, x1, y1, rad):
    """отрисовка дерева; red, green, blue - цвет по RGB, (x1, y1) - координаты центра, радиус"""
    kusok_of_tree(surface, r, g, b, x1, y1, rad)
    circle(surface, (r, g, b), (x1 + rad, y1 - rad), rad)
    kusok_of_tree(surface, r, g, b, x1, y1 - 2 * rad, rad)
    circle(surface, (r, g, b), (x1 + rad, y1 - 3 * rad), rad)

def tree_animated(surface, r, g, b, x1, y1, rad):
    for i in range(1, 40):
        rad = i
        tree(surface, r, g, b, x1, y1, rad)
        pygame.display.update()
        clock.tick(10)

def kusok_of_tree(surface, r, g, b, x1, y1, rad):
    """отрисовка куска дерева; red, green, blue - цвет по RGB, (x1, y1) - координаты центра, радиус"""
    n = 0
    while n != 2:
        circle(surface, (r, g, b), (x1, y1), rad)
        x1 = x1 + 2 * rad
        n = n + 1

def stvol_animated(surface, red, green, blue, x1, y1, x2, y2):
    for i in range(1, 50):
        x = i
        rect(surface, (red, green, blue), (x1, y1, x, y2))
        pygame.display.update()
        clock.tick(100)

def sun(surface, r, g, b, x1, y1):
    """это кошмар!!! отрисовка дерева; red, green, blue - цвет по RGB, (x1, y1) - координаты центра, радиус"""
    polygon(surface, (r, g, b), [(x1-700, y1), (250, 120), (200, 20)])
    polygon(surface, (r, g, b), [(150, 50), (250, 50), (200, 140)])
    polygon(surface, (r, g, b), [(140, 80), (230, 135), (230, 25)])
    polygon(surface, (r, g, b), [(170, 25), (170, 135), (260, 80)])
    polygon(surface, (r, g, b), [(215, 20), (220, 120), (140, 100)])
    polygon(surface, (r, g, b), [(190, 20), (160, 110), (255, 100)])
    polygon(surface, (r, g, b), [(200, 120), (155, 35), (260, 65)])
    polygon(surface, (r, g, b), [(200, 120), (140, 60), (245, 35)])
    circle(surface, (r, g, b), (200, 80), 50)

def sun_animated(surface):
    n = 0
    while n != 2:
        pygame.transform.rotate(surface, 180)
        pygame.display.update()
        clock.tick(100)
        n = n + 1

def house_m(surface, r_base, g_base, b_base, r_win, g_win, b_win, r_roof, g_roof, b_roof, x1, y1, x2, y2):
    """отрисовка дома; red, green, blue - цвет по RGB, (x1, y1, x2, y2) - координаты"""
    base(surface, r_base, g_base, b_base, x1, y1, x2, y2)
    roof(surface, r_roof, g_roof, b_roof, x1, y1, x2, y2)
    win(surface, r_win, g_win, b_win, (x1 + 48), (y1 + 25), (x2 // 4), (y2 // 4))
    win(surface, r_win, g_win, b_win, (x1 + 98), (y1 + 25), (x2 // 4), (y2 // 4))
    win(surface, r_win, g_win, b_win, (x1 + 48), (y1 + 50), (x2 // 4), (y2 // 4))
    win(surface, r_win, g_win, b_win, (x1 + 98), (y1 + 50), (x2 // 4), (y2 // 4))

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1080, 800))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

main()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()