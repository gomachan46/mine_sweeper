import random

from items.attack import Attack
from items.defence import Defence
from items.gold import Gold


class ItemGenerator:
    @classmethod
    def generate(cls, ratio):
        roulette = random.random() < ratio
        candidates = [
            Gold(500),
            Attack(5),
            Defence(5),
        ]
        return random.choice(candidates) if roulette is True else None
