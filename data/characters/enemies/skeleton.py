import pygame

from data.characters.enemy import *

class Skeleton(Enemy):

    def __init__(self, position: tuple):
        super().__init__(position,
                         IMAGE_PATH= "assets/images/character/enemy/skeleton/idle/1.png",
                         name= "skeleton",
                         enemy_or_player= "enemy")
        self.constitution = 10
        self.charisma = 12
        self.dexterity = 14
        self.wisdom = 6
        self.strength = 16
        self.intelligence = 8
        self.armor_class = 8
        self.name = "Skeleton"
        self.max_damage = 5
        self.modifier = (self.strength - 10)//2
