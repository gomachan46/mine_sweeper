from bomb import Bomb
from goal import Goal
from wall import Wall


class Stage:
    def __init__(self, field, player):
        self.__field = field
        player.point = self.__field.start
        self.__player = player

    @property
    def player(self):
        return self.__player

    @property
    def field(self):
        return self.__field

    def next(self, x, y, toggle_mark):
        if toggle_mark is True:
            self.__field.toggle_mark(self.__player.x + x, self.__player.y + y)
            return

        self.__player.steps += 1
        self.__player.x += x
        self.__player.y += y
        opened = self.__field.open_cell(self.__player.x, self.__player.y)
        if opened is None:
            # マーク済のセルなどが理由で開けなかった場合
            self.__player.steps -= 1
            self.__player.x -= x
            self.__player.y -= y
            return 'マークされていて進めません'
        elif isinstance(opened, Bomb):
            self.__player.pass_away()
            return '生きていればこんな選手でした'
        elif isinstance(opened, Wall):
            self.__player.steps -= 1  # 壁に当たるのはカウントしなくてもいいかな
            self.__player.x -= x
            self.__player.y -= y
            return '壁なので進めません'
        elif isinstance(opened, Goal):
            return '次のステージへ！'
        elif opened.item is not None:
            item = opened.drop_item()
            self.__player.pick_up(item)
            return f'{item.name}を手に入れた！'

        return None

    def get_foot_cell(self):
        return self.__field.get_cell(self.__player.x, self.__player.y)
