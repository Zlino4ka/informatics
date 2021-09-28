
import pygame
from pygame.draw import *

def filling(surface, r, g, b):
    """red, green, blue - цвет по RGB, surface - поверхность"""
    pygame.Surface.fill(surface, (r, g, b))

def base(surface, r, g, b, x1, y1, x2, y2):
    rect(screen, (r, g, b), (x1, y1, x2, y2))


pygame.init()

FPS = 30
screen = pygame.display.set_mode((1080, 800))

filling(screen, 0, 0, 0)
base(screen, 255, 255, 255, 350, 200, 300, 200)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()