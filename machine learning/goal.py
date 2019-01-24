import pygame
from pygame.locals import *
import colors

class goal:
    
    def __init__(self, x, y, color):
        self.color = color
        self.x = x
        self.y = y
    
    def draw(self, DISPLAY):
        pygame.draw.circle(DISPLAY, colors.getColor(self.color),(self.x,self.y),30)
        
    def isInside(self,x,y):
        if(x >= self.x - 30 and x <= self.x + 30):
            if(y >= self.y - 30 and y <= self.y +30):
                return True
        return False
