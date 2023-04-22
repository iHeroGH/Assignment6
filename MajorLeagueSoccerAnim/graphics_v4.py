''' hi '''
# Imports
import pygame
import math
import random

from colors import Color
from pygame_handler import PygameHandler
from config import Config
from artist import Artist

config = Config()
handler = PygameHandler(config)
artist = Artist(handler)

screen = handler.screen

while not handler.done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    handler.handle_events()

    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 
    artist.move_clouds()
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(config.sky_color)
    handler.SEE_THROUGH.fill(Color.COLOR_KEY)
    handler.SEE_THROUGH.set_colorkey(Color.COLOR_KEY)
    
    if not config.day:
        artist.draw_stars()

    artist.draw_sun_or_moon()

    artist.draw_clouds(config.cloud_color)

    screen.blit(handler.SEE_THROUGH, (0, 0))   

    artist.draw_field()

    # DARKNESS
    if not config.day and not config.light_on:
        screen.blit(handler.DARKNESS, (0, 0))    

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop 
    handler.clock_tick()

# Close window and quit
handler.quit()
