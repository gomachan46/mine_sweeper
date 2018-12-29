import random

from items.gold import Gold
from items.power import Power


class ItemGenerator:
    @classmethod
    def generate(cls, ratio):
        roulette = random.random() < ratio
        return random.choice([Gold(500), Power(5)]) if roulette is True else None
