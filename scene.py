import pygame
from sprite_controlled import SpriteControlled
from sprite import Sprite
from sprite_animated import SpriteAnimated
from sprite_pickable import SpritePickable
from sprite_stateful import SpriteStateful
from warp import Warp
from ui_panel import UiPanel
from ui_group import UiGroup
from ui_button import UiButton
from message import Message

class Scene:

    path = 'D:\\ARTFX\\3D3-Prog\\BLAISE_CAZALET_G\\python\\Exercice\\Vidal_Elise\\python_Adventure\\data\\'

    def __init__(self, filename, inventory):
        self.inventory = inventory
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
        self.pickables = []
        self.state_sprites = []
        self.messages=[]
        self.observers=[]


        self.font = pygame.font.Font(None, 24) #define font
        self.collision_text = self.font.render("Move! Fool!", False, (0,0,0,)) #declare variable to display in case of collision

        #UI Group
        self.ui_top = UiGroup()
        panel = UiPanel(0,0,800,100)
        self.ui_top.add_element(panel)
        #button0 = UiButton(10, 10, 50, 50, "button0")
        #self.ui_top.add_element(button0)
        #self.panel.set_visible(True)



        for line in data:
            cell=line.split(";")
                #GROUND
            if(cell[0]=="ground"):
                self.ground=Sprite(0,0,cell[1]+".png",False)
                screen_w, screen_h = pygame.display.get_surface().get_size()
                ground_height=screen_h - self.ground.surface.get_height()
                self.ground.y=ground_height

                #BACKGROUND
            elif(cell[0]=="background"):
                self.background=Sprite(0,0,cell[1]+".png",False)

                #HERO
            elif(cell[0]=="hero"):
                height=0
                if(cell[3]=="ground"):
                    height=-1
                self.hero = SpriteAnimated(int(cell[2]), height, cell[1], True, int(cell[4]), "idle")

                #SPRITE
            elif(cell[0]=="friend"):
                height=0
                if(cell[3]=="ground"):
                    height=-1
                friend = Sprite(int(cell[2]),height,cell[1]+".png",True)
                #self.friend = SpriteAnimated(int(cell[2]), height, cell[1], True, int(cell[4]), "idle")
                self.sprites.append(friend)

            elif(cell[0]=="stateful"):
                height=0
                if(cell[3]=="ground"):
                    height=-1
                sprite = SpriteStateful(int(cell[2]), height, eval(cell[1]), True, eval(cell[4]), cell[5])
                self.observers.append(sprite)
                self.state_sprites.append(sprite)

                #WARP
            elif(cell[0]=="warp"):
                height=0
                if(cell[3]=="ground"):
                    height=-1
                warp=Warp(int(cell[2]),height,cell[1]+".png",True,eval(cell[4]))
                self.warps.append(warp)

                #PICKABLES
            elif(cell[0]=="pickable"):
                height = 0
                if(cell[3]== "ground"):
                    height = -1
                item = SpritePickable(int(cell[2]), height, cell[1]+"_ingame.png", False, cell[1])
                self.pickables.append(item)

        # Set Height
        if(self.hero.y==-1):
            self.hero.y = ground_height
        for s in self.sprites:
            if(s.y==-1):
                s.y=ground_height
        for s in self.state_sprites:
            if(s.y==-1):
                s.y=ground_height
        for w in self.warps:
            if(w.y==-1):
                w.y=ground_height-w.surface.get_height() / 2
        for p in self.pickables:
            if(p.y == -1):
                p.y = ground_height - p.surface.get_height()

    def after_change(self):
        self.update_inventory_ui()

    def inputs(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                if(mouse_click[1] > self.ui_top.elements[0].h):
                    self.hero.move_to(mouse_click[0])
        self.ui_top.inputs(events)

    def update(self, change_scene):
        self.cursor.set_position(pygame.mouse.get_pos())
        self.hero.update()
        for w in self.warps:
            if(self.hero.intersects(w)):
                change_scene(w.to_scene, w.to_scene_x)
        for p in self.pickables:
            if(self.hero.intersects(p) and not (p.is_picked)):
                self.add_to_inventory(p.pick())
        self.ui_top.update()
        for message in self.messages:
            for observer in self.observers:
                observer.notify(message)
        self.messages.clear()

    def add_to_inventory(self, item):
        self.inventory.append(item)
        self.update_inventory_ui()


    def update_inventory_ui(self):
        i = 0
        for item in self.inventory:
            x = i*95+10
            y = 10
            w = 90
            h = 90
            self.ui_top.add_element(UiButton(x,y,w,h,item, self.send_message))
            i = i+1

    def send_message(self, message):
        self.messages.append(message)

    def draw(self, screen):
        self.background.draw(screen)
        self.ground.draw(screen)
        for s in self.sprites:
            s.draw(screen)
        for w in self.warps:
            w.draw(screen)
        for p in self.pickables:
            p.draw(screen)
        for s in self.state_sprites:
            s.draw(screen)
        self.hero.draw(screen)
        self.ui_top.draw(screen)
        self.cursor.draw(screen)
        for s in self.sprites:
            if self.hero.intersects(s): #if there's a collision between hero and friend (class method)
                screen.blit(self.collision_text, (self.hero.x, self.hero.y - 150)) #display the text declared in the load section, with position.