import pygame
import random
import math

# File Imports
from colors import Color

class Artist:
    """
    Handles all the draw operations and visual aspects of the project.
    
    Attributes
    ----------
    clouds : list[list[int, int]]
        A list of [x, y] coordinates for all the clouds that should be drawn
    stars : list[list[int, int, int, int]]
        A list of [x, y, r, r] coordinates for all the stars that should be drawn
    """

    def __init__(self):
        """Initializes the cloud and star list for visualization later"""
        self.init_clouds()
        self.init_stars()
    
    def init_clouds(self) -> None:
        """Creates a list of 20 random [x,y] coordinates for cloud positions"""
        
        # List comprehension to create a list of [rand number x, rand number y]
        # x is from -100 to 1600
        # y is from 0 to 150
        # We do this 20 times
        self.clouds = [
            [random.randrange(-100, 1600), random.randrange(0, 150)]
            for _ in range(20)
            ]
    
    def init_stars(self) -> None:
        """Creates a list of 20 random [x,y,size] coordinates for stars"""
        
        # List comprehension to create a list of [rand x, rand y, rand r, r]
        # These values will be used to create an elipse, so it needs an extra 'rect' variable 
        # x is from 0 to 800
        # y is from 0 to 200
        # r is either 1 or 2
        # The last item of the list is a repeat of r
        # We do this 200 times
        self.stars = [
            [
                random.randrange(0, 800), 
                random.randrange(0, 200),
                r:=random.randrange(1, 2),
                r
            ]
            for _ in range(200)
        ]

    def config_darkness(self, darkness: pygame.Surface) -> None:
        darkness.set_alpha(200)
        darkness.fill(Color.BLACK)
    
    def config_see_through(self, see_through: pygame.Surface) -> None:
        see_through.set_alpha(150)
        see_through.fill(Color.COLOR_KEY)
        see_through.set_colorkey(Color.COLOR_KEY)

    def move_clouds(self) -> None:
        """Moves each cloud to the left 0.5 units"""

        # Loop through each cloud in self.clouds and move it to the left 0.5 units
        for cloud in self.clouds:
            cloud[0] -= 0.5

            # If we reach the edge of the screen, re-randomize its position
            if cloud[0] < -100:
                cloud[0] = random.randrange(800, 1600)
                cloud[1] = random.randrange(0, 150)
    
    def draw_clouds(
            self, 
            surface: pygame.Surface, 
            see_through: pygame.Surface, 
            cloud_color: tuple) -> None:
        """
        Draws every cloud in the cloud list
        
        Simply uses the draw_single_cloud method to draw each cloud, then places
        the see_through surface on the main screen

        Parameters
        ----------
        surface : pygame.Surface
            The main screen to draw the see_through surface onto
        see_through : pygame.Surface
            The see_through surface to draw clouds onto
        cloud_color : tuple
            A tuple representing the (R,G,B) values of the cloud's color
        """

        # Loop through each cloud in self.clouds and draw it 
        # using self.draw_single_cloud(...)
        # We draw the clouds onto the see_through surface
        for cloud in self.clouds:
            self.draw_single_cloud(
                see_through, 
                cloud[0], 
                cloud[1], 
                cloud_color
            )
        
        # Place the see_through surface on top of the screen
        surface.blit(see_through, (0, 0))
    
    def draw_single_cloud(
        self, 
        surface: pygame.Surface, 
        x: int, 
        y: int, 
        cloud_color: tuple) -> None:
        """
        Draws a single cloud given its (x, y) coordinates and its color

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the clouds onto
        x : int
            The x poisiton of the cloud
        y : int
            The y position of the cloud
        cloud_color : tuple
            A tuple representing the (R, G, B) values of the cloud's color
        """

        # Draw the cloud shape by drawing some ellipse
        pygame.draw.ellipse( # Bottom Left
            surface, 
            cloud_color, 
            [x, y + 8, 10, 10]
        )
        pygame.draw.ellipse( # Top Left
            surface, 
            cloud_color, 
            [x + 6, y + 4, 8, 8]
        )
        pygame.draw.ellipse( # Top Right
            surface, 
            cloud_color, 
            [x + 10, y, 16, 16]
        )
        pygame.draw.ellipse( # Bottom Right
            surface, 
            cloud_color, 
            [x + 20, y + 8, 10, 10]
        )
        pygame.draw.rect( # Bottom
            surface, 
            cloud_color, 
            [x + 6, y + 8, 18, 10]
        )
    
    def draw_stars(self, surface: pygame.Surface) -> None:
        """
        Draws every star in the stars list
        
        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the stars onto
        """

        # Loop through each star in self.stars and draw an ellipse at the location
        for star in self.stars:
            pygame.draw.ellipse(
                surface, 
                Color.WHITE, 
                star
            )

    def draw_fence(self, surface: pygame.Surface) -> None:
        """
        Draws the fences of the field
        
        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the fences onto
        """

        # Draw the vertical fence separators
        y = 170
        for x in range(5, 800, 30):
            pygame.draw.polygon(
                surface, 
                Color.NIGHT_GRAY, 
                [
                    [x + 2, y], 
                    [x + 2, y + 15], 
                    [x, y + 15], 
                    [x, y]
                ]
            )

        # Draw the vertical fence parts (not the separators)
        y = 170
        for x in range(5, 800, 3):
            pygame.draw.line(
                surface, 
                Color.NIGHT_GRAY, 
                [x, y], 
                [x, y + 15], 
                1
            )

        # Draw the horizontal fence parts
        x = 0
        for y in range(170, 185, 4):
            pygame.draw.line(
                surface, 
                Color.NIGHT_GRAY, 
                [x, y], 
                [x + 800, y], 
                1
            )
  
    def draw_sun_or_moon(
            self, 
            surface: pygame.Surface, 
            is_day: bool, 
            sky_color: tuple) -> None:
        """
        Chooses to draw the sun or the moon depending on if it's day or not

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the sun/moon onto
        is_day : bool
            A bool denoting whether or not it's day
        sky_color : tuple
            A tuple representing the (R, G, B) values of the sky's color
        """

        # If it's day, draw the sun
        if is_day:
            pygame.draw.ellipse(
                surface, 
                Color.BRIGHT_YELLOW, 
                [520, 50, 40, 40]
            )
        # If it's night, draw the moon
        else:
            pygame.draw.ellipse(
                surface, 
                Color.WHITE,
                [520, 50, 40, 40]
            ) # The moon ellipse
            pygame.draw.ellipse(
                surface, 
                sky_color, 
                [530, 45, 40, 40]
            ) # The moon cutout, for the crescendo shape

    def check_darkness(
        self, 
        is_day: bool, 
        light_on: bool, 
        surface: pygame.Surface, 
        darkness: pygame.Surface) -> None:
        """
        Determines the darkness of the field based on is_day and light_on

        The method simply checks whether or not it's day and the lights are on
        and blits the darkness surface onto the original surface
        
        Parameters
        ----------
        is_day : bool
            A bool denoting whether or not it's day
        light_on : bool
            A bool denoting whether or not the lights are on
        surface : pygame.Surface
            The surface to draw the darkness onto
        darkness : pygame.Surface
            The surface that visually darkens the original surface
        """
        # Check if it should be dark and place the darkness surface onto the screen
        if not (is_day or light_on):
            surface.blit(darkness, (0, 0))   

    def draw_grass(
            self, 
            surface: pygame.Surface, 
            field_color: tuple, 
            stripe_color: tuple) -> None:
        """
        Draws the grassy area on the field

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the grass onto
        field_color : tuple
            A tuple representing the (R, G, B) values of the field's color
        stripe_color : tuple
            A tuple representing the (R, G, B) values of the stripe's color
        """

        # Draw the base field
        y = 180
        pygame.draw.rect(
            surface, 
            field_color, 
            [0, y, 800 , 420]
        
        )

        # Draw each stripe on the field
        for height in [42, 52, 62, 82]:
            pygame.draw.rect(
                surface, 
                stripe_color, 
                [0, y, 800, height]
            )
            y += 2 * height

    def draw_out_of_bounds(self, surface: pygame.Surface) -> None:
        """
        Draws the out-of-bounds lines along the edges of the field

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the grass onto
        """

        # Set constants that will determine the size of the field
        top_y = 220
        top_left = 140
        top_right = 660
        
        bottom_y = 580
        bottom_left = 0
        bottom_right = 800

        mid_y = bottom_y - top_y

        # Top
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [top_left, top_y], 
            [top_right, top_y], 
            3
        )
        # Bottom
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [bottom_left, bottom_y], 
            [bottom_right, bottom_y], 
            5
        )
        
        # Left
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [bottom_left, mid_y], 
            [top_left, top_y], 
            5
        )
        # Right
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [top_right, top_y], 
            [bottom_right, mid_y], 
            5
        )

    def draw_safety_circle(self, surface: pygame.Surface) -> None:
        """
        Draws the safety circle near the center of the field

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the grass onto
        """
        pygame.draw.ellipse(
            surface, 
            Color.WHITE, 
            [240, 500, 320, 160], 
            5
        )
    
    def draw_outer_goal_box(self, surface: pygame.Surface) -> None:
        """
        Draws the goal box onto the field

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the grass onto
        """

        # Left
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [260, 220], 
            [180, 300], 
            5
        )
        # Bottom
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [180, 300], 
            [620, 300], 
            3
        )
        # Right
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [620, 300], 
            [540, 220], 
            5
        )

    def draw_arc(self, surface: pygame.Surface) -> None:
        """
        Draws the arc near the goal box on the field

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the grass onto
        """
        pygame.draw.arc(
            surface, 
            Color.WHITE, 
            [330, 280, 140, 40], 
            math.pi, 
            2 * math.pi, 
            5
        )

    def draw_scoreboard(self, surface: pygame.Surface) -> None:
        """
        Draws the scoreboard behind the goal

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the grass onto
        """
        
        # Scoreboard Stand
        pygame.draw.rect(
            surface, 
            Color.GRAY, 
            [390, 120, 20, 70]
        )

        # Scoreboard Screen
        pygame.draw.rect(
            surface, 
            Color.BLACK, 
            [300, 40, 200, 90]
        )
        # Scoreboard Border
        pygame.draw.rect(
            surface, 
            Color.WHITE, 
            [302, 42, 198, 88], 
            2
        )

    def draw_goal(self, surface: pygame.Surface) -> None:
        """
        Draws the goal-post itself

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the grass onto
        """

        # Goal Border
        pygame.draw.rect(
            surface, 
            Color.WHITE, 
            [320, 140, 
            160, 80], 
            5
        )

        # Goal Bottom Center
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [340, 200], 
            [460, 200], 
            3
        )
        # Goal Bottom Left
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [320, 220], 
            [340, 200], 
            3
        )
        # Goal Bottom Right
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [480, 220], 
            [460, 200], 
            3
        )

        # Goal Stand Left
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [320, 140], 
            [340, 200], 
            3
        )
        # Goal Stand Right
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [480, 140], 
            [460, 200], 
            3
        )

    def draw_inner_goal_box(self, surface: pygame.Surface) -> None:
        """
        Draws the inner goal box in front of the goal

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the grass onto
        """

        # Left
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [310, 220], 
            [270, 270], 
            3
        )
        # Bottom
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [270, 270], 
            [530, 270], 
            2
        )
        # Right
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [530, 270], 
            [490, 220], 
            3
        )

    def draw_light_poles(self, surface: pygame.Surface) -> None:
        """
        Draws the two light poles on either side of the field

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the grass onto
        """

        # Left Pole
        # Pole
        pygame.draw.rect(
            surface, 
            Color.GRAY, 
            [150, 60, 20, 140]
        )
        # Bottom
        pygame.draw.ellipse(
            surface, 
            Color.GRAY, 
            [150, 195, 20, 10]
        )

        # Right Pole
        # Pole
        pygame.draw.rect(
            surface, 
            Color.GRAY, 
            [630, 60, 20, 140]
        )
        # Bottom
        pygame.draw.ellipse(
            surface, 
            Color.GRAY, 
            [630, 195, 20, 10]
        )

    def draw_lights(
            self, 
            surface: pygame.Surface, 
            light_color: tuple) -> None:
        """
        Draws the lights onto both light poles

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the grass onto
        light_color : tuple
            A tuple representing the (R, G, B) values of the color of the light
        """
        # Left Pole
        light_pos1 = 0
        # Draw the two separator lines on the pole
        for i in range(1,3):
            pygame.draw.line(
                surface, 
                Color.GRAY, 
                [110, 80 - 20*i], 
                [210, 80 - 20*i], 
                2
            )
            # For each separator, draw 6 light bulbs
            for i in range(1,6):
                pygame.draw.ellipse(
                    surface, 
                    light_color, 
                    [90 + 20*i, 40 - light_pos1, 20, 20]
                )
            light_pos1 += 20
        # Draw the left pole's top border
        pygame.draw.line(
            surface, 
            Color.GRAY, 
            [110, 20], 
            [210, 20], 
            2
        )

        # Right Pole
        light_pos2 = 0
        # Draw the two separator lines on the pole
        for i in range(1,3):
            pygame.draw.line(
                surface, 
                Color.GRAY, 
                [590, 80 - 20*i], 
                [690, 80 - 20*i], 
                2
            )
            # For each separator, draw 6 light bulbs
            for i in range(1,6):
                pygame.draw.ellipse(
                    surface, 
                    light_color, 
                    [570 + 20*i, 40 - light_pos2, 20, 20]
                    )
            light_pos2 += 20
        # Draw the right pole's top border
        pygame.draw.line(
            surface, 
            Color.GRAY, 
            [590, 20], 
            [690, 20], 
            2
        )

    def draw_net(self, surface: pygame.Surface) -> None:
        """
        Draws the net inside the goal

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the grass onto
        """
        
        # DOWN
        # CENTER
        # Left
        for i in range(1, 9):
            pygame.draw.line(
                surface, 
                Color.WHITE, 
                [320 + 5*i, 140], 
                [338 + 3*i, 200], 
                1
            )
        # MidLeft
        for i in range(1, 5):
            pygame.draw.line(
                surface, 
                Color.WHITE, 
                [360 + 4*i, 140], 
                [361 + 4*i, 200], 
                1
            )

        # Mid
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [380, 140], 
            [380, 200], 
            1
        )
        for i in range(1, 11):
            pygame.draw.line(
                surface, 
                Color.WHITE, 
                [380 + 4*i, 140], 
                [380 + 4*i, 200], 
                1
            )
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [424, 140], 
            [423, 200], 
            1
        )

        # MidRight
        for i in range(1, 4):
            pygame.draw.line(
                surface, 
                Color.WHITE, 
                [424 + 4*i, 140], 
                [423 + 4*i, 200], 
                1
            )
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [440, 140], 
            [438, 200], 
            1
        )
        # Right
        for i in range(1, 8):
            pygame.draw.line(
                surface, 
                Color.WHITE, 
                [440 + 5*i, 140], 
                [438 + 3*i, 200], 
                1
            )

        # LEFT
        for i in range(1, 9):
            pygame.draw.line(
                surface, 
                Color.WHITE, 
                [320, 140], 
                [322 + i*2, 218 - i*2], 
                1
            )

        # RIGHT
        for i in range(1, 9):
            pygame.draw.line(
                surface, 
                Color.WHITE, 
                [480, 140], 
                [478 - i*2, 218 - i*2], 
                1
            )

        # ACROSS
        # TOP
        for i in range(1, 10):
            pygame.draw.line(
                surface, 
                Color.WHITE, 
                [324, 140 + i*4], 
                [476, 140 + i*4], 
                1
            )
        
        # MIDDLE
        pygame.draw.line(
            surface, 
            Color.WHITE, 
            [335, 180], 
            [470, 180], 
            1
        )

        # BOTTOM
        for i in range(1, 5):
            pygame.draw.line(
                surface, 
                Color.WHITE, 
                [335, 180 + i*4], 
                [465, 180 + i*4]
            )

    def draw_stands(self, surface: pygame.Surface) -> None:
        """
        Draws the stands on either side of the field

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the grass onto
        """
        # RIGHT
        # Bottom
        pygame.draw.polygon(
            surface, 
            Color.RED, 
            [
                [680, 220], 
                [800, 340], 
                [800, 290], 
                [680, 180]
            ]
        )
        # Top
        pygame.draw.polygon(
            surface, 
            Color.WHITE, 
            [
                [680, 180], 
                [800, 100], 
                [800, 290]
            ]
        )

        # LEFT
        # Bottom
        pygame.draw.polygon(
            surface, 
            Color.RED, 
            [
                [120, 220], 
                [0, 340], 
                [0, 290], 
                [120, 180]
            ]
        )
        # Top
        pygame.draw.polygon(
            surface, 
            Color.WHITE, 
            [
                [120, 180], 
                [0, 100], 
                [0, 290]
            ]
        )

    def draw_corner_flags(self, surface: pygame.Surface) -> None:
        """
        Draws the flags on either corner of the field

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the grass onto
        """
        # RIGHT
        # Stand
        pygame.draw.line(
            surface, 
            Color.BRIGHT_YELLOW, 
            [140, 220], 
            [135, 190], 
            3
        )
        # Flag
        pygame.draw.polygon(
            surface, 
            Color.RED, 
            [
                [132, 190], 
                [125, 196], 
                [135, 205]
            ]
        )

        # LEFT
        # Stand
        pygame.draw.line(
            surface, 
            Color.BRIGHT_YELLOW, 
            [660, 220], 
            [665, 190], 
            3
        )
        # Flag
        pygame.draw.polygon(
            surface, 
            Color.RED, 
            [
                [668, 190], 
                [675, 196], 
                [665, 205]
            ]
        )
         
    def draw_field(
            self, 
            surface: pygame.Surface, 
            field_color: tuple, 
            stripe_color: tuple, 
            light_color: tuple, 
            ) -> None:
        """
        Draws each aspect of the field by calling each draw_x function

        This function takes all the necessary configurations to pass to the
        respective functions

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the grass onto
        field_color : tuple
            A tuple representing the (R, G, B) values of the field's color
        stripe_color : tuple
            A tuple representing the (R, G, B) values of the stripe's color
        light_color : tuple
            A tuple representing the (R, G, B) values of the light's color
        """
        # Draw the grass
        self.draw_grass(surface, field_color, stripe_color)

        # Draw the back fence
        self.draw_fence(surface)

        # Draw field markings
        self.draw_out_of_bounds(surface)
        self.draw_safety_circle(surface)
        self.draw_outer_goal_box(surface)
        self.draw_inner_goal_box(surface)
        self.draw_arc(surface)

        # Draw the scoreboard
        self.draw_scoreboard(surface)

        # Draw the goal frame
        self.draw_goal(surface)
        # Draw the nets
        self.draw_net(surface)

        # Draw the light poles and lights
        self.draw_light_poles(surface)
        self.draw_lights(surface, light_color)

        # Draw the audience stands
        self.draw_stands(surface)

        # Draw the corner flags
        self.draw_corner_flags(surface)
    
    def update_screen(self) -> None:
        """Updates the pygame screen by simply calling display.flip()"""
        pygame.display.flip()