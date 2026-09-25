from pygame import *

class Button:
    def __init__(self, IMAGE_PATH: str, position: tuple):
        self.IMAGE_PATH = IMAGE_PATH
        self.image = image.load(self.IMAGE_PATH)
        self.position = position
        self.rect = self.image.get_rect(topleft=self.position)

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    

class TextArea:
    def __init__(self, text: str, font: font, color: tuple, position: tuple):
        self.text = text
        self.font = font
        self.color = color
        self.position = position
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect(topleft=self.position)

    def draw(self, surface):
        surface.blit(self.rendered_text, self.position)

    def update_text(self, new_text: str):
        self.text = new_text
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect(topleft=self.position)