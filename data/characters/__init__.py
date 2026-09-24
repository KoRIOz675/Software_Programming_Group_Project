from pygame import image

from data.window_renderer import scale_image, render

class Character:
    IMAGE_PATH = None
    strength = 0
    dexterity = 0
    constitution = 0
    intelligence = 0
    wisdom = 0
    charisma = 0

    def __init__(self, position):
        self.image = scale_image(image.load(self.IMAGE_PATH))
        self.position = position
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10

    def draw(self):
        render(self.image, self.position)

    def set_stats(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma