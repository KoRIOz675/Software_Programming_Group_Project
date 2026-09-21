from imports import *

init()
set_custom_cursor()

while RUNNING:
    dt = clock.get_time() / 1000
    dest_rect = get_window_dest_rect()

    for e in event.get():
        if e.type == QUIT:
            RUNNING = False
        else:
            handle_click_event(e, dest_rect)

    update_click_effects(dt)

    # scene.draw()
    # hero.draw()
    draw_click_effects(render_screen)

    present(dest_rect)

    display.flip()
    
    clock.tick(FPS)
    
quit()