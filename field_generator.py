import random

from bomb import Bomb
from field import Field
from item_generator import ItemGenerator
from safe import Safe


class FieldGenerator:
    @classmethod
    def generate(cls, width, height, bomb_amount):
        cell_amount = width * height
        cells = [Safe(item=ItemGenerator.generate(0.2)) for _ in range(cell_amount)]
        indexes = random.sample(range(cell_amount), bomb_amount)
        for i in indexes:
            cells[i] = Bomb()

        return Field(width, height, cells)

    @classmethod
    def generate_by_level(cls, level):
        width = 9 - 1 + level
        height = 9 - 1 + level
        bomb_amount = 5 - 1 + level
        return cls.generate(width, height, bomb_amount)
