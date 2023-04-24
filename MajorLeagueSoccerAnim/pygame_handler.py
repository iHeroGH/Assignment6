import pygame
from colors import Color
from config import Config
from artist import Artist

class PygameHandler:
    """
    Handles all the non-visual Pygame operations (like events) of the project.

    The handler is the main delegator for the operation, checking configuration
    settings, calling draw methods, and initializing/maintaining the Pygame
    surfaces. The main game loop is also held in this class
    
    Attributes
    ----------
    config : Config
        An instance of the Config class that contains all the color options
        and day/lights settings for the game
    artist : Artist
        An instance of the Artist class that houses all the drawing functions
    
    width : int
        The width of the screen to initialize
    height : int
        The height of the screen to initialize
    
    refresh_rate : int
        The refresh rate of the screen
    clock : pygame.time.Clock
        A Pygame Clock object to help keep track of time
        (can be used in the future on the scoreboard to create a countdown)
    
    done : bool
        A bool denoting whether or not the user has exited
    
    screen : pygame.Surface
        The main surface on which the field will be drawn
    darkness : pygame.Surface
        A surface that will be overlaid onto the screen to imitate darkness
        (if the lights were turned off, or it was nighttime)
    see_through : pygame.Surface
        A surface that will house the clouds and stars
    
    """

    def __init__(self, config: Config, artist: Artist):
        """Initializes attributes of the Handler class
        
        Parameters:
        -----------
        config : Config
            An instance of the Config class that contains all the color options
            and day/lights settings for the game
        artist : Artist
            An instance of the Artist class that houses all the drawing functions
        """
        self.config: Config = config
        self.artist: Artist = artist

        self.init_pygame()

        self.width: int = 800
        self.height: int = 600

        self.create_display(self.width, self.height)
        self.create_timer()

        self.create_darkness()
        self.create_see_through()

        self.done: bool = False
    
    def init_pygame(self) -> None:
        pygame.init()

    def create_display(
            self, 
            width: int, 
            height: int
            ) -> None:
        """
        Creates display for graphics using width and height

        width : int
            Sets the width of the screen  

        height : int
            Sets the height of the screen  

        """
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Major League Soccer")

    def create_timer(self) -> None:
        """
        Creates timer using pygame Clock class to keep track of time in a game and ensure 
        that the game runs consistently.

        clock : pygame.time.Clock
            A Pygame Clock object to help keep track of time
            (can be used in the future on the scoreboard to create a countdown)

        refresh_rate : int
            The refresh rate of the screen
        """
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.refresh_rate: int = 60
    
    def create_darkness(self) -> None:
        """
        Creates a surface that will be overlaid onto the screen to imitate darkness.

        darkness : pygame.Surface
            A surface that will be overlaid onto the screen to imitate darkness
            (if the lights were turned off, or it was nighttime)

        """
        self.darkness: pygame.Surface = pygame.Surface(
                                                        (self.width, 
                                                        self.height)
                                                    )
        self.darkness.set_alpha(200)
        self.darkness.fill(Color.BLACK)
    
    def create_see_through(self) -> None:
        """
        Creates a surface that will house the clouds and stars.
        """
        self.see_through: pygame.Surface = pygame.Surface(
                                                            (self.width, 
                                                            self.height/3.75)
                                                        )
        self.see_through.set_alpha(150)
    
    def handle_events(self) -> None:
        """
        Handles all events in the Pygame event queue
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events(event)

    def handle_key_events(self, event: pygame.event.Event) -> None:
        """
        Handles key events in the Pygame event queue

        Parameters:
        -----------
        event: pygame.event.Event
            Determines the instance of an event (key press)
        """
        if event.key == pygame.K_l:
            self.config.switch_light()
        elif event.key == pygame.K_d:
            self.config.switch_day()

    def clock_tick(self) -> None:
        """
        Handles frame rate of the game
        """
        self.clock.tick(self.refresh_rate)

    def game_loop(self) -> None:
        """
        The main game loop that calls all the necessary functions to run the game.
        """
        while not self.done:
            self.handle_events()

            self.artist.move_clouds()
            
            self.screen.fill(self.config.sky_color)
            self.see_through.fill(Color.COLOR_KEY)
            self.see_through.set_colorkey(Color.COLOR_KEY)
    
            if not self.config.day:
                self.artist.draw_stars(self.see_through)

            self.artist.draw_sun_or_moon(
                self.screen, 
                self.config.day, 
                self.config.sky_color
            )

            self.artist.draw_clouds(
                self.screen, 
                self.see_through, 
                self.config.cloud_color
            )

            self.artist.draw_field(
                self.screen, 
                self.config.field_color, 
                self.config.stripe_color, 
                self.config.light_color
            )

            self.artist.check_darkness(
                self.config.day, 
                self.config.light_on, 
                self.screen, 
                self.darkness
            ) 

            self.artist.update_screen()

            self.clock_tick()

        self.quit()

    def quit(self) -> None:
        """Quits the Pygame instance by simply calling .quit()"""
        pygame.quit()