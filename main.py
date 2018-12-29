import textwrap

from game import Game


def main():
    game = Game()
    stage = game.start()
    message = None
    is_player_visible = True

    while True:
        x = 0
        y = 0
        toggle_mark = False
        for index, text in enumerate(stage.field.get_texts()):
            if is_player_visible is True and index == stage.player.y:
                text[stage.player.x] = 'P'
            print(' '.join(text))
        print('ステージ:', str(game.stage))
        print('歩数:', str(stage.player.steps))
        print('足元:', str(stage.get_foot_cell()))
        print('お金:', str(stage.player.gold.name))
        print('パーツ:', f'[{",".join(map(str, stage.player.parts))}]')

        if message is not None:
            print(message)
            message = None

        if stage.player.is_dead():
            break

        inp = input(textwrap.dedent('''
        利用可能キー:
          移動:
            q w e
            a   d
            z x c
          マーク:
            Q W E
            A   D
            Z X C
          プレイヤーの表示/非表示:
            s or S
        終了するには`exit`と入力してください
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
            message = '正しく入力してください'
            continue

        message = stage.next(x, y, toggle_mark)


main()
