import pygame
from ui_elements import UiElements
from sprite import Sprite
from message import Message

class UiButton(UiElements):
    def __init__(self, x, y, w, h, filename, send_message):
        UiElements.__init__(self, x, y, w, h)
        #self.color = (0, 0, 255)
        UiElements.add_event(self, "hover_in", self.on_hover_in)
        UiElements.add_event(self, "hover_out", self.on_hover_out)
        UiElements.add_event(self, "click", self.on_click)
        UiElements.add_event(self, "release", self.on_release)
        self.sprite_idle = Sprite(x, y, filename + "_idle.png", False)
        self.sprite_click = Sprite(x, y, filename + "_click.png", False)
        self.sprite_hover = Sprite(x, y, filename + "_hover.png", False)
        self.current_sprite = self.sprite_idle
        #self.surface = pygame.Surface((self.w, self.h)) we already get the surface from the Sprite class
        self.is_hover = False
        self.is_clicked = False

        self.send_message = send_message

    def change_color(self, color):
        self.color = color

    def on_hover_in(self):
        self.current_sprite = self.sprite_hover
        #self.change_color((0,255,0))

    def on_hover_out(self):
        self.current_sprite = self.sprite_idle
        #self.change_color((0, 0, 255))

    def on_click(self):
        self.current_sprite = self.sprite_click
        self.send_message(Message("change_state","happy"))
        #self.change_color((255,0,0))

    def on_release(self):
        if(self.is_hover):
            self.current_sprite = self.sprite_hover
            #self.change_color((0,255,0))
        else:
            self.current_sprite = self.sprite_idle
            #self.change_color((0,0,255))

    def inputs(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if(mouse_x > self.x and mouse_x < self.x + self.w and mouse_y > self.y and mouse_y < self.y + self.h):
                    self.is_clicked = True
                    self.events["click"]()
            if event.type == pygame.MOUSEBUTTONUP:
                self.is_clicked = False
                self.events["release"]()

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if(not(self.is_hover) and (mouse_x > self.x and mouse_x < self.x + self.w and mouse_y > self.y and mouse_y < self.y + self.h)):
            self.is_hover = True
            self.events["hover_in"]()
        if(self.is_hover and not (mouse_x > self.x and mouse_x < self.x + self.w and mouse_y > self.y and mouse_y < self.y + self.h)):
            self.is_hover = False
            self.events["hover_out"]()
    
    def draw(self, screen):
        self.current_sprite.draw(screen) #call draw function from the Sprite class
        #screen.blit(self.surface, (self.x, self.y))
        #pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
