class Gold:
    ICON = '$'

    def __init__(self, value):
        self.__value = value
        self.__name = f'{value} gold'

    @property
    def value(self):
        return self.__value

    @property
    def name(self):
        return self.__name

    def __add__(self, other):
        return Gold(self.value + other.value)

    def __str__(self):
        return self.name
