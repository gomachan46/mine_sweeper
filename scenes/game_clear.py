from canvas import Canvas
from items.attack import Attack
from items.defence import Defence
from scenes.scene import Scene


class GameClear(Scene):
    def __init__(self, player):
        self.__player = player

    def draw(self):
        attack = 0
        defence = 0
        for part in self.__player.parts:
            if isinstance(part, Attack):
                attack += part.value
            elif isinstance(part, Defence):
                defence += part.value
        Canvas.store_main([
            'おめでとう！',
            'こんな選手が登録されました(まだされないけど)',
            f'攻撃力: {attack}',
            f'防御力: {defence}',
        ])

    def next(self, _):
        from scenes.title import Title
        return Title()
