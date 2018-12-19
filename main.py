import random

def main():
    side_length = 9
    bomb_count = 10
    field = [[{'type': 'Safe', 'count': 0} for _ in range(side_length)] for _ in range(side_length)]

    candidates = range(side_length)
    for _ in range(bomb_count):
        a, b = random.sample(candidates, 2)
        field[a][b] = {'type': 'Bomb'}

    for i in range(side_length):
        for j in range(side_length):
            if field[i][j]['type'] == 'Bomb':
                for a, b in [(i - 1, j - 1), (i, j - 1), (i + 1, j - 1), (i - 1, j), (i + 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]:
                    if a in range(side_length) and b in range(side_length) and field[a][b]['type'] == 'Safe':
                        field[a][b]['count'] += 1

    for rows in field:
        print(' '.join([str(c['count']) if c['type'] == 'Safe' else 'B' for c in rows]))

main()
