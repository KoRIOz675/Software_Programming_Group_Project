from pygame import display

from data.characters.enemy import Enemy
from data.characters.player import Player
from data.scenes import Scene

class Combat:
    def __init__(self, player: list[Player], enemy: list[Enemy], scene: Scene):
        self.player = player
        self.enemy = enemy
        self.scene = scene
        self.is_going = True


    def start_combat(self):
        pass
        ''' draw logic moved to main
        self.scene.draw()
        self.scene.play_music()
        self.scene_manager()

    def scene_manager(self):
        while self.is_going:
            self.scene.draw()
            display.flip()

    '''

    def end_combat(self):
        self.is_going = False
    
    def display_combat_status(self):
        # Implement logic to display combat status here
        pass
    
    def player_turn(self):
        # Implement player turn logic here
        pass
    
    def select_target(self):
        # Implement logic to select a target from the enemy list
        pass

    def get_scene(self):
        return self.scene