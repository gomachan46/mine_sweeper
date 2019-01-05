from canvas import Canvas
from field_generator import FieldGenerator
from items.attack import Attack
from items.defence import Defence
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
                Attack(5),
                Attack(10),
                Attack(20),
                Attack(30),
                Attack(40),
                Attack(50),
            ],
            [
                Defence(5),
                Defence(10),
                Defence(20),
                Defence(30),
                Defence(40),
                Defence(50),
            ],
            [
                Attack(5),
                Attack(10),
                Attack(20),
                Attack(30),
                Attack(40),
                Attack(50),
            ],
            [
                Defence(5),
                Defence(10),
                Defence(20),
                Defence(30),
                Defence(40),
                Defence(50),
            ],
            [
                Attack(5),
                Attack(10),
                Attack(20),
                Attack(30),
                Attack(40),
                Attack(50),
            ],
            [
                Defence(5),
                Defence(10),
                Defence(20),
                Defence(30),
                Defence(40),
                Defence(50),
            ],
        ]

    def draw(self):
        decorated_lines = []
        Canvas.store_main(['いらっしゃいある'])
        for line in self.__parts_lines:
            decorated_lines.append(['うりきれ' if part is None else part.name for part in line])
        decorated_lines[self.__player.y][self.__player.x] = f'[{decorated_lines[self.__player.y][self.__player.x]}]'
        for line in decorated_lines:
            Canvas.store_main([' '.join([part_name for part_name in line])])

        if self.__parts_lines[self.__player.y][self.__player.x] is not None:
            price = self.__parts_lines[self.__player.y][self.__player.x].price
            Canvas.store_main([f'{price}円'])

        Canvas.store_main([
            'sキーで購入',
            'Sキーで退店して次のステージへ',
        ])

        part_names = [p.name for p in self.__player.parts]
        decorated_part_names = [' '.join(part_names[i:i + 6]) for i in range(0, len(part_names), 6)]
        Canvas.store_side(['所持パーツ'])
        Canvas.store_side(decorated_part_names)

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
                Canvas.store_main(['もうないよ'])
                return self

            self.__parts_lines[self.__player.y][self.__player.x] = None
            self.__player.pick_up(item)
            Canvas.store_main(['どうもね'])
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
