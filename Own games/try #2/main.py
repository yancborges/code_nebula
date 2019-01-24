import pygame, sys
from pygame.locals import *
import time
from zombie import zombie
from player import player
import colors
import random
from effect import effect

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAY = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')


movDir = []

timer = 0

zombies = []

plr = player(200,10, 10)

def randomSpawn():
    zombies.append(zombie(random.randint(10,390),random.randint(10,290),3,random.randint(1,3)))

def moveZombies():
    for zombie in zombies:
        if(zombie.x != plr.x):
            if(zombie.x > plr.x):
                zombie.x -= 1
            else:
                zombie.x += 1
        if(zombie.y != plr.y):
            if(zombie.y > plr.y):
                zombie.y -= 1
            else:
                zombie.y += 1
        if(zombie.x == plr.x and zombie.y == plr.y):
            plr.health -1
        if(zombie.health < 1):
            zombies.remove(zombie)
        else:
            zombie.z_draw(DISPLAY)


def movePlayer():
    if(len(movDir) > 0):
        for direction in movDir:
            if(direction == 'left'):
                if(plr.x > 10):
                    plr.x -= 4
            elif(direction == 'right'):
                if(plr.x < 380):
                    plr.x += 4
            elif(direction == 'up'):
                if(plr.y > 10):
                    plr.y -= 4
            else:
                if(plr.y < 280):
                    plr.y += 4
    plr.p_draw(DISPLAY)
    
effects = []

def showEffects():
    for e in effects:
        e.e_draw(DISPLAY)
        if(timer-e.duration == e.spawn):
            effects.remove(e)
        for zombie in zombies:
            if(zombie.collide(e.x,e.y,50) == True):
                zombie.z_damaged()

while True:
    
    DISPLAY.fill(colors.getColor('WHITE'))

    timer += 1
    
    for event in pygame.event.get():
        if(event.type == KEYDOWN):
            if (event.key == K_LEFT):
                movDir.append('left')
            if(event.key == K_RIGHT):
                movDir.append('right')
            if(event.key == K_UP):
                movDir.append('up')
            if(event.key == K_DOWN):
                movDir.append('down')
        elif(event.type == KEYUP):
            if (event.key == K_LEFT):
                movDir.remove('left')
            if(event.key == K_RIGHT):
                movDir.remove('right')
            if(event.key == K_UP):
                movDir.remove('up')
            if(event.key == K_DOWN):
                movDir.remove('down')
            if(event.key == K_SPACE):
                effects.append(effect(plr.x,plr.y,'CIRCLE', 'PURPLE' ,timer, 10))
        elif(event.type == QUIT):
            pygame.quit()
            sys.exit()
            
    movePlayer()
    moveZombies()  
    showEffects()
    if(int(timer/10) == timer/10):
        randomSpawn()            
        
    
    pygame.display.update()
    fpsClock.tick(FPS)
