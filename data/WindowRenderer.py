from data.config.Config import *
from data.config.FullScreenConfig import *

BACKGROUND_IMAGE = image.load("assets/images/backgrounds/0.png") # TEMP: To be replaced

def draw_scene():
    render_screen.blit(BACKGROUND_IMAGE, (0, 0))

def get_window_dest_rect():
    window_w, window_h = screen.get_size()
    if window_w <= 0 or window_h <= 0:
        return None
    return get_scaled_rect((window_w, window_h), (SCREEN_WIDTH, SCREEN_HEIGHT))

def present(dest_rect):
    if dest_rect is None:
        return
    screen.fill(BLACK)
    scaled = transform.smoothscale(render_screen, dest_rect.size)
    screen.blit(scaled, dest_rect)
