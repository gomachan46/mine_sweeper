import random

from items.attack import Attack
from items.defence import Defence
from items.gold import Gold
from items.power import Power


class ItemGenerator:
    @classmethod
    def generate(cls, ratio):
        roulette = random.random() < ratio
        candidates = [
            Gold(500),
            Power(5),
            Attack(5),
            Defence(5),
        ]
        return random.choice(candidates) if roulette is True else None
