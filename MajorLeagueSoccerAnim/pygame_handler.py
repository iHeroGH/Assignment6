import pygame

from colors import Color
from config import Config

class PygameHandler:

    def __init__(self, config: Config):
        self.config = config

        self.init_pygame()

        self.width = 800
        self.height = 600

        self.create_display(self.width, self.height)
        self.create_timer()

        self.create_darkness()
        self.create_see_through()

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

    def quit(self):
        pygame.quit()