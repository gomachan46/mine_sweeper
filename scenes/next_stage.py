from canvas import Canvas
from scenes.player_creation import PlayerCreation
from scenes.scene import Scene


class NextStageGoal(Scene):
    def __init__(self, player, next_level):

    def draw(self):
        Canvas.store([
            'ドキドキ地雷パニック',
            'Press Any Button',
            'Note: `exit`と入力することでいつでも終了できます'
        ])

    def next(self, key):
        return PlayerCreation()
