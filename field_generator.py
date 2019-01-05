import random

from cells.bomb import Bomb
from field import Field
from items.item_generator import ItemGenerator
from cells.safe import Safe


class FieldGenerator:
    @classmethod
    def generate(cls, width, height, bomb_amount, item_ratio, item_rarity):
        cell_amount = width * height
        cells = [Safe(item=ItemGenerator.generate(item_ratio, item_rarity)) for _ in range(cell_amount)]
        indexes = random.sample(range(cell_amount), bomb_amount)
        for i in indexes:
            cells[i] = Bomb()

        return Field(width, height, cells)

    @classmethod
    def generate_by_level(cls, level):
        width = 9 - 1 + level
        height = 9 - 1 + level
        bomb_amount = 5 - 1 + level
        item_ratio = ((level // 5) + 1) * 0.1
        item_rarity = (level // 5) + 1
        return cls.generate(width, height, bomb_amount, item_ratio, item_rarity)
