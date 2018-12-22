import random

from bomb import Bomb
from field import Field
from safe import Safe

class FieldGenerator:
    @classmethod
    def generate(cls, width, height, bomb_amount):
        cell_amount = width * height
        cells = [Safe() for _ in range(cell_amount)]
        indexes = random.sample(range(cell_amount), bomb_amount)
        for i in indexes:
            cells[i] = Bomb()

        return Field(width, height, cells)
