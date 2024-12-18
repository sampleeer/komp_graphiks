import numpy as np

from param import mid

class Point:
	def __init__(self, x, y, z=1):
		self.__x = x
		self.__y = y
		self.__z = z

	def copy(self):
		return Point(self.__x, self.__y, self.__z)

	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y

	@x.setter
	def x(self, val):
		self.__x = val

	@y.setter
	def y(self, val):
		self.__y = val

	def mult_mat(self, mat):
		newCoors = list(np.dot([self.__x, self.__y, self.__z], mat))
		self.__x, self.__y, self.__z = newCoors[0], newCoors[1], newCoors[2]

	@property
	def coors(self):
		return mid[0] + self.__x, mid[1] - self.__y

	@property
	def coors_norm(self):
		return self.__x, self.__y