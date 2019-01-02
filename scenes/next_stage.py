from canvas import Canvas
from field_generator import FieldGenerator
from point import Point
from scenes.game_clear import GameClear
from scenes.scene import Scene
from scenes.shop import Shop


class Stage(object):
    pass


class NextStage(Scene):
    def __init__(self, player, cleared_level):
        player.point = Point(0, 0)
        self.__player = player
        self.__cleared_level = cleared_level
        self.__next_level = self.__cleared_level + 1

    def draw(self):
        Canvas.store_main([
            'ゴール！',
            '次へ進む(y/Y)',
            'もうやめる(n/N)'
        ])

    def next(self, key):
        if key == 'y' or key == 'Y':
            if self.__cleared_level % 5 == 0:
                return Shop(self.__player, self.__next_level)

            field = FieldGenerator.generate_by_level(self.__next_level)
            from scenes.stage import Stage
            return Stage(field, self.__player, self.__next_level)
        elif key == 'n' or key == 'N':
            return GameClear(self.__player)
        else:
            Canvas.store_side(['正しく入力してください'])

        return self
