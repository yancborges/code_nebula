import pygame, sys
from pygame.locals import *
import colors
from goal import goal
from dot import dot
from village import village
from brain import brain

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAY = pygame.display.set_mode((800, 440), 0, 32)
pygame.display.set_caption('Learning...')


gl = goal(50, 220,'BLUE')
gen = 0

manhatthan = village(True)
manhatthan.populate()

while True:
        
    print("Generation: %d" %gen) 
    
    while (manhatthan.isAlive == True):
    
        DISPLAY.fill(colors.getColor('WHITE'))
    
        gl.draw(DISPLAY)
        manhatthan.update(DISPLAY)
    
        pygame.display.update()
        fpsClock.tick(FPS)
    
    gen += 1
    manhatthan.getNewPop(gl)
    
