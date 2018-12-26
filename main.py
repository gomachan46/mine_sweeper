import textwrap

from field_generator import FieldGenerator
from game import Game
from player import Player


def main():
    width = 9
    height = 9
    bomb_amount = 10

    field = FieldGenerator.generate(width, height, bomb_amount)
    player = Player(field.start)
    game = Game(field, player)
    message = None

    while True:
        for text in field.get_texts():
            print(' '.join(text))

        if message is not None:
            print(message)

        if game.player.is_dead():
            break

        inp = input(textwrap.dedent('''
        Available keys:
        q w e
        a s d
        z x c
        Type `exit` to exit.
        '''))
        if inp == 'q':
            game.player.x -= 1
            game.player.y -= 1
        elif inp == 'a':
            game.player.x -= 1
        elif inp == 'z':
            game.player.x -= 1
            game.player.y += 1
        elif inp == 'w':
            game.player.y -= 1
        elif inp == 'x':
            game.player.y += 1
        elif inp == 'e':
            game.player.x += 1
            game.player.y -= 1
        elif inp == 'd':
            game.player.x += 1
        elif inp == 'c':
            game.player.x += 1
            game.player.y += 1
        elif inp == 'exit':
            break
        else:
            message = 'Invalid input'
            continue

        message = game.judge()


main()
