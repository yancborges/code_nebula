import pygame, sys
from pygame.locals import *
import time

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAY = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255,255,255)
BLACK = (0,0,0)


catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

mousex = 0
mousey = 0

def insedeCat(x, y):
    if(x > catx-10 and x < catx+130):
        if(y > caty-10 and y < caty+90):
            return True
    return False
    

while True:
    DISPLAY.fill(WHITE)
    
    lastdir = direction
    if(direction == 'right'):
        catx += 5
        if(catx == 280):
            direction = 'down'
    elif(direction == 'down'):
        caty += 5
        if(caty == 220):
            direction = 'left'
    elif(direction == 'left'):
        catx -= 5
        if(catx == 10):
            direction = 'up'
    elif(direction == 'up'):
        caty -= 5
        if(caty == 10):
            direction = 'right'
    if(lastdir != direction):
    
        soundObj = pygame.mixer.Sound('meow.wav')
        soundObj.play()
        time.sleep(1)
        soundObj.stop()
    
    mouseClicked = False
    
    for event in pygame.event.get():
        if(event.type == MOUSEMOTION):
            mousex, mousey = event.pos
        elif(event.type == MOUSEBUTTONUP):
            mousex, mousey = event.pos
            mouseClicked = True
        elif(event.type == QUIT):
            pygame.quit()
            sys.exit()
            
    DISPLAY.blit(catImg, (catx, caty))
    
    if(mouseClicked == True):
        
        if(insedeCat(mousex, mousey)):
            soundObj = pygame.mixer.Sound('mad.wav')
            soundObj.play()
            time.sleep(2)
            soundObj.stop()
    
    pygame.display.update()
    fpsClock.tick(FPS)
