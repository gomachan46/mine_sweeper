from items.gold import Gold
from point import Point


class Player:
    def __init__(self, name, point=Point(0, 0), gold=Gold(0), parts=None, is_visible=True):
        if parts is None:
            parts = []
        self.__name = name
        self.__point = point
        self.__x = self.__point.x
        self.__y = self.__point.y
        self.__gold = gold
        if parts is None:
            parts = []
        self.__parts = parts
        self.__is_visible = is_visible

    @property
    def name(self):
        return self.__name

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def gold(self):
        return self.__gold

    @property
    def parts(self):
        return self.__parts

    @property
    def is_visible(self):
        return self.__is_visible

    @is_visible.setter
    def is_visible(self, value):
        self.__is_visible = value

    def pick_up(self, item):
        if isinstance(item, Gold):
            self.__gold += item
            return
        self.__parts.append(item)

    def buy(self, item):
        self.__gold -= item.price
        self.__parts.append(item)

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, value):
        self.__point = value
        self.__x = self.__point.x
        self.__y = self.__point.y
