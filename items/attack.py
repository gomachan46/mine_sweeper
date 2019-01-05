import random


class Attack:
    ICON = '?'

    def __init__(self, value):
        self.__value = value
        self.__price = value * 1000
        self.__name = f'攻撃力+{value}'

    @classmethod
    def generate_by_rarity(cls, rarity):
        candidates = range(1, rarity + 1)
        return cls(random.choice(candidates))

    @property
    def value(self):
        return self.__value

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name
