from pygame import *

init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS=60
## Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

# Game state
RUNNING = True


# Pygame setup
clock = time.Clock()
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)
render_screen = Surface((SCREEN_WIDTH, SCREEN_HEIGHT))