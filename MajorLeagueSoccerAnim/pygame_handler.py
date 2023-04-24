import pygame
from colors import Color
from config import Config
from artist import Artist

class PygameHandler:

    def __init__(self, config: Config, artist: Artist):
        self.config = config

        self.init_pygame()

        self.width = 800
        self.height = 600

        self.create_display(self.width, self.height)
        self.create_timer()

        self.create_darkness()
        self.create_see_through()

        self.gameloop()

        self.done = False
    
    def init_pygame(self):
        pygame.init()

    def create_display(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Major League Soccer")

    def create_timer(self):
        self.clock = pygame.time.Clock()
        self.refresh_rate = 60
    
    def create_darkness(self):
        self.DARKNESS = pygame.Surface((self.width, self.height))
        self.DARKNESS.set_alpha(200)
        self.DARKNESS.fill(Color.BLACK)
    
    def create_see_through(self):
        self.SEE_THROUGH = pygame.Surface((self.width, self.height/3.75))
        self.SEE_THROUGH.set_alpha(150)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events(event)

    def handle_key_events(self, event):
        if event.key == pygame.K_l:
            self.config.switch_light()
        elif event.key == pygame.K_d:
            self.config.switch_day()

    def clock_tick(self):
        self.clock.tick(self.refresh_rate)

    def gameloop(self):

        while not self.done:
            # Event processing (React to key presses, mouse clicks, etc.)
            ''' for now, we'll just check to see if the X is clicked '''
            self.handle_events()

             # Game logic (Check for collisions, update points, etc.)
            ''' leave this section alone for now ''' 
            self.artist.move_clouds()
            
            # Drawing code (Describe the picture. It isn't actually drawn yet.)
            self.screen.fill(self.config.sky_color)
            self.SEE_THROUGH.fill(Color.COLOR_KEY)
            self.SEE_THROUGH.set_colorkey(Color.COLOR_KEY)
    
            if not self.config.day:
                self.artist.draw_stars()

            self.artist.draw_sun_or_moon()

            self.artist.draw_clouds(self.config.cloud_color)

            self.screen.blit(self.handler.SEE_THROUGH, (0, 0))   

            self.artist.draw_field()

            # DARKNESS
            if not self.config.day and not self.config.light_on:
                self.screen.blit(self.handler.DARKNESS, (0, 0))    

            # Update screen (Actually draw the picture in the window.)
            pygame.display.flip()

            # Limit refresh rate of game loop 
            self.handler.clock_tick()

        # Close window and quit
        self.handler.quit()

    def quit(self):
        pygame.quit()

    def game_loop(self):
        return None