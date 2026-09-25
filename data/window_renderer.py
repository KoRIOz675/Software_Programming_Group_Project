from data.config.config import *
from data.config.full_screen_config import *

CHARACTER_SOURCE_SIZE = 32
CHARACTER_RENDER_SIZE = 128
RENDER_SCALE = CHARACTER_RENDER_SIZE // CHARACTER_SOURCE_SIZE

def scale_image(surface):
    width, height = surface.get_size()
    return transform.scale(surface, (width * RENDER_SCALE, height * RENDER_SCALE))

def render(surface, position):
    render_screen.blit(surface, position)

def get_window_dest_rect():
    window_w, window_h = screen.get_size()
    if window_w <= 0 or window_h <= 0:
        return None
    return get_scaled_rect((window_w, window_h), (SCREEN_WIDTH, SCREEN_HEIGHT))

def present(dest_rect):
    if dest_rect is None:
        return
    screen.fill(BLACK)
    scaled = transform.scale(render_screen, dest_rect.size)
    screen.blit(scaled, dest_rect)

def to_render_pos(pos, dest_rect):
    if not dest_rect or dest_rect.width <= 0:
        return None
    scale = dest_rect.width / SCREEN_WIDTH
    return ((pos[0] - dest_rect.x) / scale, (pos[1] - dest_rect.y) / scale)
