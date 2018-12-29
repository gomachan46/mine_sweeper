from canvas import Canvas
from field_generator import FieldGenerator
from player import Player
from scene import Scene
from stage import Stage


class PlayerCreation(Scene):
    def draw(self):
        Canvas.store(['プレーヤー名を入力してください'])

    def next(self, name):
        player = Player(name)
        field = FieldGenerator.generate(9, 9, 5)
        level = 1
        return Stage(field, player, level)
