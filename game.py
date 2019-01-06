import shelve

from canvas import Canvas
from scenes.title import Title


class Game:
    DATA_FILE = '.mine_sweeper/mine_sweeper.db'
    data = {
        'players': [],
    }

    def __init__(self, scene=Title()):
        self.__scene = scene
        self.load()

    def draw(self):
        self.__scene.draw()
        return Canvas.draw()

    def next(self, key):
        self.__scene = self.__scene.next(key)
        self.save()

    @property
    def scene(self):
        return self.__scene

    @classmethod
    def save(cls):
        db = shelve.open(cls.DATA_FILE)
        db['data'] = cls.data
        db.close()

    @classmethod
    def load(cls):
        db = shelve.open(cls.DATA_FILE)
        cls.data = db['data']
        for player in cls.data['players']:
            print(player.name)
        db.close()
