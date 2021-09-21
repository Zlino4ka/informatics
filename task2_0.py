
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1080, 800))

#Fill
pygame.Surface.fill(screen, (204, 255, 204))

#Sky
rect(screen, (204, 255, 255), (0, 0, 1080, 400))

#House
rect(screen, (255, 204, 153), (200, 300, 300, 220))
rect(screen, (255, 153, 0), (200, 300, 300, 220), 4)
polygon(screen, (255, 128, 128), [(200, 300), (500, 300), (350, 200)])
polygon(screen, (255, 0, 0), [(200, 300), (500, 300), (350, 200)], 4)
rect(screen, (153, 204, 255), (300, 370, 100, 80))
rect(screen, (0, 102, 204), (300, 370, 100, 80), 4)

#Cloud
circle(screen,(255,255,255),(600,200),40)
circle(screen,(192,192,192),(600,200),40,4)
circle(screen,(255,255,255),(650,200),40)
circle(screen,(192,192,192),(650,200),40,4)
circle(screen,(255,255,255),(700,200),40)
circle(screen,(192,192,192),(700,200),40,4)
circle(screen,(255,255,255),(750,200),40)
circle(screen,(192,192,192),(750,200),40,4)
circle(screen,(255,255,255),(650,150),40)
circle(screen,(192,192,192),(650,150),40,4)
circle(screen,(255,255,255),(700,150),40)
circle(screen,(192,192,192),(700,150),40,4)

#Tree
rect(screen,(51,51,0),(910,350,30,150))
circle(screen,(153,204,0),(920,250),40)
circle(screen,(0,51,0),(920,250),40,4)
circle(screen,(153,204,0),(880,300),40)
circle(screen,(0,51,0),(880,300),40,4)
circle(screen,(153,204,0),(920,300),40)
circle(screen,(0,51,0),(920,300),40,4)
circle(screen,(153,204,0),(960,300),40)
circle(screen,(0,51,0),(960,300),40,4)
circle(screen,(153,204,0),(850,350),40)
circle(screen,(0,51,0),(850,350),40,4)
circle(screen,(153,204,0),(850,350),40)
circle(screen,(0,51,0),(850,350),40,4)
circle(screen,(153,204,0),(900,350),40)
circle(screen,(0,51,0),(900,350),40,4)
circle(screen,(153,204,0),(950,350),40)
circle(screen,(0,51,0),(950,350),40,4)
circle(screen,(153,204,0),(1000,350),40)
circle(screen,(0,51,0),(1000,350),40,4)

polygon(screen, (255,255,153), [(850,120),(950,120),(900,20)])
polygon(screen, (255,255,153), [(850,50),(950,50),(900,140)])
polygon(screen, (255,255,153), [(840,80),(930,135),(930,25)])
polygon(screen, (255,255,153), [(870,25),(870,135),(960,80)])
polygon(screen, (255,255,153), [(915,20), (920,120), (840,100)])
polygon(screen, (255,255,153), [(890,20), (860,110), (955,100)])
polygon(screen, (255,255,153), [(900,120), (855,35), (960,65)])
polygon(screen, (255,255,153), [(900,120), (840,60), (945,35)])
circle(screen, (255,255,153),(900,80),50)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()