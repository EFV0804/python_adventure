import pygame
from sprite_controlled import SpriteControlled
from sprite import Sprite
from warp import Warp

class Scene:

    def __init__(self, name, background_file, ground_file):
        self.name = name
        self.background = Sprite(0, 0,background_file,False)
        self.ground = Sprite(0, 0, ground_file, False)
        screen_w, screen_h = pygame.display.get_surface().get_size()
        ground_height = screen_h - self.ground.surface.get_height()
        self.ground.y = ground_height

        self.hero = SpriteControlled(10, ground_height, 'hero.png', True, 2)
        self.friend = Sprite(300, ground_height, 'friend.png', True)
        self.cursor = Sprite(0, 0, 'cursor.png', True)

        self.font = pygame.font.Font(None, 24) #define font
        self.collision_text = self.font.render("Move! Fool!", False, (0,0,0,)) #declare variable to display in case of collision

        self.warp = Warp(700, ground_height, 'warp.png', True, "level01")
        self.warp.y = ground_height - self.warp.surface.get_height() / 2

    def load(self):
        pass

    def inputs(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                self.hero.move_to(mouse_click[0])

    def update(self, change_scene):
        self.cursor.set_position(pygame.mouse.get_pos())
        self.hero.update()
        if (self.hero.intersects(self.warp)):
            change_scene(self.warp.to_scene)

    def draw(self, screen):
        self.background.draw(screen)
        self.ground.draw(screen)
        self.friend.draw(screen)
        self.warp.draw(screen)
        self.hero.draw(screen)
        if self.hero.intersects(self.friend): #if there's a collision between hero and friend (class method)
            screen.blit(self.collision_text, (self.hero.x, self.hero.y - 200)) #display the text declared in the load section, with position.
        self.cursor.draw(screen)