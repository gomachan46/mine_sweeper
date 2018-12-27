class Cell:
    TEXT_MARK = 'X'
    TEXT_INVISIBLE = ' '

    def __init__(self, text, visible):
        self.__text = text
        self.__visible = visible
        self.__mark = False

    def toggle_mark(self):
        if self.__visible is True:
            return
        self.__mark = not self.__mark

    def open(self):
        if self.__mark is True:
            return
        self.__visible = True
        return self

    def get_text(self):
        if self.__mark is True:
            return self.TEXT_MARK
        if self.__visible is False:
            return self.TEXT_INVISIBLE
        return self.__text

    def __str__(self):
        return self.get_text()
