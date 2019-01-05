class Defence:
    ICON = '?'

    def __init__(self, value):
        self.__value = value
        self.__name = f'防御力+{value}'

    @property
    def value(self):
        return self.__value

    @property
    def name(self):
        return self.__name
