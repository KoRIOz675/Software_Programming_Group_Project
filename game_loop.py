from data.characters import player
from data.combat.combat import Combat
from data.characters.enemy import Enemy
from data.characters.enemies.skeleton import Skeleton
from data.characters.player import Player
from data.scenes import Scene

greg = Player((0,0),"Greg","soldier")
spooky_scary_skeleton = Skeleton((5, 5))
saine = Scene("assets/images/backgrounds/cthulhu.jpeg", "assets/audio/2.ogg", 0.1)
level1 = Combat([greg], [spooky_scary_skeleton], saine)

class GameLoop:
    def __init__(self):
        self.is_going = True
        self.current_scene = None
        self.current_combat = None

    def set_scene(self, scene: Scene):
        self.current_scene = scene

    def get_scene(self):
        return self.current_scene

    def get_combat(self):
        return self.current_combat

    def start_game(self, save_path: str):
        self.current_combat = level1
        self.current_scene = level1.get_scene()
        level1.start_combat()

    def loop(self, dt: float):
        self.current_combat.draw()
        self.current_combat.update(dt)