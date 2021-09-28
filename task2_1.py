
import pygame
from pygame.draw import *

def main():
    """запускает отрисовку изображения"""
    # Fill
    filling(screen, 204, 255, 204)
    # Sky
    win(screen, 204, 255, 255, 0, 0, 1080, 400)
    # House
    house(screen, 255, 204, 153, 153, 204, 255, 255, 128, 128, 150, 500, 300, 200)
    house_m(screen, 255, 204, 153, 153, 204, 255, 255, 128, 128, 450, 330, 200, 100)
    # Cloud
    cloud(screen, 255, 255, 255, 400, 200, 40)
    cloud(screen, 255, 255, 255, 100, 100, 40)
    cloud(screen, 255, 255, 255, 700, 100, 35)
    # Tree
    rect(screen, (51, 51, 0), (910, 500, 30, 150))
    tree(screen, 153, 204, 0, 890, 500, 40)
    rect(screen, (51, 51, 0), (710, 330, 20, 120))
    tree(screen, 153, 204, 0, 690, 330, 30)
    # Sun
    sun(screen, 255, 255, 153, 850, 120)

def filling(surface, r, g, b):
    """заливка холста; red, green, blue - цвет по RGB"""
    pygame.Surface.fill(surface, (r, g, b))

def base(surface, red, green, blue, x1, y1, x2, y2):
    """отрисовка основания дома; red, green, blue - цвет по RGB, (x1, y1, x2, y2) - (left, top, width, height)"""
    rect(surface, (red, green, blue), (x1, y1, x2, y2))
    rect(surface, (0, 0, 0), (x1, y1, x2, y2), 4)

def win(surface, red, green, blue, x1, y1, x2, y2):
    """отрисовка сегмента окна; red, green, blue - цвет по RGB, (x1, y1, x2, y2) - (left, top, width, height)"""
    rect(surface, (red, green, blue), (x1, y1, x2, y2))
    rect(surface, (0, 0, 0), (x1, y1, x2, y2), 4)

def roof(surface, red, green, blue, x1, y1, x2, y2):
    """отрисовка крыши; red, green, blue - цвет по RGB, (x1, y1, x2, y2) - координаты основания крыши"""
    polygon(surface, (red, green, blue), [(x1, y1), (x1 + x2, y1), (x1 + x2 // 2, y1 - 50)])
    polygon(surface, (0, 0, 0), [(x1, y1), (x1 + x2, y1), (x1 + x2 // 2, y1 - 50)], 4)

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
        circle(surface, (0, 0, 0), (x1, y1), rad, 4)
        x1 = x1 + rad
        n = n + 1
    n = 0
    x1 = x1 - 3 * rad
    while n != 2:
        circle(surface, (r, g, b), (x1, y1 - rad), rad)
        circle(surface, (0, 0, 0), (x1, y1 - rad), rad, 4)
        x1 = x1 + rad
        n = n + 1

def tree(surface, r, g, b, x1, y1, rad):
    """отрисовка дерева; red, green, blue - цвет по RGB, (x1, y1) - координаты центра, радиус"""
    kusok_of_tree(surface, r, g, b, x1, y1, rad)
    circle(surface, (r, g, b), (x1 + rad, y1 - rad), rad)
    circle(surface, (0, 0, 0), (x1 + rad, y1 - rad), rad, 4)
    kusok_of_tree(surface, r, g, b, x1, y1 - 2 * rad, rad)
    circle(surface, (r, g, b), (x1 + rad, y1 - 3 * rad), rad)
    circle(surface, (0, 0, 0), (x1 + rad, y1 - 3 * rad), rad, 4)

def kusok_of_tree(surface, r, g, b, x1, y1, rad):
    """отрисовка куска дерева; red, green, blue - цвет по RGB, (x1, y1) - координаты центра, радиус"""
    n = 0
    while n != 2:
        circle(surface, (r, g, b), (x1, y1), rad)
        circle(surface, (0, 0, 0), (x1, y1), rad, 4)
        x1 = x1 + 2 * rad
        n = n + 1

def sun(surface, r, g, b, x1, y1):
    """это кошмар!!! отрисовка дерева; red, green, blue - цвет по RGB, (x1, y1) - координаты центра, радиус"""
    polygon(screen, (r, g, b), [(x1, y1), (950, 120), (900, 20)])
    polygon(screen, (r, g, b), [(850, 50), (950, 50), (900, 140)])
    polygon(screen, (r, g, b), [(840, 80), (930, 135), (930, 25)])
    polygon(screen, (r, g, b), [(870, 25), (870, 135), (960, 80)])
    polygon(screen, (r, g, b), [(915, 20), (920, 120), (840, 100)])
    polygon(screen, (r, g, b), [(890, 20), (860, 110), (955, 100)])
    polygon(screen, (r, g, b), [(900, 120), (855, 35), (960, 65)])
    polygon(screen, (r, g, b), [(900, 120), (840, 60), (945, 35)])
    circle(screen, (r, g, b), (900, 80), 50)

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

main()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
