from canvas import Canvas
from items.power import Power
from scenes.scene import Scene


class GameClear(Scene):
    def __init__(self, player):
        self.__player = player

    def draw(self):
        power = 0
        for part in self.__player.parts:
            if isinstance(part, Power):
                power += part.value
        Canvas.store([
            'おめでとう！',
            'こんな選手が登録されました(まだされないけど)',
            f'パワー: {power}',
        ])

    def next(self, _):
        from scenes.title import Title
        return Title()
