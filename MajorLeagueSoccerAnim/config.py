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
    _light_on : bool
        A bool denoting whether or not the lights are on
    """

    def __init__(self):
        """Simply initializes the _day and _light_on bools to True"""
        self._day: bool = True
        self._light_on: bool = True

    @property
    def light_on(self) -> bool:
        """
        Returns the value of _light_on
        
        Returns
        -------
        _light_on : bool
            Whether or not the lights are on
        """
        return self._light_on
    
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
        
        This method uses the _light_on attribute to calculate what color 
        should be returned

        Returns
        -------
        color : tuple
            A tuple representing the (R, G, B) values of the light's color
        """
        return Color.YELLOW if self._light_on else Color.SILVER
    
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
        return Color.WHITE if self._day else Color.NIGHT_GRAY

    def switch_light(self):
        """
        Switches whether or not the lights are on

        The function simply sets the bool to the opposite of itself
        """
        self._light_on = not self._light_on
    
    def switch_day(self):
        """
        Switches whether or not it's day

        The function simply sets the bool to the opposite of itself
        """
        self._day = not self._day