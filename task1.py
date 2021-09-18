
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1080, 800))

pygame.Surface.fill(screen, (204,255,255))
circle(screen,(255,255,0),(500,400),200)
circle(screen,(255,0,0),(430,330),40)
circle(screen,(0,0,0),(430,330),20)
circle(screen,(255,0,0),(590,330),30)
circle(screen,(0,0,0),(590,330),15)
polygon(screen,(0,0,0),[(290,210),(290,240),(480,310),(480,280)])
polygon(screen,(0,0,0),[(550,315),(540,295),(700,240),(710,260)])
rect(screen,(0,0,0),(400,470,200,30))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


