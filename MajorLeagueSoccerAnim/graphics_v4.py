# File imports
from pygame_handler import PygameHandler
from config import Config
from artist import Artist

# Create the config and artist for the handler
config = Config()
artist = Artist()
# Create the handler by using the config and artist
handler = PygameHandler(config, artist)

# Start the game
handler.game_loop()