from data.characters.enemy import enemy
from data.scenes import scene

class Combat:
    def __init__(self, player: list[object], enemy: list[enemy], scene: scene):
        self.player = player
        self.enemy = enemy
        self.scene = scene
    
    def start_combat(self):
        # Implement combat logic here
        pass
    
    def end_combat(self):
        # Implement end combat logic here
        pass
    
    def display_combat_status(self):
        # Implement logic to display combat status here
        pass
    
    def player_turn(self):
        # Implement player turn logic here
        pass
    
    def select_target(self):
        # Implement logic to select a target from the enemy list
        pass