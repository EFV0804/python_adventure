import pygame
from sprite_controlled import SpriteControlled
from sprite import Sprite
from warp import Warp
from ui_panel import UiPanel
from ui_group import UiGroup

class Scene:

    path = 'D:\\ARTFX\\3D3-Prog\\BLAISE_CAZALET_G\\python\\Exercice\\Vidal_Elise\\python_Adventure\\'

    def __init__(self, filename):
        self.filename = filename
        self.load(filename)

    def load(self, filename):
        file = open(Scene.path+filename)
        data = file.read().splitlines()

        ground_height=0
        self.cursor=Sprite(0,0,"cursor.png",False)
        #create maps
        self.sprites=[]
        self.warps=[]

        self.font = pygame.font.Font(None, 24) #define font
        self.collision_text = self.font.render("Move! Fool!", False, (0,0,0,)) #declare variable to display in case of collision

        #UI
        self.ui_top = UiGroup()
        panel = UiPanel(0,0,800,100)
        self.ui_top.add_element(panel)
        #self.panel.set_visible(True)



        for line in data:
            cell=line.split(";")
            #Ground
            if(cell[0]=="ground"):
                self.ground=Sprite(0,0,cell[1]+".png",False)
                screen_w, screen_h = pygame.display.get_surface().get_size()
                ground_height=screen_h - self.ground.surface.get_height()
                self.ground.y=ground_height
                #Background
            elif(cell[0]=="background"):
                self.background=Sprite(0,0,cell[1]+".png",False)
                #hero
            elif(cell[0]=="hero"):
                height=0
                if(cell[3]=="ground"):
                    height=-1
                self.hero = SpriteControlled(int(cell[2]),ground_height,cell[1]+".png",True,int(cell[4]))
                #sprite
            elif(cell[0]=="sprite"):
                height=0
                if(cell[3]=="ground"):
                    height=-1
                sprite = Sprite(int(cell[2]),height,cell[1]+".png",True)
                self.sprites.append(sprite)
                #Warp
            elif(cell[0]=="warp"):
                height=0
                if(cell[3]=="ground"):
                    height=-1
                warp=Warp(int(cell[2]),height,cell[1]+".png",True,eval(cell[4]))
                self.warps.append(warp)

        # Set Height
        if(self.hero.y==-1):
            self.hero.y = ground_height
        for s in self.sprites:
            if(s.y==-1):
                s.y=ground_height
        for w in self.warps:
            if(w.y==-1):
                w.y=ground_height-w.surface.get_height() / 2

    def inputs(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                self.hero.move_to(mouse_click[0])
        self.ui_top.inputs(events)

    def update(self, change_scene):
        self.cursor.set_position(pygame.mouse.get_pos())
        self.hero.update()
        for w in self.warps:
            if(self.hero.intersects(w)):
                change_scene(w.to_scene, w.to_scene_x)
        self.ui_top.update()

    def draw(self, screen):
        self.background.draw(screen)
        self.ground.draw(screen)
        for s in self.sprites:
            s.draw(screen)
        for w in self.warps:
            w.draw(screen)
        self.hero.draw(screen)
        self.ui_top.draw(screen)
        self.cursor.draw(screen)
        for s in self.sprites:
            if self.hero.intersects(s): #if there's a collision between hero and friend (class method)
                screen.blit(self.collision_text, (self.hero.x, self.hero.y - 150)) #display the text declared in the load section, with position.