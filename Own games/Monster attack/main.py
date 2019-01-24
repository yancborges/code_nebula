import pygame, sys
from pygame.locals import *
import time
from monster import monster
from player import player

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAY = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

movDir = []

monsters = []
monsters.append(monster(10,10,5))
monsters.append(monster(100,100,5))
monsters.append(monster(90,90,5))

plr = player(150,150, 10)

def monsterCollide(monster):
    for m in monsters:
        if(m != monster):
            if(monster.x < m.x and monster.x > m.x+15):
                if(monster.y < m.y and monster.y > m.y+15):
                    return True
            if(monster.x+15 < m.x and monster.x+15 > m.x+15):
                if(monster.y+15 < m.y and monster.y+15 > m.y+15):
                    return True
    return False
            
def moveMonsters():
    for monster in monsters:
        if(monster.x != plr.x):
            if(monster.x > plr.x):
                monster.x -= 2
            else:
                monster.x += 2
        if(monster.y != plr.y):
            if(monster.y > plr.y):
                monster.y -= 2
            else:
                monster.y += 2
        while(monsterCollide(monster)):
            if(monster.x > plr.x):
                monster.x -= 2
            else:
                monster.x += 2
            if(mosnter.y > plr.y):
                monster.y -= 2
            else:
                monster.y += 2
        if(monster.x == plr.x and monster.y == plr.y):
            plr.hp -1
        pygame.draw.rect(DISPLAY, RED, (monster.x, monster.y, 15, 15))


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
    pygame.draw.rect(DISPLAY, BLACK, (plr.x, plr.y, 15, 15))

while True:
    
    DISPLAY.fill(WHITE)

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
        elif(event.type == QUIT):
            pygame.quit()
            sys.exit()
            
    movePlayer()
    moveMonsters()                
    
    
    pygame.display.update()
    fpsClock.tick(FPS)
