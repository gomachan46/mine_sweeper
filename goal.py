from cell import Cell


class Goal(Cell):
    TEXT = 'G'

    def __init__(self, visible=True):
        super().__init__(self.TEXT, visible)
