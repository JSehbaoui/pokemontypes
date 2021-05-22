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
    Pokedex_tile_pos  = (50,50)
    Pokedex_tile_size = (600, 400)

    AttDex_tile_pos = (700, 50)
    AttDex_tile_size = (490, 100)

    AbilityDex_tile_pos = (700,200)
    AbilityDex_tile_size = (490, 100)

    TypenDex_tile_pos = (700, 350)
    TypenDex_tile_size = (490, 100)
    
    TeamBuilder_tile_pos = (50, 500)
    TeamBuilder_tile_size = (600, 100)
    
    TeamAuswahl_tile_pos = (700, 500)
    TeamAuswahl_tile_size = (340, 100)
    
    Shutdown_tile_pos = (1090, 500)
    Shutdown_tile_size = (100, 100)
    Shutdown_tile_icon = pygame.image.load(r'assets/bilder/icons/quit.png')


    #fonts
    poke_font_path = r"components/fonts/Pokemon Solid.ttf"
    #----------------------------------------------------------

    # CREATING THE WINDOW--------------------------------------
    window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
    window.fill(grass_green)
    clock = pygame.time.Clock()
    #----------------------------------------------------------

    #CREATING THE SURFACE FOR CONTENTS-------------------------
    surface = pygame.Surface((WIDTH, HEIGHT))
    surface.fill(grass_green)
    #----------------------------------------------------------

    # DEFINING THE MAIN TILES----------------------------------
    PokeDex_tile = Tile(x = Pokedex_tile_pos[0],
                        y = Pokedex_tile_pos[1],
                        w = Pokedex_tile_size[0],
                        h = Pokedex_tile_size[1],
                        color_b = crimson_red,
                        color_t = black,
                        command= print_I_work,
                        font_size = 70,
                        font = poke_font_path,
                        text = "PokeDex"
                                                )

    AttDex_tile = Tile( x = AttDex_tile_pos[0],
                        y = AttDex_tile_pos[1],
                        w = AttDex_tile_size[0],
                        h = AttDex_tile_size[1],
                        color_b = crimson_red,
                        color_t=black,
                        command=print_I_work,
                        font_size=40,
                        font = poke_font_path,
                        text = "AttackenDex"
    )

    AbilityDex_tile = Tile(  x = AbilityDex_tile_pos[0],
                        y = AbilityDex_tile_pos[1],
                        w = AbilityDex_tile_size[0],
                        h = AbilityDex_tile_size[1],
                        color_b = crimson_red,
                        color_t= black,
                        command = print_I_work,
                        font_size=40,
                        font = poke_font_path, 
                        text = "AbilityDex")

    TypenDex_tile = Tile(x = TypenDex_tile_pos[0],
                        y = TypenDex_tile_pos[1],
                        w = TypenDex_tile_size[0],
                        h = TypenDex_tile_size[1],
                        color_b = crimson_red,
                        color_t= black,
                        command = print_I_work,
                        font_size=40,
                        font = poke_font_path, 
                        text = "TypenDex")

    TeamBuilder_tile = Tile(x = TeamBuilder_tile_pos[0],
                        y = TeamBuilder_tile_pos[1],
                        w = TeamBuilder_tile_size[0],
                        h = TeamBuilder_tile_size[1],
                        color_b = crimson_red,
                        color_t= black,
                        command = print_I_work,
                        font_size=40,
                        font = poke_font_path, 
                        text = "TeamBuilder")

    TeamAuswahl_tile = Tile(x = TeamAuswahl_tile_pos[0],
                        y = TeamAuswahl_tile_pos[1],
                        w = TeamAuswahl_tile_size[0],
                        h = TeamAuswahl_tile_size[1],
                        color_b = crimson_red,
                        color_t= black,
                        command = print_I_work,
                        font_size=40,
                        font = poke_font_path, 
                        text = "TeamAuswahl")

    Shutdown_tile = Tile(x = Shutdown_tile_pos[0],
                        y = Shutdown_tile_pos[1],
                        w = Shutdown_tile_size[0],
                        h = Shutdown_tile_size[1],
                        color_b = crimson_red,
                        color_t= black,
                        command = quit,
                        font_size=40,
                        font = poke_font_path, 
                        icon=Shutdown_tile_icon)

    
    #----------------------------------------------------------

    # mainloop
    while go:
        # frames per second
        clock.tick(tick)

        # drawing all tiles
        surface.fill(grass_green)
        for tile in Tile.all_tiles:
            tile.draw(surface)
            tile.check_for_animation(screen=surface, bg_color=grass_green)

        # checking for events
        for event in pygame.event.get():

            for tile in Tile.all_tiles:
                tile.processEvent(event)
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
        
        # blitting the content from the window on the window
        window.blit(surface, (0,0))

        # refreshing the window
        pygame.display.flip()

# executing the main-function when started from file
if __name__ == "__main__":
    main()