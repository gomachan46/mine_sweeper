from cell import Cell


class Safe(Cell):
    def __init__(self, visible=True, count=0):
        super().__init__(str(count), visible)
        self.count = count

    def count_up(self):
        self.count += 1
        self.text = str(self.count)
