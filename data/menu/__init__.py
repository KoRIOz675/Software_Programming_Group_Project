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
        self._cache = {}

    def draw(self, surface, gradient=None):
        if gradient:
            surface.blit(self._get_gradient_text(*gradient), self.position)
        else:
            surface.blit(self.rendered_text, self.position)

    def update_text(self, new_text: str):
        self.text = new_text
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect(topleft=self.position)
        self._cache = {}

    def _get_gradient_text(self, top_color, bottom_color):
        # Vertical gradient: white text multiplied by a top-to-bottom color ramp
        top, bottom = Color(top_color), Color(bottom_color)
        key = (tuple(top), tuple(bottom))
        if key not in self._cache:
            text = self.font.render(self.text, True, (255, 255, 255))
            width, height = text.get_size()
            ramp = Surface((width, height), SRCALPHA)
            for row in range(height):
                ramp.fill(top.lerp(bottom, row / max(1, height - 1)), (0, row, width, 1))
            text.blit(ramp, (0, 0), special_flags=BLEND_RGBA_MULT)
            self._cache[key] = text
        return self._cache[key]
