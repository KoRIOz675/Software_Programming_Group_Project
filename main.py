from imports import *

init()
set_custom_cursor()

scene = Scene("assets/images/scenes/map-01.png", "assets/audio/0.ogg", 0.1)
scene.play_music()

while RUNNING:
    dt = clock.get_time() / 1000
    dest_rect = get_window_dest_rect()

    for e in event.get():
        if e.type == QUIT:
            RUNNING = False
        else:
            handle_click_event(e, dest_rect)

    update_click_effects(dt)

    render_screen.fill(BLACK)
    scene.draw()
    # hero.draw()
    draw_click_effects(render_screen)

    present(dest_rect)

    display.flip()
    
    clock.tick(FPS)
    
quit()