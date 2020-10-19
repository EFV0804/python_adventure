import pygame, sys
import math
class Sprite:
    path = 'D:\\ARTFX\\3D3-Prog\\BLAISE_CAZALET_G\\python\\Exercice\\Vidal_Elise\\python_Adventure\\images\\' #Declare path variable for Sprite class

    def __init__(self, x, y , filename, centered): #This the constructor, it's the function used to create the sprites. All parameters except "self" need to be specified
        self.x = x
        self.y = y
        self.ox = 0
        self.oy = 0
        self.surface = pygame.image.load(Sprite.path + filename).convert_alpha()
        if(centered):
            self.ox = -self.surface.get_width() / 2
            self.oy = -self.surface.get_height()

    def set_position(self, position): #Functio set pos, can take in an array.
        self.x = position[0]
        self.y = position[1]

    def intersects(self, sprite): #AABB collision collision <=> not(not(collision)). Instead of finding if there is a collision, we try to find out if there not(not a collision).
        x1, y1, w1, h1 = self.x + self.ox, self.y + self.oy, self.surface.get_width(), self.surface.get_height() #values of sprite 1
        x2, y2, w2, h2 = sprite.x + sprite.ox, sprite.y + sprite.oy, sprite.surface.get_width(), sprite.surface.get_height() #values of sprite 2
        return not (x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1) #Check position of points for overlap, if overlap then collision
        
    def draw(self, screen): #function to display Sprite on screen
        screen.blit(self.surface, (self.x + self.ox, self.y + self.oy))
