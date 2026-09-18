from pygame import *
from data.config import *
from data.full_screen_config import *

init()

while RUNNING:
    for e in event.get():
        if e.type == QUIT:
            RUNNING = False
        elif e.type == KEYDOWN and e.key == K_F11:
            toggle_fullscreen()

    render_screen.fill(PURPLE)
    
    window_w, window_h = screen.get_size()
    if window_w > 0 and window_h > 0:
        dest_rect = get_scaled_rect((window_w, window_h), (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill(BLACK)
        scaled = transform.smoothscale(render_screen, dest_rect.size)
        screen.blit(scaled, dest_rect)

    
    display.flip()
    
    clock.tick(FPS)
    
quit()