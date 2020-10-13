import pygame, sys
from sprite import Sprite
from sprite_controlled import SpriteControlled
from scene import Scene
import math

def main():
    #Load
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    quit_game = False
    #path = 'D:\\ARTFX\\3D3-Prog\\BLAISE_CAZALET_G\\python\\Exercice\\Vidal_Elise\\Adventure_game\\' #declare path variable to get resources like sprites

        #load sprites
    #background = pygame.image.load(path+'background.png').convert() #load background without class method
    #ground = Sprite(0, 416, 'ground.png', False)  #load with class method
    #ground_height = 600 - ground.surface.get_height() #declare ground height variable

    #hero = SpriteControlled(100, ground_height, 'hero.png', True, 2) #load with subclass method
    #friend = Sprite(200, ground_height, 'friend.png', True)

    #font = pygame.font.Font(None, 24) #define font
    #collision_text = font.render("Move! Fool!", False, (0,0,0,)) #declare variable to display in case of collision

    #cursor = Sprite(0, 0, 'cursor.png', True) #load Sprite cursor
    pygame.mouse.set_visible(False) #Hide the mouse to leave only the cursor sprite visible



    level00 = Scene("level00", "background.png", "ground.png")
    level01 = Scene("level01", "background1.png", "ground1.png")
    scenes = {}
    scenes["level00"] = level00
    scenes["level01"] = level01
    current_scene = level00

    #Game Loop
    while not(quit_game): #while the "quit" bool is false
        #Inputs
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game = True
            #if event.type == pygame.MOUSEBUTTONDOWN: #if mouse button pressed
                #mouse_click = pygame.mouse.get_pos() # create variable with mouse position (x, y)
                #hero.move_to(mouse_click[0]) # set hero sprite to x [0] value of mouse position
        current_scene.inputs(events)
                
        #Update
        #cursor.set_position(pygame.mouse.get_pos()) #set the cursor sprite's position to current mouse pos
        #hero.update() #Run SpriteControlled method for progressive mouvement.
        current_scene.update()

        #Draw
        screen.fill((0,0,0)) #color the screen black
        current_scene.draw(screen)
        #screen.blit(background, (0, 0)) #display background by blitting
        #ground.draw(screen) # display ground sprite using class method
        #hero.draw(screen)
        #friend.draw(screen)
        #if hero.intersects(friend): #if there's a collision between hero and friend (class method)
            #screen.blit(collision_text, (hero.x, hero.y - 200)) #display the text declared in the load section, with position.
        #cursor.draw(screen)
        pygame.display.update() #updates the entire display. Can pass argument to update part of display instead

        
if __name__ == "__main__":
    main()