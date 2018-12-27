class Power:
    ICON = '?'

    def __init__(self, value):
        self.__value = value
        self.__name = f'パワー+{value}'

    @property
    def value(self):
        return self.__value

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return self.name
