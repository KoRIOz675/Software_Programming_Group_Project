from pygame import image

from data.WindowRenderer import scale_image, render

class Scene:
    IMAGE_PATH = None

    def __init__(self, position=(0, 0)):
        self.image = scale_image(image.load(self.IMAGE_PATH))
        self.position = position

    def draw(self):
        render(self.image, self.position)
