import pygame

from data.characters.enemy import *

class Skeleton(Enemy):

    def __init__(self, position: tuple):
        super().__init__(position)
        self.name = "Skeleton"
        self.damage = 5
