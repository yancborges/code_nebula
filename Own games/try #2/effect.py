import pygame, sys
from pygame.locals import *
import colors

class effect:
    
    def __init__(self, x, y, kd, color, spawn, duration):
        self.x = x
        self.y = y
        self.kd = kd
        self.color = color
        self.spawn = spawn
        self.duration = duration
        
    def e_draw(self, DISPLAY):
        if(self.kd == 'CIRCLE'):
            pygame.draw.circle(DISPLAY, colors.getColor(self.color),(self.x,self.y),50,5)
