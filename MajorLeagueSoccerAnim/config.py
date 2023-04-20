from colors import Color

class Config:

    def __init__(self):
        self._day = True
        self._light_on = True

    @property
    def light_on(self):
        return self._light_on
    
    @property
    def day(self):
        return self._day

    @property
    def light_color(self):
        return Color.YELLOW if self._light_on else Color.SILVER
    
    @property
    def sky_color(self):
        return Color.BLUE if self._day else Color.DARK_BLUE

    @property
    def field_color(self):
        return Color.GREEN if self._day else Color.DARK_GREEN

    @property
    def stripe_color(self):
        return Color.DAY_GREEN if self._day else Color.NIGHT_GREEN

    @property
    def cloud_color(self):
        return Color.WHITE if self._day else Color.NIGHT_GRAY

    def switch_light(self):
        self._light_on = not self._light_on
    
    def switch_day(self):
        self._day = not self._day