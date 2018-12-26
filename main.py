from field_generator import FieldGenerator


def main():
    width = 9
    height = 9
    bomb_amount = 10

    field = FieldGenerator.generate(width, height, bomb_amount)
    player_point = field.start

    while True:
        for text in field.get_texts():
            print(' '.join(text))

        inp = input('hjklで入力して。hで左jで下kで上lで右に動くよ。exitで終わります').strip()
        if inp == 'h':
            player_point.x -= 1
        elif inp == 'j':
            player_point.y += 1
        elif inp == 'k':
            player_point.y -= 1
        elif inp == 'l':
            player_point.x += 1
        elif inp == 'exit':
            break
        else:
            print('ちゃんと入力しろ')

        field.open_cell(player_point.x, player_point.y)

main()
