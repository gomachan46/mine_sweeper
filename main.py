import textwrap

from game import Game


def main():
    game = Game.start()
    message = None

    while True:
        x = 0
        y = 0
        for text in game.field.get_texts():
            print(' '.join(text))
        print('stage:', str(Game.stage))
        print('steps:', str(game.player.steps))

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
            x -= 1
            y -= 1
        elif inp == 'a':
            x -= 1
        elif inp == 'z':
            x -= 1
            y += 1
        elif inp == 'w':
            y -= 1
        elif inp == 'x':
            y += 1
        elif inp == 'e':
            x += 1
            y -= 1
        elif inp == 'd':
            x += 1
        elif inp == 'c':
            x += 1
            y += 1
        elif inp == 'exit':
            break
        else:
            message = 'Invalid input'
            continue

        message = game.next(x, y)


main()
