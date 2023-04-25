from colors import Color

class Config:
    """
    A class containing configuration booleans for day-ness and light status
    
    This class uses @property to calculate colors of various attributes by
    checking whether or not it's day or whether or not the lights are on.
    Those properties return a value from the Color class depending on the return
    value.

    Attributes
    ----------
    _day : bool
        A bool denoting whether or not it's day
    _lights_on : bool
        A bool denoting whether or not the lights are on
    """

    def __init__(self):
        """Simply initializes the _day and _lights_on bools to True"""
        self._day: bool = True # Whether or not it's day
        self._lights_on: bool = True # Whether or not the lights are on

    @property
    def light_on(self) -> bool:
        """
        Returns the value of _lights_on
        
        Returns
        -------
        _lights_on : bool
            Whether or not the lights are on
        """
        return self._lights_on
    
    @property
    def day(self) -> bool:
        """
        Returns the value of _day
        
        Returns
        -------
        _day : bool
            Whether or not it's day
        """
        return self._day

    @property
    def light_color(self) -> tuple:
        """
        Returns the light's color
        
        This method uses the _lights_on attribute to calculate what color 
        should be returned

        Returns
        -------
        color : tuple
            A tuple representing the (R, G, B) values of the light's color
        """
        # Yellow if the lights are on, Silver otherwise
        return Color.YELLOW if self._lights_on else Color.SILVER
    
    @property
    def sky_color(self) -> tuple:
        """
        Returns the sky's color
        
        This method uses the _day attribute to calculate what color 
        should be returned

        Returns
        -------
        color : tuple
            A tuple representing the (R, G, B) values of the sky's color
        """
        # Blue if it's day, Dark-Blue otherwise
        return Color.BLUE if self._day else Color.DARK_BLUE

    @property
    def field_color(self) -> tuple:
        """
        Returns the field's color
        
        This method uses the _day attribute to calculate what color 
        should be returned

        Returns
        -------
        color : tuple
            A tuple representing the (R, G, B) values of the field's color
        """
        # Green if it's day, Dark-Green otherwise
        return Color.GREEN if self._day else Color.DARK_GREEN

    @property
    def stripe_color(self) -> tuple:
        """
        Returns the stripe's color
        
        This method uses the _day attribute to calculate what color 
        should be returned

        Returns
        -------
        color : tuple
            A tuple representing the (R, G, B) values of the stripe's color
        """
        # Day-Green if it's day, Night-Green otherwise
        return Color.DAY_GREEN if self._day else Color.NIGHT_GREEN

    @property
    def cloud_color(self) -> tuple:
        """
        Returns the cloud's color
        
        This method uses the _day attribute to calculate what color 
        should be returned

        Returns
        -------
        color : tuple
            A tuple representing the (R, G, B) values of the cloud's color
        """
        # White if it's day, Night-Gray otherwise
        return Color.WHITE if self._day else Color.NIGHT_GRAY

    def switch_light(self) -> None:
        """
        Switches whether or not the lights are on

        The function simply sets the bool to the opposite of itself
        """
        # Just flip the bool
        self._lights_on = not self._lights_on
    
    def switch_day(self) -> None:
        """
        Switches whether or not it's day

        The function simply sets the bool to the opposite of itself
        """
        # Just flip the bool
        self._day = not self._day
