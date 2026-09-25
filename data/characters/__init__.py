from pygame import image
from random import randint
import datetime
from data.window_renderer import scale_image, render

class Character:
    IMAGE_PATH = None
    name = "place_holder"
    enemy_or_player = "place_holder"

    def __init__(self, position: tuple):
        self.image = scale_image(image.load(self.IMAGE_PATH))
        self.position = position
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10
        self.armor_class = 10
        self.level = 1
        self.animation_idle = []
        self.animation_attack = []
        self.animation_death = []
        self.frame_index = 0
        self.not_dead = 1  # if villains is alive or not
        self.update_time = datetime.datetime.now().microsecond.real
        self.rect = None
        self.init_animations()

    def init_animations(self):
        for i in range(4):
            img = image.load(f"./images/character/{self.enemy_or_player}/{self.name}/Idle/{i}.png").convert_alpha()
            self.animation_idle.append(img)
        self.image = self.animation_idle[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position


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