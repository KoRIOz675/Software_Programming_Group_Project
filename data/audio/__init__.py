from pygame import *
from enum import Enum

class AudioType(Enum):
    BGM = "bgm"
    SFX = "sfx"

class Audio:
    def __init__(self, AUDIO_FILE: str, AUDIO_VOLUME: float, AUDIO_TYPE: AudioType):
        if not mixer.get_init():
            mixer.init()
        self.sound = None
        self.AUDIO_FILE = AUDIO_FILE
        self.AUDIO_VOLUME = AUDIO_VOLUME
        self.AUDIO_TYPE = AUDIO_TYPE
        self.set_music(self.AUDIO_FILE)
        self.set_volume(self.AUDIO_VOLUME)

    def play(self, loops: int = None):
        if self.AUDIO_TYPE == AudioType.BGM:
            mixer.music.load(self.AUDIO_FILE)
            mixer.music.set_volume(self.AUDIO_VOLUME)
            mixer.music.play(-1 if loops is None else loops)
        else:
            self.sound.play(0 if loops is None else loops)

    def stop(self):
        if self.AUDIO_TYPE == AudioType.BGM:
            mixer.music.fadeout(500)
        elif self.sound is not None:
            self.sound.fadeout(500)

    def pause(self):
        if self.AUDIO_TYPE == AudioType.BGM:
            mixer.music.pause()

    def unpause(self):
        if self.AUDIO_TYPE == AudioType.BGM:
            mixer.music.unpause()

    def set_music(self, music_file: str):
        self.AUDIO_FILE = music_file
        if self.AUDIO_TYPE == AudioType.SFX:
            self.sound = mixer.Sound(self.AUDIO_FILE)
            self.sound.set_volume(self.AUDIO_VOLUME)

    def set_volume(self, volume: float):
        self.AUDIO_VOLUME = max(0.0, min(1.0, volume))
        if self.AUDIO_TYPE == AudioType.BGM:
            mixer.music.set_volume(self.AUDIO_VOLUME)
        elif self.sound is not None:
            self.sound.set_volume(self.AUDIO_VOLUME)
