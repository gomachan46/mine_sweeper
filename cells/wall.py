from cells.cell import Cell


class Wall(Cell):
    TEXT = '.'

    def __init__(self, visible=True):
        super().__init__(self.TEXT, visible)
