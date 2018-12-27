class Gold:
    ICON = 'G'

    def __init__(self, value):
        self.__value = value
        self.__name = f'{value}円'

    @property
    def value(self):
        return self.__value

    @property
    def name(self):
        return self.__name
