from cell import Cell


class Start(Cell):
    TEXT = 'S'

    def __init__(self, visible=True):
        super().__init__(self.TEXT, visible)
