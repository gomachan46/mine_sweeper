import random

from items.attack import Attack
from items.defence import Defence
from items.gold import Gold


class ItemGenerator:
    @classmethod
    def generate(cls, ratio, rarity):
        roulette = random.random() < ratio
        candidates = [
            Gold.generate_by_rarity(rarity),
            Attack.generate_by_rarity(rarity),
            Defence.generate_by_rarity(rarity),
        ]
        return random.choice(candidates) if roulette is True else None
