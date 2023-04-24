# Imports
from pygame_handler import PygameHandler
from config import Config
from artist import Artist

config = Config()
artist = Artist()
handler = PygameHandler(config, artist)

handler.game_loop()
