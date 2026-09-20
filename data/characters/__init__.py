from pygame import image

from data.WindowRenderer import scale_image, render

class Character:
    IMAGE_PATH = None

    def __init__(self, position):
        self.image = scale_image(image.load(self.IMAGE_PATH))
        self.position = position

    def draw(self):
        render(self.image, self.position)
