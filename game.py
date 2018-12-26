from bomb import Bomb
from wall import Wall


class Game:
    def __init__(self, field, player):
        self.__field = field
        self.__player = player

    @property
    def player(self):
        return self.__player

    def judge(self):
        opened = self.__field.open_cell(self.__player.x, self.__player.y)
        if isinstance(opened, Bomb):
            self.__player.pass_away()
            return 'Player is dead...'
        elif isinstance(opened, Wall):
            return 'There is a wall'

        return None
