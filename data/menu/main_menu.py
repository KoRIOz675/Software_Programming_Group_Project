from pygame import *
from data.config.config import SCREEN_WIDTH, SCREEN_HEIGHT
from data.menu import *
from data.audio import Audio, AudioType

BUTTON_X = (SCREEN_WIDTH - 256) // 2

class MainMenu:
    def __init__(self):
        self.background_image = image.load("assets/images/menu/main_menu.jpeg")
        self.background_image = transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.start_button = Button("assets/images/menu/start_button.png", (BUTTON_X, 400))
        self.quit_button = Button("assets/images/menu/quit_button.png", (BUTTON_X, 500))
        self.click_sound = Audio("assets/audio/2.ogg", 0.5, AudioType.SFX)
        self.menu_music = Audio("assets/audio/0.ogg", 0.1, AudioType.BGM)
        title_font = font.Font(None, 64)
        title_text = "My Game Title"
        title_x = (SCREEN_WIDTH - title_font.size(title_text)[0]) // 2
        self.game_title = TextArea(title_text, title_font, (255, 255, 255), (title_x, 200))

    def draw(self, surface):
        surface.blit(self.background_image, (0, 0))
        self.game_title.draw(surface)
        self.start_button.draw(surface)
        self.quit_button.draw(surface)

    def play_music(self):
        self.menu_music.play(-1)

    def stop_music(self):
        self.menu_music.stop()

    def handle_event(self, event, mouse_pos):
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and mouse_pos is not None:
            if self.start_button.is_clicked(mouse_pos):
                self.click_sound.play()
                return "start_game"
            elif self.quit_button.is_clicked(mouse_pos):
                self.click_sound.play()
                return "quit_game"
        return None
