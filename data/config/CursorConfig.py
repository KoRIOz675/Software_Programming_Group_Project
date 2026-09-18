from data.config.Config import *

CLICK_EFFECT_DURATION = 0.35
CLICK_EFFECT_START_RADIUS = 18
CLICK_EFFECT_END_RADIUS = 2
CLICK_EFFECT_WIDTH = 2
CLICK_EFFECT_COLOR = WHITE
CURSOR_HOTSPOT = (0, 0)
CURSOR_IMAGE = image.load("assets/images/cursor/standby.png")

click_effects = []

def set_custom_cursor():
    mouse.set_cursor(CURSOR_HOTSPOT, CURSOR_IMAGE)

def spawn_click_effect(pos):
    click_effects.append({"pos": pos, "age": 0.0})

def handle_click_event(e, dest_rect):
    if e.type != MOUSEBUTTONDOWN or e.button != 1:
        return
    if not dest_rect or dest_rect.width <= 0:
        return
    scale = dest_rect.width / SCREEN_WIDTH
    render_pos = ((e.pos[0] - dest_rect.x) / scale, (e.pos[1] - dest_rect.y) / scale)
    spawn_click_effect(render_pos)

def update_click_effects(dt):
    for effect in click_effects[:]:
        effect["age"] += dt
        if effect["age"] >= CLICK_EFFECT_DURATION:
            click_effects.remove(effect)

def draw_click_effects(surface):
    for effect in click_effects:
        t = effect["age"] / CLICK_EFFECT_DURATION
        radius = CLICK_EFFECT_START_RADIUS + (CLICK_EFFECT_END_RADIUS - CLICK_EFFECT_START_RADIUS) * t
        pos = (int(effect["pos"][0]), int(effect["pos"][1]))
        draw.circle(surface, CLICK_EFFECT_COLOR, pos, max(1, round(radius)), CLICK_EFFECT_WIDTH)
        