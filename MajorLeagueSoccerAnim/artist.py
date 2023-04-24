import pygame
import random
import math

from colors import Color
from pygame_handler import PygameHandler

class Artist:

    def __init__(self, handler: PygameHandler):
        self.handler = handler

        self.config = handler.config
        self.screen = handler.screen

        self.init_clouds()
        self.init_stars()
    
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
        pygame.draw.ellipse(self.handler.SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
        pygame.draw.ellipse(self.handler.SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
        pygame.draw.ellipse(self.handler.SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
        pygame.draw.ellipse(self.handler.SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
        pygame.draw.rect(self.handler.SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])

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

    def draw_fence(self):
        """ This function draws the fence with the certain sizes """
        y = 170
        for x in range(5, 800, 30):
            pygame.draw.polygon(self.screen, Color.NIGHT_GRAY, [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])

        y = 170
        for x in range(5, 800, 3):
            pygame.draw.line(self.screen, Color.NIGHT_GRAY, [x, y], [x, y + 15], 1)

        x = 0
        for y in range(170, 185, 4):
            pygame.draw.line(self.screen, Color.NIGHT_GRAY, [x, y], [x + 800, y], 1)
  
    def draw_sun_or_moon(self):
        if self.config.day:
            pygame.draw.ellipse(self.screen, Color.BRIGHT_YELLOW, [520, 50, 40, 40])
        else:
            pygame.draw.ellipse(self.screen, Color.WHITE, [520, 50, 40, 40]) 
            pygame.draw.ellipse(self.screen, self.config.sky_color, [530, 45, 40, 40])

    def draw_grass(self):
        y = 180
        pygame.draw.rect(
            self.screen, self.config.field_color, [0, y, 800 , 420]
        
        )
        for height in [42, 52, 62, 82]:
            pygame.draw.rect(
                self.screen, self.config.stripe_color, [0, y, 800, height]
            )
            y += 2 * height

    def draw_out_of_bounds(self):
            
            top_y = 220
            top_left = 140
            top_right = 660
            
            bottom_y = 580
            bottom_left = 0
            bottom_right = 800

            mid_y = bottom_y - top_y

            # Top
            pygame.draw.line(self.screen, Color.WHITE, [top_left, top_y], [top_right, top_y], 3)
            # Bottom
            pygame.draw.line(self.screen, Color.WHITE, [bottom_left, bottom_y], [bottom_right, bottom_y], 5)
            
            # Left
            pygame.draw.line(self.screen, Color.WHITE, [bottom_left, mid_y], [top_left, top_y], 5)
            # Right
            pygame.draw.line(self.screen, Color.WHITE, [top_right, top_y], [bottom_right, mid_y], 5)

    def draw_safety_circle(self):
        pygame.draw.ellipse(self.screen, Color.WHITE, [240, 500, 320, 160], 5)
    
    def draw_outer_goal_box(self):
        pygame.draw.line(self.screen, Color.WHITE, [260, 220], [180, 300], 5)
        pygame.draw.line(self.screen, Color.WHITE, [180, 300], [620, 300], 3)
        pygame.draw.line(self.screen, Color.WHITE, [620, 300], [540, 220], 5)

    def draw_arc(self):
        pygame.draw.arc(self.screen, Color.WHITE, [330, 280, 140, 40], math.pi, 2 * math.pi, 5)

    def draw_scoreboard(self):
        pygame.draw.rect(self.screen, Color.GRAY, [390, 120, 20, 70])
        pygame.draw.rect(self.screen, Color.BLACK, [300, 40, 200, 90])
        pygame.draw.rect(self.screen, Color.WHITE, [302, 42, 198, 88], 2)

    def draw_goal(self):
        pygame.draw.rect(self.screen, Color.WHITE, [320, 140, 160, 80], 5)
        pygame.draw.line(self.screen, Color.WHITE, [340, 200], [460, 200], 3)
        pygame.draw.line(self.screen, Color.WHITE, [320, 220], [340, 200], 3)
        pygame.draw.line(self.screen, Color.WHITE, [480, 220], [460, 200], 3)
        pygame.draw.line(self.screen, Color.WHITE, [320, 140], [340, 200], 3)
        pygame.draw.line(self.screen, Color.WHITE, [480, 140], [460, 200], 3)

    def draw_inner_goal_box(self):
        pygame.draw.line(self.screen, Color.WHITE, [310, 220], [270, 270], 3)
        pygame.draw.line(self.screen, Color.WHITE, [270, 270], [530, 270], 2)
        pygame.draw.line(self.screen, Color.WHITE, [530, 270], [490, 220], 3)

    def draw_light_poles(self):
        #light pole 1
        pygame.draw.rect(self.screen, Color.GRAY, [150, 60, 20, 140])
        pygame.draw.ellipse(self.screen, Color.GRAY, [150, 195, 20, 10])

        #light pole 2
        pygame.draw.rect(self.screen, Color.GRAY, [630, 60, 20, 140])
        pygame.draw.ellipse(self.screen, Color.GRAY, [630, 195, 20, 10])

    def draw_lights(self):
        light_pos1 = 0
        for i in range(1,3):
            pygame.draw.line(self.screen, Color.GRAY, [110, 80 - 20*i], [210, 80 - 20*i], 2)
            for i in range(1,6):
                pygame.draw.ellipse(self.screen, self.config.light_color, [90 + 20*i, 40 - light_pos1, 20, 20])
            light_pos1 += 20
        pygame.draw.line(self.screen, Color.GRAY, [110, 20], [210, 20], 2)

        light_pos2 = 0
        for i in range(1,3):
            pygame.draw.line(self.screen, Color.GRAY, [590, 80 - 20*i], [690, 80 - 20*i], 2)
            for i in range(1,6):
                pygame.draw.ellipse(self.screen, self.config.light_color, [570 + 20*i, 40 - light_pos2, 20, 20])
            light_pos2 += 20
        pygame.draw.line(self.screen, Color.GRAY, [590, 20], [690, 20], 2)

    def draw_net(self):
        #net
        for i in range(1, 9):
            pygame.draw.line(self.screen, Color.WHITE, [320 + 5*i, 140], [338 + 3*i, 200], 1)
        for i in range(1, 5):
            pygame.draw.line(self.screen, Color.WHITE, [360 + 4*i, 140], [361 + 4*i, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [380, 140], [380, 200], 1)
        for i in range(1, 11):
            pygame.draw.line(self.screen, Color.WHITE, [380 + 4*i, 140], [380 + 4*i, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [424, 140], [423, 200], 1)
        for i in range(1, 4):
            pygame.draw.line(self.screen, Color.WHITE, [424 + 4*i, 140], [423 + 4*i, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [440, 140], [438, 200], 1)
        for i in range(1, 8):
            pygame.draw.line(self.screen, Color.WHITE, [440 + 5*i, 140], [438 + 3*i, 200], 1)

        #net part 2
        for i in range(1, 9):
            pygame.draw.line(self.screen, Color.WHITE, [320, 140], [322 + i*2, 218 - i*2], 1)

        #net part 3
        for i in range(1, 9):
            pygame.draw.line(self.screen, Color.WHITE, [480, 140], [478 - i*2, 218 - i*2], 1)

        #net part 4
        for i in range(1, 10):
            pygame.draw.line(self.screen, Color.WHITE, [324, 140 + i*4], [476, 140 + i*4], 1)
        pygame.draw.line(self.screen, Color.WHITE, [335, 180], [470, 180], 1)
        for i in range(1, 5):
            pygame.draw.line(self.screen, Color.WHITE, [335, 180 + i*4], [465, 180 + i*4])

    def draw_stands(self):
         #stands right
        pygame.draw.polygon(self.screen, Color.RED, [[680, 220], [800, 340], [800, 290], [680, 180]])
        pygame.draw.polygon(self.screen, Color.WHITE, [[680, 180], [800, 100], [800, 290]])

        #stands left
        pygame.draw.polygon(self.screen, Color.RED, [[120, 220], [0, 340], [0, 290], [120, 180]])
        pygame.draw.polygon(self.screen, Color.WHITE, [[120, 180], [0, 100], [0, 290]])

    def draw_corner_flags(self):
        #corner flag right
        pygame.draw.line(self.screen, Color.BRIGHT_YELLOW, [140, 220], [135, 190], 3)
        pygame.draw.polygon(self.screen, Color.RED, [[132, 190], [125, 196], [135, 205]])

        #corner flag left
        pygame.draw.line(self.screen, Color.BRIGHT_YELLOW, [660, 220], [665, 190], 3)
        pygame.draw.polygon(self.screen, Color.RED, [[668, 190], [675, 196], [665, 205]]) 

    def draw_field(self):
        self.draw_grass()
        
        self.draw_fence()

        self.draw_out_of_bounds()

        self.draw_safety_circle()

        self.draw_outer_goal_box()

        self.draw_arc()
        
        self.draw_scoreboard()

        self.draw_goal()

        self.draw_inner_goal_box()

        self.draw_light_poles()

        self.draw_lights()

        self.draw_net()

        self.draw_stands()
        
        self.draw_corner_flags()