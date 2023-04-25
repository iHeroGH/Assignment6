import pygame

# File Imports
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
        
        Parameters
        ----------
        config : Config
            An instance of the Config class that contains all the color options
            and day/lights settings for the game
        artist : Artist
            An instance of the Artist class that houses all the drawing functions
        """
        # Set the config and artist passed in
        self.config: Config = config
        self.artist: Artist = artist

        # Initialize the Pygame module
        self.init_pygame()

        # Set the size fields
        self.width: int = 800
        self.height: int = 600

        # Create the background timer
        self.create_timer()

        # Create the necessary surfaces
        self.create_display(self.width, self.height) # The main screen
        self.create_darkness() # A darkness overlay
        self.create_see_through() # A see-through overlay

        # Whether or not the game is done
        self.done: bool = False
    
    def init_pygame(self) -> None:
        """Quits the Pygame instance by simply calling .init()"""
        pygame.init()

    def create_display(
            self, 
            width: int, 
            height: int
            ) -> None:
        """
        Creates display for the program using the width and height

        Parameters
        ----------
        width : int
            The width of the screen
        height : int
            The height of the screen

        """
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Major League Soccer")

    def create_timer(self) -> None:
        """
        Creates a timer using the Pygame.time.Clock object which will be used
        to keep track of time (or to create a countdown in the future)

        Parameters
        ----------
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
        Creates a surface that will be overlaid onto the screen to create darkness.

        Parameters
        ----------
        darkness : pygame.Surface
            A surface that will be overlaid onto the screen to create darkness
            (if the lights were turned off, or it was nighttime)
        """
        self.darkness: pygame.Surface = pygame.Surface(
                                                        (self.width, 
                                                        self.height)
                                                    )
        self.artist.config_darkness(self.darkness)
    
    def create_see_through(self) -> None:
        """
        Creates a surface that will house the clouds and stars.
        """
        self.see_through: pygame.Surface = pygame.Surface(
                                                            (self.width, 
                                                            self.height/3.75)
                                                        )
        self.artist.config_see_through(self.see_through)
    
    def handle_events(self) -> None:
        """
        Handles all events in the Pygame event queue
        """
        # The general Pygame event handling method
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the user is quitting
                self.done = True # We are done
            elif event.type == pygame.KEYDOWN: # If a key is pressed
                self.handle_key_events(event) # Delegate to a different function

    def handle_key_events(self, event: pygame.event.Event) -> None:
        """
        Handles key events in the Pygame event queue

        Parameters
        -----------
        event: pygame.event.Event
            A keyboard-press event that will be analyzed in the function
        """
        # If the key is the L key
        if event.key == pygame.K_l:
            self.config.switch_light() # Turn the lights off
        # If the key is the D key
        elif event.key == pygame.K_d:
            self.config.switch_day() # Switch whether it's day or night

    def clock_tick(self) -> None:
        """
        Handles frame rate of the game
        """
        self.clock.tick(self.refresh_rate)

    def game_loop(self) -> None:
        """
        The main game loop that calls all the necessary functions to run the game.
        """
        # While the user has not exited
        while not self.done:
            # Handle any events if necessary (key presses, exiting)
            self.handle_events()

            # Maintain the see-through layer
            self.screen.fill(self.config.sky_color)
            self.artist.config_see_through(self.see_through)

            # If it's nighttime, draw the stars
            if not self.config.day:
                self.artist.draw_stars(self.screen)

            # Maintain daytiome or nighttime by drawing the sun or moon
            self.artist.draw_sun_or_moon(
                self.screen, 
                self.config.day, 
                self.config.sky_color
            )

            # Move the clouds
            self.artist.move_clouds()
            # Draw the moved clouds
            self.artist.draw_clouds(
                self.screen, 
                self.see_through, 
                self.config.cloud_color
            )

            # Maintain the field colors by redrawing the entire field
            self.artist.draw_field(
                self.screen, 
                self.config.field_color, 
                self.config.stripe_color, 
                self.config.light_color
            )

            # Check if the darkness layer should be added
            self.artist.check_darkness(
                self.config.day, 
                self.config.light_on, 
                self.screen, 
                self.darkness
            ) 

            # Update the screen and tick via refresh rate
            self.artist.update_screen()
            self.clock_tick()

        # The user has exited the screen, so quit the Pygame instance
        self.quit()

    def quit(self) -> None:
        """Quits the Pygame instance by simply calling .quit()"""
        pygame.quit()