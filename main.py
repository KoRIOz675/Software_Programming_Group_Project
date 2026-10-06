from imports import *
from game_loop import *

init()
set_custom_cursor()

main_menu = MainMenu()
main_menu.play_music()
game_started = False

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

        if e.type == MOUSEBUTTONDOWN:
            action = main_menu.handle_event(e, to_render_pos(e.pos, dest_rect))
            if action == "start_game":
                main_menu.stop_music()
                game_loop = GameLoop()
                game_loop.start_game("saves/save1.json")
                game_started = True
            elif action == "quit_game":
                RUNNING = False

    if game_started:
        game_loop.loop(dt)
    else:
        main_menu.draw(render_screen)

    update_click_effects(dt)
    draw_click_effects(render_screen)

    present(dest_rect)

    display.flip()

    clock.tick(FPS)

quit()
