import random

class brain:
    
    def __init__(self, size):
        self.directions = []
        self.size = size
        
    def createBrain(self):
        
        directions = ['NORTH','SOUTH','WEST','EAST','NORTHWEST','NORTHEAST','SOUTHWEST','SOUTHEAST']
        for i in range(self.size):
            self.directions.append(directions[random.randint(0,(len(directions)-1))])
            
    def mutate(self):
        mutationRate = 1
        directions = ['NORTH','SOUTH','WEST','EAST','NORTHWEST','NORTHEAST','SOUTHWEST','SOUTHEAST']
        for i in range(self.size):
            rand = random.randint(0,1000)
            if (rand < mutationRate):
                self.directions[i] = directions[random.randint(0,(len(directions)-1))]
            
    
