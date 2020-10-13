import pygame
from scene import Scene
from sprite_controlled import SpriteControlled
from sprite import Sprite
from warp import Warp

class Level00(Scene):
    def __init__ (self, name, background_file, ground_file):
        Scene.__init__(self, name, background_file, ground_file)
        screen_h = pygame.display.get_surface().get_size()[1]
        ground_height = screen_h - self.ground.surface.get_height()
        self.ground.y = ground_height
        self.hero = SpriteControlled(10, ground_height, "hero.png", True, 2)
        self.friend = Sprite(300, ground_height, 'friend.png', True)
        self.cursor = Sprite(0, 0, "cursor.png", False)
        self.warp = Warp(600, 0, "warp.png", False, "level01")
        self.warp.y = ground_height - self.warp.surface.get_height() / 2

        self.font = pygame.font.Font(None, 24) #define font
        self.collision_text = self.font.render("Move! Fool!", False, (0,0,0,)) #declare variable to display in case of collision

    def update():
        self.cursor.set_position(pygame.mouse.get_pos())
        self.hero.update()
        if (self.hero.intersects(self.warp)):
            change_scene(self.warp.to_scene)

    def draw():
        self.background.draw(screen)
        self.ground.draw(screen)
        self.friend.draw(screen)
        self.warp.draw(screen)
        self.hero.draw(screen)
        if self.hero.intersects(self.friend): #if there's a collision between hero and friend (class method)
            screen.blit(self.collision_text, (self.hero.x, self.hero.y - 200)) #display the text declared in the load section, with position.
        self.cursor.draw(screen)