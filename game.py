from bomb import Bomb
from field_generator import FieldGenerator
from goal import Goal
from player import Player
from wall import Wall


# NOTE: GameとStageっていう概念を設けてもうちょっとハッキリさせたほうが良いかも
class Game:
    width = 0
    height = 0
    bomb_amount = 0
    stage = 1

    def __init__(self, field, player):
        self.__field = field
        player.point = self.__field.start
        self.__player = player

    @classmethod
    def start(cls, width=9, height=9, bomb_amount=5):
        cls.width = width
        cls.height = height
        cls.bomb_amount = bomb_amount
        return cls(FieldGenerator.generate(width, height, bomb_amount), Player())

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
            return 'Can not open. Is it marked?'
        elif isinstance(opened, Bomb):
            self.__player.pass_away()
            return 'Player is dead...'
        elif isinstance(opened, Wall):
            self.__player.steps -= 1  # 壁に当たるのはカウントしなくてもいいかな
            self.__player.x -= x
            self.__player.y -= y
            return 'There is a wall'
        elif isinstance(opened, Goal):
            Game.width += 1
            Game.height += 1
            Game.bomb_amount += 1
            Game.stage += 1
            self.__field = FieldGenerator.generate(Game.width, Game.height, Game.bomb_amount)
            self.__player.point = self.__field.start
            return 'There is a goal! Next stage!'
        elif opened.item is not None:
            item = opened.drop_item()
            return f'{item.name}を手に入れた！'

        return None

    def get_foot_cell(self):
        return self.__field.get_cell(self.__player.x, self.__player.y)
