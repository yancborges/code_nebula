import pygame
from pygame.locals import *
import colors

class player:
    
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health
        
    def p_draw(self, DISPLAY):
        pygame.draw.circle(DISPLAY, colors.getColor('GREEN'),(self.x,self.y),15,0)
