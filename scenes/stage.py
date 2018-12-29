from cells.bomb import Bomb
from canvas import Canvas
from field_generator import FieldGenerator
from cells.goal import Goal
from scenes.scene import Scene
from scenes.game_over import GameOver
from cells.wall import Wall
from scenes.shop import Shop


class Stage(Scene):
    def __init__(self, field, player, level):
        self.__field = field
        player.point = self.__field.start
        self.__player = player
        self.__level = level
        self.__is_player_visible = True

    @property
    def player(self):
        return self.__player

    @property
    def field(self):
        return self.__field

    def draw(self):
        for index, text in enumerate(self.__field.get_texts()):
            if self.__is_player_visible is True and index == self.player.y:
                text[self.__player.x] = 'P'
            Canvas.store([' '.join(text)])
        level = self.__level
        player_name = self.__player.name
        player_steps = self.__player.steps
        foot_cell = self.__field.get_cell(self.__player.x, self.__player.y)
        parts = ",".join([p.name for p in self.__player.parts])
        gold = self.__player.gold.name
        Canvas.store([
            f'ステージ: {level}',
            f'名前: {player_name}',
            f'歩数: {player_steps}',
            f'足元: {foot_cell}',
            f'お金: {gold}',
            f'パーツ: [{parts}]',
            '利用可能キー:',
            '移動:',
            '  q w e',
            '  a   d',
            '  z x c',
            'マーク:',
            '  Q W E',
            '  A   D',
            '  Z X C',
            'プレイヤーの表示/非表示:',
            '  s or S',
        ])

    def next(self, key):
        x, y, toggle_mark = self.__handle_key(key)
        if toggle_mark is True:
            self.__field.toggle_mark(self.__player.x + x, self.__player.y + y)
            return self

        self.__player.steps += 1
        self.__player.x += x
        self.__player.y += y
        opened = self.__field.open_cell(self.__player.x, self.__player.y)
        if opened is None:
            # マーク済のセルなどが理由で開けなかった場合
            self.__player.steps -= 1
            self.__player.x -= x
            self.__player.y -= y
            Canvas.store(['マークされていて進めません'])
        elif isinstance(opened, Bomb):
            return GameOver(self.__player)
        elif isinstance(opened, Wall):
            self.__player.steps -= 1
            self.__player.x -= x
            self.__player.y -= y
            Canvas.store(['壁なので進めません'])
        elif isinstance(opened, Goal):
            Canvas.store(['次のステージへ！'])
            next_level = self.__level + 1
            if self.__level % 5 == 0:
                return Shop(self.__player, next_level)

            field = FieldGenerator.generate_by_level(next_level)
            return Stage(field, self.__player, next_level)
        elif opened.item is not None:
            item = opened.drop_item()
            self.__player.pick_up(item)
            Canvas.store([f'{item.name}を手に入れた！'])

        return self

    def __handle_key(self, key):
        x = 0
        y = 0
        toggle_mark = False
        if key == 'q':
            x -= 1
            y -= 1
        elif key == 'a':
            x -= 1
        elif key == 'z':
            x -= 1
            y += 1
        elif key == 'w':
            y -= 1
        elif key == 'x':
            y += 1
        elif key == 'e':
            x += 1
            y -= 1
        elif key == 'd':
            x += 1
        elif key == 'c':
            x += 1
            y += 1
        elif key == 'Q':
            x -= 1
            y -= 1
            toggle_mark = True
        elif key == 'A':
            x -= 1
            toggle_mark = True
        elif key == 'Z':
            x -= 1
            y += 1
            toggle_mark = True
        elif key == 'W':
            y -= 1
            toggle_mark = True
        elif key == 'X':
            y += 1
            toggle_mark = True
        elif key == 'E':
            x += 1
            y -= 1
            toggle_mark = True
        elif key == 'D':
            x += 1
            toggle_mark = True
        elif key == 'C':
            x += 1
            y += 1
            toggle_mark = True
        elif key == 's' or key == 'S':
            self.__is_player_visible = not self.__is_player_visible
        else:
            Canvas.store(['正しく入力してください'])

        return x, y, toggle_mark
