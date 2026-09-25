from pygame import *

from data.audio import Audio, AudioType
from data.window_renderer import scale_image, render

class Scene:
    def __init__(self, IMAGE_PATH: str, AUDIO_FILE: str, AUDIO_VOLUME: float):
        self.IMAGE_PATH = IMAGE_PATH
        self.image = scale_image(image.load(self.IMAGE_PATH))
        self.position = (0, 0)
        self.music = Audio(AUDIO_FILE, AUDIO_VOLUME, AudioType.BGM)

    def draw(self):
        render(self.image, self.position)

    def play_music(self):
        self.music.play(-1)
    
    def stop_music(self):
        self.music.stop()