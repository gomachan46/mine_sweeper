from canvas import Canvas
from player_creation import PlayerCreation
from scene import Scene


class Title(Scene):
    def draw(self):
        Canvas.store([
            'ドキドキ地雷パニック',
            'Press Any Button'
        ])

    def next(self, _):
        return PlayerCreation()
