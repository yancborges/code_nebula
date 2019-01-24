#! py

import pygame, sys
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Oi')

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)

windowSurface.fill(BLUE)

pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291,106), (236, 277), (56,277), (0,106)))
pygame.draw.circle(windowSurface, RED, (300, 50), 20, 0)
pygame.draw.rect(windowSurface, WHITE, (200,150,100,50))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
        

