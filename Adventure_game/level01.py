import pygame
from scene import Scene
from sprite_controlled import SpriteControlled
from sprite import Sprite
from warp import Warp

class Level01(Scene):
    def __init__ (self, name, background_file, ground_file):
        Scene.__init__(self, name, background_file, ground_file)
        screenh = pygame.display.get_surface().get_size()
        