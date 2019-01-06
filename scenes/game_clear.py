from canvas import Canvas
from cleared_player import ClearedPlayer
from items.attack import Attack
from items.defence import Defence
from scenes.scene import Scene


class GameClear(Scene):
    def __init__(self, player):
        attack = 0
        defence = 0
        for part in player.parts:
            if isinstance(part, Attack):
                attack += part.value
            elif isinstance(part, Defence):
                defence += part.value
        self.__cleared_player = ClearedPlayer(player.name, attack, defence)
        from game import Game
        Game.data['cleared_players'].append(self.__cleared_player)

    def draw(self):
        Canvas.store_main([
            'おめでとう！',
            'こんな選手が登録されました',
            f'名前: {self.__cleared_player.name}',
            f'攻撃力: {self.__cleared_player.attack}',
            f'防御力: {self.__cleared_player.defence}',
        ])

    def next(self, _):
        from scenes.title import Title
        return Title()
