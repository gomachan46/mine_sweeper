from bomb import Bomb
from goal import Goal
from point import Point
from safe import Safe
from start import Start
from wall import Wall


class Field:
    def __init__(self, width, height, cells):
        self.__goal = Point(((width - 1) // 2) + 1, 0)  # あとで追加される壁ブロックを見越して設定しておく
        self.__start = Point(((width - 1) // 2) + 1, height + 1)  # あとで追加される壁ブロックを見越して設定しておく
        # スタート行とゴール行の構築
        goal_line = [Wall()] * (width - 1)
        start_line = [Wall()] * (width - 1)
        goal_line.insert(self.__goal.x - 1, Goal())
        start_line.insert(self.__start.x - 1, Start())
        cells = [cells[i:i + width] for i in range(0, width * height, width)]
        # 初動3マス絶対安全エリアの確保
        cells[-1][self.__start.x - 1] = Safe()
        cells[-1][self.__start.x] = Safe()
        cells[-1][self.__start.x + 1] = Safe()
        cells.insert(0, goal_line)
        cells.append(start_line)
        # 両側の壁の構築
        for index, _ in enumerate(cells):
            cells[index].insert(0, Wall())
            cells[index].append(Wall())
        self.__width = len(cells[0])
        self.__height = len(cells)

        for y in range(self.__height):
            for x in range(self.__width):
                if not isinstance(cells[y][x], Bomb):
                    continue

                surroundings = [
                    (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                    (x - 1, y),                 (x + 1, y),
                    (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
                ]
                for s_x, s_y in surroundings:
                    if s_x in range(self.__width) and s_y in range(self.__height) and isinstance(cells[s_y][s_x], Safe):
                        cells[s_y][s_x].count_up()
        self.__cells = cells

    def open_cell(self, x, y):
        self.__cells[y][x].open()

    def get_texts(self):
        return [[c.get_text() for c in row] for row in self.__cells]

    @property
    def goal(self):
        return self.__goal

    @property
    def start(self):
        return self.__start
