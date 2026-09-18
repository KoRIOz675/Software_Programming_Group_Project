from data.config import *

def get_scaled_rect(window_size, render_size):
    window_w, window_h = window_size
    render_w, render_h = render_size
    scale = min(window_w / render_w, window_h / render_h)
    scaled_w = int(render_w * scale)
    scaled_h = int(render_h * scale)
    x = (window_w - scaled_w) // 2
    y = (window_h - scaled_h) // 2
    return Rect(x, y, scaled_w, scaled_h)

def toggle_fullscreen():
    global screen, is_fullscreen
    is_fullscreen = not is_fullscreen
    if is_fullscreen:
        screen = display.set_mode((0, 0), FULLSCREEN)
    else:
        screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)
