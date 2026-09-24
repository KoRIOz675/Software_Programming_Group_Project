import pygame
from __init__ import Character
from random import randint

class Enemy(Character):
    max_damage = 0
    modifier = None

    def __init__(self, position: tuple):
        super().__init__(position)


    def attack(self, target: Character):
        if target.armor_class < randint(1,20) + self.modifier:
            target.take_damage(self.max_damage)