from random import randint

from data.characters.__init__ import Character


class Enemy(Character):
    modifier = None
    max_damage = 0

    def __init__(self, position: tuple, IMAGE_PATH: str, name: str, enemy_or_player: str):
        super().__init__(position, IMAGE_PATH, name, enemy_or_player)
        self.enemy_or_player = "enemy"


    def attack(self, target: Character):
        if target.armor_class < randint(1,20) + self.modifier:
            target.take_damage(randint(1, self.max_damage))