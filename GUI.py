# The GUI for the pokemon libary #

import pygame
from pygame.constants import QUIT

def main():
    pygame.init()

    # window properties
    WIDTH = 1290
    HEIGHT = 720
    tick = 60

    # colors
    grass_green = (81, 128, 45)

    # mainloop-boolean
    go = True

    # creating the window 
    window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
    window.fill(grass_green)
    clock = pygame.time.Clock()

    # mainloop
    while go:
        # frames per second
        clock.tick(tick)

        # checking for events
        for event in pygame.event.get():
            # killing the mainloop and therefore closing the window
            if event.type == pygame.QUIT:
                go = False
            
            # Keyboard Inputs
            if event.type == pygame.KEYDOWN:
                # closing the window if "ESC" is pressed
                if event.key == pygame.K_ESCAPE:
                    quit()

            # Left-Mousebutton Inputs
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pass
        
        # refreshing the window
        pygame.display.flip()

# executing the main-function when started from file
if __name__ == "__main__":
    main()