from canvas import Canvas
from items.power import Power
from scenes.scene import Scene


class GameOver(Scene):
    def __init__(self, player):
        self.__player = player

    def draw(self):
        power = 0
        for part in self.__player.parts:
            if isinstance(part, Power):
                power += part.value
        Canvas.store_main([
            '生きていればこんな選手でした',
            f'パワー: {power}',
        ])

    def next(self, _):
        from scenes.title import Title
        return Title()
