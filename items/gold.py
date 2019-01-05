import random


class Gold:
    ICON = '$'

    def __init__(self, value):
        if value < 0:
            raise ValueError('Goldは0以上の数でなければなりません')
        self.__value = value
        self.__price = value
        self.__name = f'{value}円'

    @classmethod
    def generate_by_rarity(cls, rarity):
        candidates = range(1, (rarity + 1) * 100)
        return cls(random.choice(candidates))

    @property
    def value(self):
        return self.__value

    @property
    def name(self):
        return self.__name

    def __add__(self, other):
        return Gold(self.value + other.value)

    def __sub__(self, other):
        return Gold(self.value - other.value)

    def __str__(self):
        return self.name
