# The GUI for the pokemon libary #

# importing pygame
import pygame
from pygame import surface

# importing all components
from components.widgets.tile import Tile

# importing all functions
from components.functions.print import print_I_work


# defining the main function
def main():

    # initializing pygame-------------------------------------
    pygame.init()
    #---------------------------------------------------------


    # CONSTANTS-----------------------------------------------
    # window properties
    WIDTH = 1290
    HEIGHT = 720
    tick = 60
    outer_border = 50

    # colors
    black = (0, 0, 0)
    grass_green = (81, 128, 45)
    crimson_red = (153, 32, 23)

    # mainloop-boolean
    go = True

    # tileproperties
    Pokedex_tile_pos  = (0,0)
    Pokedex_tile_size = (600, 400)

    #fonts
    poke_font_path = r"components/fonts/Pokemon Solid.ttf"
    #----------------------------------------------------------

    # CREATING THE WINDOW--------------------------------------
    window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
    window.fill(grass_green)
    clock = pygame.time.Clock()
    #----------------------------------------------------------

    #CREATING THE SURFACE FOR CONTENTS-------------------------
    surface = pygame.Surface((WIDTH-2*outer_border, HEIGHT-2*outer_border))
    #----------------------------------------------------------

    # DEFINING THE MAIN TILES----------------------------------
    Pokedex_tile = Tile(x = Pokedex_tile_pos[0],
                        y = Pokedex_tile_pos[1],
                        w = Pokedex_tile_size[0],
                        h = Pokedex_tile_size[1],
                        color_b = crimson_red,
                        color_t = black,
                        command= print_I_work,
                        font_size = 70,
                        font = poke_font_path,
                        text = "PokeDex",
                        anchor_point_x=outer_border,
                        anchor_point_y=outer_border
                                                )

    tiles = [Pokedex_tile]
    #----------------------------------------------------------

    # mainloop
    while go:
        # frames per second
        clock.tick(tick)

        # drawing all tiles
        for tile in tiles:
            tile.draw(surface)

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
                for tile in tiles:
                    tile.processEvent(event)
        
        # blitting the content from the window on the window
        window.blit(surface, (outer_border, outer_border) )

        # refreshing the window
        pygame.display.flip()

# executing the main-function when started from file
if __name__ == "__main__":
    main()