from brain import brain
import pygame
from pygame.locals import *
import colors
from goal import goal

class dot:
    
    def __init__(self, isAlive, isWinner, isBest, strengh, brain, x, y, speed, step):
        self.isAlive = isAlive
        self.isWinner = isWinner
        self.isBest = isBest
        self.strengh = strengh
        self.brain = brain
        self.x = x
        self.y = y
        self.speed = speed
        self.step = step
        if(self.isBest == True):
            self.color = 'GREEN'
        else:
            self.color = 'BLACK'
        
    def draw(self, DISPLAY):
        pygame.draw.circle(DISPLAY, colors.getColor(self.color),(self.x,self.y),5)
        
    def moveAt(self, direction):
        if(direction == 'NORTH'):
            self.y = self.y + self.speed
        elif(direction == 'SOUTH'):
            self.y = self.y - self.speed
        elif(direction == 'WEST'):
            self.x = self.x + self.speed
        elif(direction == 'EAST'):
            self.x = self.x - self.speed
        elif(direction == 'NORTHWEST'):
            self.x = self.x + self.speed
            self.y = self.y + self.speed
        elif(direction == 'NORTHEAST'):
            self.x = self.x - self.speed
            self.y = self.y + self.speed
        elif(direction == 'SOUTHWEST'):
            self.x = self.x + self.speed
            self.y = self.y - self.speed
        elif(direction == 'SOUTHEAST'):
            self.x = self.x - self.speed
            self.y = self.y - self.speed
            
    def move(self):
        self.moveAt(self.brain.directions[int(self.step)])
    
    def update(self, DISPLAY):
        if(self.isAlive == True):
            if(self.x <= 5 or self.x >= 795):
                self.setDead()
            if(self.y <= 5 or self.y >= 435):
                self.setDead()
            if(self.step >= self.brain.size):
                self.setDead()
            else:
                self.move()
                self.step += 1
        self.draw(DISPLAY)
        
    def setDead(self):
        self.isAlive = False
        self.color = 'PURPLE'
        
    
    def setStrengh(self, goal):
        if(self.isWinner == True):
            self.strengh = 1.0/16.0 + 10000.0/(self.step * self.step)
        else:
            
            if(self.x > goal.x):
                distX = self.x - goal.x
            else:
                distX = goal.x - self.x
            if(self.y > goal.y):
                distY = self.y - goal.y
            else:
                distY = goal.y - self.y
                
            h = (distX**2) + (distY**2)
            distanceToGoal = h**0.5
            
            self.strengh = 1.0/(distanceToGoal * distanceToGoal)

        
        
        
        
