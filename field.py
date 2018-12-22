from bomb import Bomb
from safe import Safe


class Field:
    def __init__(self, width, height, cells):
        self.width = width
        self.height = height
        cells = [cells[i:i + width] for i in range(0, width * height, width)]
        for row in range(height):
            for col in range(width):
                if not isinstance(cells[row][col], Bomb):
                    continue

                surroundings = [(row - 1, col - 1), (row, col - 1), (row + 1, col - 1), (row - 1, col), (row + 1, col),
                                (row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]
                for r, c in surroundings:
                    if r in range(height) and c in range(width) and isinstance(cells[r][c], Safe):
                        cells[r][c].count_up()
        self.cells = cells

    def open_cell(self, r, c):
        self.cells[r][c].open()

    def get_texts(self):
        return [[r.get_text() for r in rows] for rows in self.cells]
