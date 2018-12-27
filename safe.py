from cell import Cell


class Safe(Cell):
    def __init__(self, visible=False, count=0):
        super().__init__(str(count), visible)
        self.__count = count

    def count_up(self):
        self.__count += 1
        self.__text = str(self.__count)
