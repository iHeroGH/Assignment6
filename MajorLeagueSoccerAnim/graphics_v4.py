''' hi '''
# Imports
import pygame
import math
import random

from colors import Color
from pygame_handler import PygameHandler
from config import Config
from artist import Artist

config = Config()
handler = PygameHandler(config)
artist = Artist(handler)

screen = handler.screen

handler.gameloop()
