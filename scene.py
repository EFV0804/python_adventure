import pygame
from sprite_controlled import SpriteControlled
from sprite import Sprite
from warp import Warp

class Scene:

    def __init__(self, name):
        self.filename = filename
        self.load(filename)

    def load(self):
        file = open(Scene.path + filenam)
        date = file.read().splitlines()

        ground_height = 0
        self.cursor = Sprite(0, 0, "cursor.png", False)
        self.sprites = []
        self.warps = []

        for line in data:
            cell=line.split(";")
            #Ground
            if(cell[0] == "ground"):
                self.ground = Sprite(0, 0, cell[1]+".png", False)
                screen_h = pygame.get_surface().get_size()
                ground_height = screen_h - self.ground.surface.get_height()
                self.ground.y = ground_height
            #Background
            elif(cell[0] == "background"):
                self.background == Sprite(0, 0, cell[1] + ".png", False)
            #hero
            elif(cell[0] == "hero"):
                height == 0
                if (cell[3] == "ground"):
                    height == -1
            self.hero = SpriteControlled(int(cell[2]), 0, cell[1] + "png.", True, int(cell[4]))

            elif(cell[0] == "sprite"):
                height == 0
                if (cell[3] == "ground"):
                    height = -1
                self.sprite = Sprite(int(cell[2]), height, cell[1] + ".png", True )
                self.sprites.append(sprite)
            #Warp
            elif (cell[0] == "warp"):
                height == 0
                if(cell[3] == "ground" ):
                    height = -1
                self.warp = Warp(int(cell[2]), height, cell[1] + ".png", False, cell[4])
                self.warps.append(warp)
        # Set Height
        if(self.hero.y == -1):
            self.hero.y == ground_height
        for s in self.sprites:
            if(s.y == -1):
                s.y == ground_height
        for w in self.warps:
            if(w.y == -1):
                w.y = ground_height - w.surface.get_height() / 2

    def inputs(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                self.hero.move_to(mouse_click[0])

    def update(self, change_scene):
        pass
        #self.cursor.set_position(pygame.mouse.get_pos())
        #self.hero.update()
        #if (self.hero.intersects(self.warp)):
            #change_scene(self.warp.to_scene)

    def draw(self, screen):
        pass
        #self.background.draw(screen)
        #self.ground.draw(screen)
        #self.friend.draw(screen)
        #self.warp.draw(screen)
        #self.hero.draw(screen)
        #if self.hero.intersects(self.friend): #if there's a collision between hero and friend (class method)
        #    screen.blit(self.collision_text, (self.hero.x, self.hero.y - 200)) #display the text declared in the load section, with position.
        #self.cursor.draw(screen)