from brain import brain
import pygame
from pygame.locals import *
import colors
from brain import brain
from dot import dot
import random

class village:
    
    def __init__(self, isAlive):
        self.isAlive = isAlive
        self.people = []
    
    def populate(self):

        while(len(self.people) < 1000):
            b = brain(500)
            b.createBrain()
            d = dot(True,False,False,0,b,700,220,10,0)
            self.people.append(d)
        
    
    def update(self,DISPLAY):
        
        alives = 0
        
        for person in self.people:
            person.update(DISPLAY)
            if(person.isAlive == True):
                alives += 1             
                
        if(alives == 0):
            self.isAlive = False
            
    def getNewPop(self, goal):
        
        fitnessSum = 0;
        
        '''
        stronger = self.people[0]
        
        for person in self.people:
            
            if(goal.isInside(person.x,person.y) == True):
                person.isWinner = True
            else:
                person.isWinner = False
            
            person.setStrengh(goal)
            
            fitnessSum += person.strengh
            if(person.strengh > stronger.strengh):
                stronger = person
        '''        
        s = 0
        x = 0
        while(x < len(self.people)):
            
            if(goal.isInside(self.people[x].x,self.people[x].y) == True):
                self.people[x].isWinner = True
            else:
                self.people[x].isWinner = False
                
            self.people[x].setStrengh(goal)
            
            fitnessSum += self.people[x].strengh
            if(self.people[x].strengh > self.people[s].strengh):
                s = x
            x += 1
        
        #stronger.isBest = True
        v = self.people[s].brain.directions
        
        av = fitnessSum/1000
        print("Average: %f" %av)
        #print("Stronger: %f" %stronger.strengh)
        print("Stronger: %f" %self.people[s].strengh)
        
        runningSum = 0
        newPop = []

        while(len(newPop) < len(self.people)-1):
            runningSum = 0
            r = random.uniform(0,fitnessSum)
            for f in self.people:
                runningSum += f.strengh
                if (runningSum > r):
                    b = f.brain
                    baby = dot(True,False,False,0,b,700,220,10,0)
                    newPop.append(baby)
                    break
        
        for f in newPop:
            f.brain.mutate()
        
        '''        
        stronger.isAlive = True
        stronger.step = 0
        stronger.x = 700
        stronger.y = 220
        stronger.color = 'GREEN'
        '''
        self.people[s].isAlive = True
        self.people[s].step = 0
        self.people[s].x = 700
        self.people[s].y = 220
        self.people[s].color = 'GREEN'
        self.people[s].brain.directions = v
        
        #newPop.append(stronger)
        newPop.append(self.people[s])
        self.people = newPop
        self.isAlive = True
        
        
    

            
