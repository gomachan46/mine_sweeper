import random

def main():
    side_length = 9
    bomb_count = 10
    field = [[{'type': 'Safe', 'count': 0, 'visible': False} for _ in range(side_length)] for _ in range(side_length)]

    candidates = range(side_length)
    for _ in range(bomb_count):
        a, b = random.sample(candidates, 2)
        field[a][b] = {'type': 'Bomb', 'visible': False}

    for i in range(side_length):
        for j in range(side_length):
            if not field[i][j]['type'] == 'Bomb':
                continue

            surroundings = [(i - 1, j - 1), (i, j - 1), (i + 1, j - 1), (i - 1, j), (i + 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]
            for r, c in surroundings:
                if r in range(side_length) and c in range(side_length) and field[r][c]['type'] == 'Safe':
                    field[r][c]['count'] += 1

    def open_cell(r, c):
        field[r][c]['visible'] = True

    open_cell(8, 4)
    open_cell(8, 5)
    open_cell(7, 4)

    for rows in field:
        def write_cell(c):
            if not c['visible']:
                return ' '
            return str(c['count']) if c['type'] == 'Safe' else 'B'

        print(' '.join(map(write_cell, rows)))

main()
