from cells.bomb import Bomb
from canvas import Canvas
from cells.goal import Goal
from scenes.next_stage import NextStage
from scenes.scene import Scene
from scenes.game_over import GameOver
from cells.wall import Wall


class Stage(Scene):
    def __init__(self, field, player, level):
        self.__field = field
        player.point = self.__field.start
        self.__player = player
        self.__level = level

    @property
    def player(self):
        return self.__player

    @property
    def field(self):
        return self.__field

    def draw(self):
        for index, text in enumerate(self.__field.get_texts()):
            if self.__player.is_visible is True and index == self.player.y:
                text[self.__player.x] = 'P'
            Canvas.store_main([' '.join(text)])
        level = self.__level
        player_name = self.__player.name
        foot_cell = self.__field.get_cell(self.__player.x, self.__player.y)
        gold = self.__player.gold.name
        Canvas.store_side([
            f'ステージ: {level}',
            f'名前: {player_name}',
            f'足元: {foot_cell}',
            f'お金: {gold}',
            'パーツ:',
        ])

        part_names = [p.name for p in self.__player.parts]

        decorated_part_names = [' '.join(part_names[i:i + 6]) for i in range(0, len(part_names), 6)]
        Canvas.store_side(decorated_part_names)

        Canvas.store_side([
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

        self.__player.x += x
        self.__player.y += y
        opened = self.__field.open_cell(self.__player.x, self.__player.y)
        if opened is None:
            # マーク済のセルなどが理由で開けなかった場合
            self.__player.x -= x
            self.__player.y -= y
            Canvas.store_side(['マークされていて進めません'])
        elif isinstance(opened, Bomb):
            return GameOver(self.__player)
        elif isinstance(opened, Wall):
            self.__player.x -= x
            self.__player.y -= y
            Canvas.store_side(['壁なので進めません'])
        elif isinstance(opened, Goal):
            return NextStage(self.__player, self.__level)
        elif opened.item is not None:
            item = opened.drop_item()
            self.__player.pick_up(item)
            Canvas.store_side([f'{item.name}を手に入れた！'])

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
            self.__player.is_visible = not self.__player.is_visible
        else:
            Canvas.store_side(['正しく入力してください'])

        return x, y, toggle_mark
