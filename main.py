import pygame, sys, math
from scene import Scene

def main():
    #Load
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    quit_game = False
    pygame.mouse.set_visible(False) #Hide the mouse to leave only the cursor sprite visible

    inventory = []
    level00 = Scene("level00.lvl", inventory)
    level01 = Scene("level01.lvl", inventory)
    scenes = {}
    scenes["level00"] = level00
    scenes["level01"] = level01
    current_scene = level00

    def change_scene(name, x):
        nonlocal current_scene
        current_scene.after_change()
        current_scene = scenes[name]
        current_scene.hero.x = x
        current_scene.hero.is_moving = False


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
        current_scene.inputs(events)
                 
        #Update
       
        current_scene.update(change_scene)

        #Draw
        screen.fill((0,0,0)) #color the screen black
        current_scene.draw(screen)
        pygame.display.update() #updates the entire display. Can pass argument to update part of display instead

        
if __name__ == "__main__":
    main()