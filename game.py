from canvas import Canvas
from title import Title


class Game:
    def __init__(self, scene=Title()):
        self.__scene = scene

    def draw(self):
        self.__scene.draw()
        return Canvas.draw()

    def next(self, key):
        self.__scene = self.__scene.next(key)

    @property
    def scene(self):
        return self.__scene
