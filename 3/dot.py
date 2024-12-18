import numpy as np
from constants import WIDTH, HEIGHT, MIDDLE


class Dot:
    def __init__(self, x, y, z=1):
        self.__x = x
        self.__y = y
        self.__z = z

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

    def multMat(self, mat):
        newCoors = list(np.dot([self.__x, self.__y, self.__z], mat))
        self.__x, self.__y, self.__z = newCoors[0], newCoors[1], newCoors[2]

    @property
    def coors(self):
        return MIDDLE[0] + self.__x, MIDDLE[1] - self.__y

    @property
    def coors_norm(self):
        return self.__x, self.__y
