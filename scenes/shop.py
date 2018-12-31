from canvas import Canvas
from field_generator import FieldGenerator
from items.power import Power
from scenes.scene import Scene


class Shop(Scene):
    def __init__(self, player, next_level):
        self.__player = player
        self.__next_level = next_level
        self.cursor = 0
        self.__parts_lines = [
            [
                Power(5),
                Power(10),
                Power(20),
                Power(30),
                Power(40),
                Power(50),
            ],
            [
                Power(5),
                Power(10),
                Power(20),
                Power(30),
                Power(40),
                Power(50),
            ],
            [
                Power(5),
                Power(10),
                Power(20),
                Power(30),
                Power(40),
                Power(50),
            ],
            [
                Power(5),
                Power(10),
                Power(20),
                Power(30),
                Power(40),
                Power(50),
            ],
            [
                Power(5),
                Power(10),
                Power(20),
                Power(30),
                Power(40),
                Power(50),
            ],
        ]

    def draw(self):
        for line in self.__parts_lines:
            Canvas.store([' '.join([f'[{part.name}]' for part in line])])
        Canvas.store([
            'いらっしゃいある',
            'sキーで退店して次のステージへ',
        ])

    def next(self, key):
        if key == 's':
            field = FieldGenerator.generate_by_level(self.__next_level)
            from scenes.stage import Stage
            return Stage(field, self.__player, self.__next_level)
        else:
            return self
