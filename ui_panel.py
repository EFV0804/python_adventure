import pygame
from ui_elements import UiElements

class UiPanel(UiElements):
    def __init__(self, x, y, w, h):
        UiElements.__init__(self, x, y, w, h)
        self.color = (255,255,255)
        self.is_hover = False
        UiElements.add_event(self, "hover_in", self.on_hover_in) #use Ui Element method to add event to events map(in ui_elements.py). "hover_in" is the key and self.on_hover... function
        UiElements.add_event(self, "hover_out", self.on_hover_out)  #use Ui Element method to add event to events map(in ui_elements.py)
    
    #def set_event(self, event_type, function):
        #self.events[event_type] = function
    
    def on_hover_in(self):
        self.change_color((175, 175, 175))

    def on_hover_out(self):
        self.change_color((255, 255, 255))
    
    def change_color(self, color):
        self.color = color

    #def set_visible(self, value):
        #self.visible = value

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if(not(self.is_hover) and (mouse_x > self.x and mouse_x < self.x + self.w and mouse_y > self.y and mouse_y < self.y + self.h)):
            self.is_hover = True
            self.events["hover_in"]()
        if(self.is_hover and not (mouse_x > self.x and mouse_x < self.x + self.w and mouse_y > self.y and mouse_y < self.y + self.h)):
            self.is_hover = False
            self.events["hover_out"]()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))