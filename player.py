class Player:
    STATUS_HEALTHY = 'healthy'
    STATUS_DEAD = 'dead'

    def __init__(self, point):
        self.__point = point
        self.__x = self.__point.x
        self.__y = self.__point.y
        self.__status = self.STATUS_HEALTHY

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
    def point(self):
        return self.__point

    @point.setter
    def point(self, value):
        self.__point = value
        self.__x = self.__point.x
        self.__y = self.__point.y

    def pass_away(self):
        self.__status = self.STATUS_DEAD

    def is_healthy(self):
        return self.__status == self.STATUS_HEALTHY

    def is_dead(self):
        return self.__status == self.STATUS_DEAD
