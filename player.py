from gold import Gold
from point import Point


class Player:
    STATUS_HEALTHY = 'healthy'
    STATUS_DEAD = 'dead'

    def __init__(self, point=Point(0, 0)):
        self.__point = point
        self.__x = self.__point.x
        self.__y = self.__point.y
        self.__status = self.STATUS_HEALTHY
        self.__steps = 0
        self.__gold = Gold(0)
        self.__parts = []

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

    def pick_up(self, item):
        if isinstance(item, Gold):
            self.__gold += item
            return
        self.__parts.append(item)

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, value):
        self.__point = value
        self.__x = self.__point.x
        self.__y = self.__point.y

    @property
    def steps(self):
        return self.__steps

    @steps.setter
    def steps(self, value):
        self.__steps = value

    def pass_away(self):
        self.__status = self.STATUS_DEAD

    def is_healthy(self):
        return self.__status == self.STATUS_HEALTHY

    def is_dead(self):
        return self.__status == self.STATUS_DEAD
