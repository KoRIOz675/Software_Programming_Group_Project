from data.characters import Character
from random import randint

class Player(Character):

    def __init__(self,position, character_name, class_name):
        super().__init__(position,
                         IMAGE_PATH=f"assets/images/character/player/{class_name}/idle/1.png",
                         name=class_name,
                         enemy_or_player="player")
        self.max_damage = 1
        self.character_name = character_name
        if class_name == "barbarian" or class_name == "soldier":
            self.modifier = (self.strength - 10)//2
        elif class_name == "mage":
            self.modifier = (self.intelligence - 10)//2
        else:
            self.modifier = (self.dexterity - 10)//2

    def attack(self, target: Character):
        if target.armor_class < randint(1,20) + self.modifier:
            target.take_damage(self.max_damage)

    def set_max_damage(self, max_damage):
        self.max_damage = max_damage