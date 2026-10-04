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
        self.is_going = True
        self.scene.play_music()

    def handle_event(self, e, render_pos):
        # render_pos is the mouse position converted to the render screen (None if not a mouse event)
        pass

    def update(self, dt):
        # Implement per-frame combat logic here
        pass

    def draw(self):
        self.scene.draw()
        for character in self.player + self.enemy:
            character.draw()

    def end_combat(self):
        self.is_going = False
        self.scene.stop_music()

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
