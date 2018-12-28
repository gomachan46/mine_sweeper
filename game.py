from field_generator import FieldGenerator
from player import Player
from stage import Stage


class Game:
    def __init__(self, width=9, height=9, bomb_amount=5, stage=1):
        self.__width = width
        self.__height = height
        self.__bomb_amount = bomb_amount
        self.__stage = stage

    def start(self):
        field = FieldGenerator.generate(self.__width, self.__height, self.__bomb_amount)
        player = Player()
        return Stage(field, player)
