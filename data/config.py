from pygame import *

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
CURSOR_HOTSPOT = (8, 8)

# Game state
RUNNING = True
IS_FULLSCREEN = False


# Pygame setup
init()

clock = time.Clock()
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)
render_screen = Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
CURSOR_IMAGE = image.load("assets/images/cursor/standby.png")
mouse.set_cursor(CURSOR_HOTSPOT, CURSOR_IMAGE)