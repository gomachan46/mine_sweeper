from cell import Cell


class Safe(Cell):
    def __init__(self, visible=False, count=0, item=None):
        super().__init__(str(count), visible, item)
        self.__count = count

    def count_up(self):
        self.__count += 1
        self.set_text(str(self.__count))
