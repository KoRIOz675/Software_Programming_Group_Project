from random import randint

from data.characters.__init__ import Character


class Enemy(Character):
    modifier = None
    max_damage = 0

    def __init__(self, position: tuple):
        super().__init__(position)
        self.enemy_or_player = "enemy"


    def attack(self, target: Character):
        if target.armor_class < randint(1,20) + self.modifier:
            target.take_damage(self.max_damage)