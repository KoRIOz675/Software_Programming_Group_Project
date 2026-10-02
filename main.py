from imports import *
from game_loop import *

init()
set_custom_cursor()

main_menu = MainMenu()
main_menu.play_music()
scene = None

render_screen.fill(BLACK)
main_menu.draw(render_screen)

while RUNNING:
    dt = clock.get_time() / 1000
    dest_rect = get_window_dest_rect()

    for e in event.get():
        if e.type == QUIT:
            RUNNING = False
            continue

        handle_click_event(e, dest_rect)

        if scene is None and e.type == MOUSEBUTTONDOWN:
            action = main_menu.handle_event(e, to_render_pos(e.pos, dest_rect))
            if action == "start_game":
                main_menu.stop_music()
                game_loop = GameLoop()
                game_loop.start_game("saves/save1.json")
                scene = game_loop.get_scene()
            elif action == "quit_game":
                RUNNING = False

    update_click_effects(dt)

    if scene is None:
        main_menu.draw(render_screen)
    else:
        scene.draw()
        # hero.draw()
    draw_click_effects(render_screen)

    present(dest_rect)

    display.flip()

    clock.tick(FPS)

quit()
