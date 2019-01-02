from canvas import Canvas
from field_generator import FieldGenerator
from items.power import Power
from point import Point
from scenes.scene import Scene


class Shop(Scene):
    def __init__(self, player, next_level):
        player.point = Point(0, 0)
        self.__player = player
        self.__next_level = next_level
        # ショップ、そんなに拡張性いらないと思うので5x6マスで固定して考える
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
        decorated_lines = []
        for line in self.__parts_lines:
            decorated_lines.append(['うりきれ' if part is None else part.name for part in line])
        decorated_lines[self.__player.y][self.__player.x] = f'[{decorated_lines[self.__player.y][self.__player.x]}]'
        for line in decorated_lines:
            Canvas.store_main([' '.join([part_name for part_name in line])])

        Canvas.store_main([
            'いらっしゃいある',
            'sキーで購入',
            'Sキーで退店して次のステージへ',
        ])

    def next(self, key):
        if key == 'q':
            self.__player.x -= 1
            self.__player.y -= 1
        elif key == 'a':
            self.__player.x -= 1
        elif key == 'z':
            self.__player.x -= 1
            self.__player.y += 1
        elif key == 'w':
            self.__player.y -= 1
        elif key == 'x':
            self.__player.y += 1
        elif key == 'e':
            self.__player.x += 1
            self.__player.y -= 1
        elif key == 'd':
            self.__player.x += 1
        elif key == 'c':
            self.__player.x += 1
            self.__player.y += 1
        elif key == 's':
            item = self.__parts_lines[self.__player.y][self.__player.x]
            if item is None:
                Canvas.store_side(['もうないよ'])
                return self

            self.__parts_lines[self.__player.y][self.__player.x] = None
            self.__player.pick_up(item)
            Canvas.store_side(['どうもね'])
        elif key == 'S':
            field = FieldGenerator.generate_by_level(self.__next_level)
            from scenes.stage import Stage
            return Stage(field, self.__player, self.__next_level)
        else:
            Canvas.store_side(['正しく入力してください'])

        if self.__player.x > 5:
            self.__player.x = 5
        elif self.__player.x < 0:
            self.__player.x = 0
        if self.__player.y > 4:
            self.__player.y = 4
        elif self.__player.y < 0:
            self.__player.y = 0

        return self
