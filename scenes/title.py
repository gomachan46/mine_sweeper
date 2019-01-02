from canvas import Canvas
from scenes.player_creation import PlayerCreation
from scenes.scene import Scene


class Title(Scene):
    def draw(self):
        Canvas.store_main([
            'ドキドキ地雷パニック',
            'Press Any Button',
            'Note: `exit`と入力することでいつでも終了できます'
        ])

    def next(self, _):
        return PlayerCreation()
