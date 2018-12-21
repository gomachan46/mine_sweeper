import random

def main():
    side_length = 9
    bomb_count = 10
    field = [[{'type': 'Safe', 'count': 0, 'visible': False} for _ in range(side_length)] for _ in range(side_length)]

    candidates = range(side_length)
    for _ in range(bomb_count):
        def roulette():
            r, c = random.sample(candidates, 2)
            if field[r][c]['type'] == 'Bomb':
                roulette()
            field[r][c] = {'type': 'Bomb', 'visible': False}
        roulette()

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

    start_r = 8
    start_c = 4
    open_cell(start_r, start_c)

    def draw_field():
        for index, rows in enumerate(field):
            def draw_cell(c):
                if not c['visible']:
                    return ' '
                return str(c['count']) if c['type'] == 'Safe' else 'B'

            texts = list(map(draw_cell, rows))
            if index == start_r:
                texts[start_c] = '\033[32m' + texts[start_c] + '\033[0m'
            print(' '.join(texts))

    while True:
        draw_field()
        inp = input('hjklで入力して。hで左jで下kで上lで右に動くよ。exitで終わります').strip()
        if inp == 'h':
            start_c -= 1
        elif inp == 'j':
            start_r += 1
        elif inp == 'k':
            start_r -= 1
        elif inp == 'l':
            start_c += 1
        elif inp == 'exit':
            break
        else:
            print('ちゃんと入力しろ')

        open_cell(start_r, start_c)

main()
