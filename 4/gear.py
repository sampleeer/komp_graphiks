from point import Point
from param import *

class gear:
	def __init__(self, canvas):
		self.canvas = canvas
		self.__centre = Point(0.0, 0.0)
		self.__gear_tooth: list = [Point(-10.0, 38.72), Point(-5.0, 50.0),
			  Point(5.0, 50.0), Point(10.0, 38.72)]
		self.__small_radius = 20.0
		self.__big_radius = 40.0

	def paint(self):
		for i in range(8):
			temp_tooth = []
			for p in self.__gear_tooth:
				temp_tooth.append(p.copy())
			for p in temp_tooth:
				p.mult_mat(
					rotation_matrix_relative_point((self.__centre.x, self.__centre.y), np.pi / 4 * i))

			self.canvas.create_polygon(temp_tooth[0].x, temp_tooth[0].y,
										 temp_tooth[1].x, temp_tooth[1].y,
										 temp_tooth[2].x, temp_tooth[2].y,
										 temp_tooth[3].x, temp_tooth[3].y, fill="black")
		self.canvas.create_oval(self.__centre.x - self.__big_radius,
								  self.__centre.y - self.__big_radius,
								  self.__centre.x + self.__big_radius,
								  self.__centre.y + self.__big_radius, fill="black")
		self.canvas.create_oval(self.__centre.x - self.__small_radius,
								  self.__centre.y - self.__small_radius,
								  self.__centre.x + self.__small_radius,
								  self.__centre.y + self.__small_radius,
								  fill="white")

	def move(self, x, y):
		self.__centre.x += x
		self.__centre.y += y
		for p in self.__gear_tooth:
			p.x += x
			p.y += y

	def rotation_gear(self, angle):
		for p in self.__gear_tooth:
			p.mult_mat(
				rotation_matrix_relative_point(
					(self.__centre.x, self.__centre.y), angle))











