import random

import pygame
from colors import Color

class Screen:

    def __init__(self):
        self.init_pygame()

        self.width = 800
        self.height = 600

        self.create_display(self.width, self.height)
        self.create_timer()

        self.create_darkness()
        self.create_see_through()

        self.init_clouds()
        self.init_stars()

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
    
    def init_clouds(self):
        self.clouds = [
            [random.randrange(-100, 1600), random.randrange(0, 150)]
            for _ in range(20)
            ]

    def move_clouds(self):
        for cloud in self.clouds:
            cloud[0] -= 0.5

            if cloud[0] < -100:
                cloud[0] = random.randrange(800, 1600)
                cloud[1] = random.randrange(0, 150)

    def draw_clouds(self, cloud_color):
        for cloud in self.clouds:
            self.draw_single_cloud(cloud[0], cloud[1], cloud_color)

    def draw_single_cloud(self, x, y, cloud_color):
        pygame.draw.ellipse(self.SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
        pygame.draw.ellipse(self.SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
        pygame.draw.ellipse(self.SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
        pygame.draw.ellipse(self.SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
        pygame.draw.rect(self.SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])
    
    def init_stars(self):
        self.stars = [
            [
                random.randrange(0, 800), 
                random.randrange(0, 200),
                r:=random.randrange(1, 2),
                r
            ]
            for _ in range(200)
        ]
    
    def draw_stars(self):
        for star in self.stars:
            pygame.draw.ellipse(self.screen, Color.WHITE, star)