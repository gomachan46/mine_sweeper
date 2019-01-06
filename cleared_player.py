class ClearedPlayer:
    def __init__(self, name, attack, defence):
        self.__name = name
        self.__attack = attack
        self.__defence = defence

    @property
    def name(self):
        return self.__name

    @property
    def attack(self):
        return self.__attack

    @property
    def defence(self):
        return self.__defence
