from canvas import Canvas
from power import Power
from scene import Scene


class GameOver(Scene):
    def __init__(self, player):
        self.__player = player

    def draw(self):
        power = 0
        for part in self.__player.parts:
            if isinstance(part, Power):
                power += part.value
        Canvas.store([
            '生きていればこんな選手でした',
            f'パワー: {power}',
        ])

    def next(self, _):
        from title import Title
        return Title()
