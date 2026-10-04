from imports import *
from game_loop import *

init()
set_custom_cursor()

main_menu = MainMenu()
main_menu.play_music()
combat = None

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

        if combat is not None:
            render_pos = to_render_pos(e.pos, dest_rect) if e.type in (MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION) else None
            combat.handle_event(e, render_pos)
        elif e.type == MOUSEBUTTONDOWN:
            action = main_menu.handle_event(e, to_render_pos(e.pos, dest_rect))
            if action == "start_game":
                main_menu.stop_music()
                game_loop = GameLoop()
                game_loop.start_game("saves/save1.json")
                combat = game_loop.get_combat()
            elif action == "quit_game":
                RUNNING = False

    update_click_effects(dt)

    if combat is not None:
        combat.update(dt)
        if not combat.is_going:
            combat = None
            main_menu.play_music()

    if combat is None:
        main_menu.draw(render_screen)
    else:
        combat.draw()
    draw_click_effects(render_screen)

    present(dest_rect)

    display.flip()

    clock.tick(FPS)

quit()
