import pygame

from data.characters.enemy import *

class Skeleton(Enemy):
    damage = 5

    def __init__(self, position: tuple):
        super().__init__(position)

