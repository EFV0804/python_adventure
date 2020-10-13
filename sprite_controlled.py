import math
from sprite import Sprite

class SpriteControlled(Sprite): #create subclass for sprite that can be controlled

    def __init__(self, x, y, filename, centered, speed): #Constructor
        Sprite.__init__(self,x,y,filename,centered) #inherits Sprite class constructor arguments
        self.speed = speed #variable to determine mouvement increment
        self.is_moving = False #Bool to set off mouvement

    def move_to(self, x): # Function to move the sprite to a position x
        self.goal_x = x # Variable to move the sprite to
        self.is_moving = True #When function is called changes bool to True

    def update(self): #Function to move the sprite progressivily 
        if(self.is_moving): # function works if bool is True
            if(self.x < self.goal_x): # If the sprite' x position is inferior the x position it's trying to reach (if sprite is left of goal)
                self.x = self.x + self.speed # then the sprite's x position is incremented by speed value
            if(self.x > self.goal_x): # If the sprite's x position is inferio to the x position it's trying to reach (if Sprite is right of goal)
                self.x = self.x - self.speed #then sprite's x position is decremented by speed value
            if(math.fabs(self.goal_x - self.x ) < self.speed): # math.fabs get absolute values. when the difference between destination and current position is inferior to speed
                self.is_moving = False # then stop moving