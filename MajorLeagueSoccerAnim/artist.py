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

    def draw_field(self):
        self.draw_grass()
        #fence
        self.draw_fence()

        self.draw_out_of_bounds()

        #safety circle
        pygame.draw.ellipse(self.screen, Color.WHITE, [240, 500, 320, 160], 5)

        #18 yard line goal box
        pygame.draw.line(self.screen, Color.WHITE, [260, 220], [180, 300], 5)
        pygame.draw.line(self.screen, Color.WHITE, [180, 300], [620, 300], 3)
        pygame.draw.line(self.screen, Color.WHITE, [620, 300], [540, 220], 5)

        #arc at the top of the goal box
        pygame.draw.arc(self.screen, Color.WHITE, [330, 280, 140, 40], math.pi, 2 * math.pi, 5)
        
        #score board pole
        pygame.draw.rect(self.screen, Color.GRAY, [390, 120, 20, 70])

        #score board
        pygame.draw.rect(self.screen, Color.BLACK, [300, 40, 200, 90])
        pygame.draw.rect(self.screen, Color.WHITE, [302, 42, 198, 88], 2)


        #goal
        pygame.draw.rect(self.screen, Color.WHITE, [320, 140, 160, 80], 5)
        pygame.draw.line(self.screen, Color.WHITE, [340, 200], [460, 200], 3)
        pygame.draw.line(self.screen, Color.WHITE, [320, 220], [340, 200], 3)
        pygame.draw.line(self.screen, Color.WHITE, [480, 220], [460, 200], 3)
        pygame.draw.line(self.screen, Color.WHITE, [320, 140], [340, 200], 3)
        pygame.draw.line(self.screen, Color.WHITE, [480, 140], [460, 200], 3)

        #6 yard line goal box
        pygame.draw.line(self.screen, Color.WHITE, [310, 220], [270, 270], 3)
        pygame.draw.line(self.screen, Color.WHITE, [270, 270], [530, 270], 2)
        pygame.draw.line(self.screen, Color.WHITE, [530, 270], [490, 220], 3)

        #light pole 1
        pygame.draw.rect(self.screen, Color.GRAY, [150, 60, 20, 140])
        pygame.draw.ellipse(self.screen, Color.GRAY, [150, 195, 20, 10])

        #lights
        pygame.draw.line(self.screen, Color.GRAY, [110, 60], [210, 60], 2)
        pygame.draw.ellipse(self.screen, self.config.light_color, [110, 40, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [130, 40, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [150, 40, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [170, 40, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [190, 40, 20, 20])
        pygame.draw.line(self.screen, Color.GRAY, [110, 40], [210, 40], 2)
        pygame.draw.ellipse(self.screen, self.config.light_color, [110, 20, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [130, 20, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [150, 20, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [170, 20, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [190, 20, 20, 20])
        pygame.draw.line(self.screen, Color.GRAY, [110, 20], [210, 20], 2)

        #light pole 2
        pygame.draw.rect(self.screen, Color.GRAY, [630, 60, 20, 140])
        pygame.draw.ellipse(self.screen, Color.GRAY, [630, 195, 20, 10])

        #lights

            
        pygame.draw.line(self.screen, Color.GRAY, [590, 60], [690, 60], 2)
        pygame.draw.ellipse(self.screen, self.config.light_color, [590, 40, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [610, 40, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [630, 40, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [650, 40, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [670, 40, 20, 20])
        pygame.draw.line(self.screen, Color.GRAY, [590, 40], [690, 40], 2)
        pygame.draw.ellipse(self.screen, self.config.light_color, [590, 20, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [610, 20, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [630, 20, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [650, 20, 20, 20])
        pygame.draw.ellipse(self.screen, self.config.light_color, [670, 20, 20, 20])
        pygame.draw.line(self.screen, Color.GRAY, [590, 20], [690, 20], 2)

        #net
        pygame.draw.line(self.screen, Color.WHITE, [325, 140], [341, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [330, 140], [344, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [335, 140], [347, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [340, 140], [350, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [345, 140], [353, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [350, 140], [356, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [355, 140], [359, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [360, 140], [362, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [364, 140], [365, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [368, 140], [369, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [372, 140], [373, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [376, 140], [377, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [380, 140], [380, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [384, 140], [384, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [388, 140], [388, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [392, 140], [392, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [396, 140], [396, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [400, 140], [400, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [404, 140], [404, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [408, 140], [408, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [412, 140], [412, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [416, 140], [416, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [420, 140], [420, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [424, 140], [423, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [428, 140], [427, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [432, 140], [431, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [436, 140], [435, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [440, 140], [438, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [445, 140], [441, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [450, 140], [444, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [455, 140], [447, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [460, 140], [450, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [465, 140], [453, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [470, 140], [456, 200], 1)
        pygame.draw.line(self.screen, Color.WHITE, [475, 140], [459, 200], 1)

        #net part 2
        pygame.draw.line(self.screen, Color.WHITE, [320, 140], [324, 216], 1)
        pygame.draw.line(self.screen, Color.WHITE, [320, 140], [326, 214], 1)
        pygame.draw.line(self.screen, Color.WHITE, [320, 140], [328, 212], 1)
        pygame.draw.line(self.screen, Color.WHITE, [320, 140], [330, 210], 1)
        pygame.draw.line(self.screen, Color.WHITE, [320, 140], [332, 208], 1)
        pygame.draw.line(self.screen, Color.WHITE, [320, 140], [334, 206], 1)
        pygame.draw.line(self.screen, Color.WHITE, [320, 140], [336, 204], 1)
        pygame.draw.line(self.screen, Color.WHITE, [320, 140], [338, 202], 1)

        #net part 3
        pygame.draw.line(self.screen, Color.WHITE, [480, 140], [476, 216], 1)
        pygame.draw.line(self.screen, Color.WHITE, [480, 140], [474, 214], 1)
        pygame.draw.line(self.screen, Color.WHITE, [480, 140], [472, 212], 1)
        pygame.draw.line(self.screen, Color.WHITE, [480, 140], [470, 210], 1)
        pygame.draw.line(self.screen, Color.WHITE, [480, 140], [468, 208], 1)
        pygame.draw.line(self.screen, Color.WHITE, [480, 140], [466, 206], 1)
        pygame.draw.line(self.screen, Color.WHITE, [480, 140], [464, 204], 1)
        pygame.draw.line(self.screen, Color.WHITE, [480, 140], [462, 202], 1)

        #net part 4
        pygame.draw.line(self.screen, Color.WHITE, [324, 144], [476, 144], 1)
        pygame.draw.line(self.screen, Color.WHITE, [324, 148], [476, 148], 1)
        pygame.draw.line(self.screen, Color.WHITE, [324, 152], [476, 152], 1)
        pygame.draw.line(self.screen, Color.WHITE, [324, 156], [476, 156], 1)
        pygame.draw.line(self.screen, Color.WHITE, [324, 160], [476, 160], 1)
        pygame.draw.line(self.screen, Color.WHITE, [324, 164], [476, 164], 1)
        pygame.draw.line(self.screen, Color.WHITE, [324, 168], [476, 168], 1)
        pygame.draw.line(self.screen, Color.WHITE, [324, 172], [476, 172], 1)
        pygame.draw.line(self.screen, Color.WHITE, [324, 176], [476, 176], 1)
        pygame.draw.line(self.screen, Color.WHITE, [335, 180], [470, 180], 1)
        pygame.draw.line(self.screen, Color.WHITE, [335, 184], [465, 184], 1)
        pygame.draw.line(self.screen, Color.WHITE, [335, 188], [465, 188], 1)
        pygame.draw.line(self.screen, Color.WHITE, [335, 192], [465, 192], 1)
        pygame.draw.line(self.screen, Color.WHITE, [335, 196], [465, 196], 1)

        #stands right
        pygame.draw.polygon(self.screen, Color.RED, [[680, 220], [800, 340], [800, 290], [680, 180]])
        pygame.draw.polygon(self.screen, Color.WHITE, [[680, 180], [800, 100], [800, 290]])

    
        #stands left
        pygame.draw.polygon(self.screen, Color.RED, [[120, 220], [0, 340], [0, 290], [120, 180]])
        pygame.draw.polygon(self.screen, Color.WHITE, [[120, 180], [0, 100], [0, 290]])
        #people
        

        #corner flag right
        pygame.draw.line(self.screen, Color.BRIGHT_YELLOW, [140, 220], [135, 190], 3)
        pygame.draw.polygon(self.screen, Color.RED, [[132, 190], [125, 196], [135, 205]])

        #corner flag left
        pygame.draw.line(self.screen, Color.BRIGHT_YELLOW, [660, 220], [665, 190], 3)
        pygame.draw.polygon(self.screen, Color.RED, [[668, 190], [675, 196], [665, 205]]) 