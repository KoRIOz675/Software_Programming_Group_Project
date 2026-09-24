from pygame import image
from random import randint
from data.window_renderer import scale_image, render

class Character:
    IMAGE_PATH = None
    strength = 0
    dexterity = 0
    constitution = 0
    intelligence = 0
    wisdom = 0
    charisma = 0
    health = 0
    max_health = 0
    armor_class = 0
    level = 0

    def __init__(self, position: tuple):
        self.image = scale_image(image.load(self.IMAGE_PATH))
        self.position = position
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10
        self.level = 1

    def draw(self):
        render(self.image, self.position)

    def set_stats(self, strength: int, dexterity: int, constitution: int, intelligence: int , wisdom: int, charisma: int):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.calculate_health()
        self.health = self.max_health

    def calculate_health(self):
        self.max_health = 5 + self.level * 5  + (self.constitution - 10) * self.level

    def set_health(self, health: int):
        self.health = health

    def get_health(self):
        return self.health
    
    def set_image(self, image_path: str):
        self.IMAGE_PATH = image_path
        self.image = scale_image(image.load(self.IMAGE_PATH))
        
    def get_stats(self):
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma
        }

    def take_damage(self, damage: int):
        self.health -= randint(1, damage)