from canvas import Canvas
from field_generator import FieldGenerator
from player import Player
from scenes.scene import Scene
from scenes.stage import Stage


class PlayerCreation(Scene):
    def draw(self):
        Canvas.store_main(['プレーヤー名を入力してください'])

    def next(self, name):
        player = Player(name)
        level = 1
        field = FieldGenerator.generate_by_level(level)
        return Stage(field, player, level)
