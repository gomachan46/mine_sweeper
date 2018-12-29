from canvas import Canvas
from field_generator import FieldGenerator
from scenes.scene import Scene


class Shop(Scene):
    def __init__(self, player, next_level):
        self.__player = player
        self.__next_level = next_level

    def draw(self):
        Canvas.store([
            'イラッシャイアル',
            'sキーで退店して次のステージへ',
        ])

    def next(self, key):
        if key == 's':
            field = FieldGenerator.generate_by_level(self.__next_level)
            from scenes.stage import Stage
            return Stage(field, self.__player, self.__next_level)
        else:
            return self
