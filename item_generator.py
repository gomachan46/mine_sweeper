import random

from gold import Gold


class ItemGenerator:
    @classmethod
    def generate(cls, ratio):
        roulette = random.random() < ratio
        return Gold(500) if roulette is True else None
