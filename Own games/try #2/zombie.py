import pygame
from pygame.locals import *
import colors

class zombie:
    
    def __init__(self, x, y, health, level):
        self.x = x
        self.y = y
        self.health = health
        self.level = level
        self.color = 'RED'
    
    def z_draw(self, DISPLAY):
        pygame.draw.circle(DISPLAY, colors.getColor(self.color),(self.x,self.y),10*self.level,0)
        
    def bar_draw(self, DISPLAY):
        x = None
        
    def collide(self, x, y, dist):
        if(x>self.x):
            Hx = x-self.x
        else:
            Hx = self.x-x
        if(y>self.y):
            Hy = y-self.y
        else:
            Hy = self.y-y
        HH = Hy**2 + Hx**2
        if((HH**(1/2)) < dist):
            return True
        
    def z_damaged(self):
        self.health -= 1
        if(self.health == 2):
            self.color = 'ORANGE'
        elif(self.health == 1):
            self.color = 'YELLOW'
        else:
            self.color = 'BLACK'
        
