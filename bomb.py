from cell import Cell


class Bomb(Cell):
    TEXT = 'B'

    def __init__(self, visible=False):
        super().__init__(self.TEXT, visible)
