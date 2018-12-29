from game import Game


def main():
    game = Game()

    while True:
        print(game.draw())
        key = input()
        if key == 'exit':
            break
        game.next(key)


main()
