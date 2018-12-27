from cell import Cell


class Bomb(Cell):
    TEXT = 'B'

    def __init__(self, visible=True):
        super().__init__(self.TEXT, visible)
