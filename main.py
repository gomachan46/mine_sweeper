import textwrap

from game import Game


def main():
    game = Game.start()
    message = None
    is_player_visible = True

    while True:
        x = 0
        y = 0
        toggle_mark = False
        for index, text in enumerate(game.field.get_texts()):
            if is_player_visible is True and index == game.player.y:
                text[game.player.x] = 'P'
            print(' '.join(text))
        print('stage:', str(Game.stage))
        print('steps:', str(game.player.steps))
        print('foot:', str(game.get_foot_cell()))

        if message is not None:
            print(message)
            message = None

        if game.player.is_dead():
            break

        inp = input(textwrap.dedent('''
        Available keys:
          move on:
            q w e
            a   d
            z x c
          mark:
            Q W E
            A   D
            Z X C
          show/hide player:
            s or S
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
        elif inp == 'Q':
            x -= 1
            y -= 1
            toggle_mark = True
        elif inp == 'A':
            x -= 1
            toggle_mark = True
        elif inp == 'Z':
            x -= 1
            y += 1
            toggle_mark = True
        elif inp == 'W':
            y -= 1
            toggle_mark = True
        elif inp == 'X':
            y += 1
            toggle_mark = True
        elif inp == 'E':
            x += 1
            y -= 1
            toggle_mark = True
        elif inp == 'D':
            x += 1
            toggle_mark = True
        elif inp == 'C':
            x += 1
            y += 1
            toggle_mark = True
        elif inp == 's' or inp == 'S':
            is_player_visible = not is_player_visible
            continue
        elif inp == 'exit':
            break
        else:
            message = 'Invalid input'
            continue

        message = game.next(x, y, toggle_mark)


main()
