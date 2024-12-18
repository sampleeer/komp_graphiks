from laba2.param import *
from laba2.point import Point

start_pos = [(-50.0, -50.0), (-50.0, 50.0), (50.0, 50.0), (50.0, -50.0),
			 (-50.0, -50.0), (-13.745, -4.564), (0.0, 50.0), (13.745, -4.564),
			 (50.0, -50.0), (0.0, -28.371), (-50.0, -50.0)]


class Star:
	def __init__(self, canvas):
		self.canvas = canvas
		self.__lines: list = []
		self.__points: list[Point] = [Point(*coor) for coor in start_pos]
		for i in range(len(self.__points) - 1):
			self.__lines.append(self.canvas.create_line(self.__points[i].coors,
														  self.__points[
															  i + 1].coors,
														  fill='red', width=2))

	def __change_lines(self):
		for i in range(len(self.__points) - 1):
			self.canvas.coords(self.__lines[i], *self.__points[i].coors,
								 *self.__points[i + 1].coors)

	def __change_coors(self, mat):
		for p in self.__points:
			p.mult_mat(mat)
		self.__change_lines()

	def shift_up(self):
		self.__change_coors(matrix_up)

	def shift_down(self):
		self.__change_coors(matrix_down)

	def shift_right(self):
		self.__change_coors(matrix_right)

	def shift_left(self):
		self.__change_coors(matrix_left)

	def reflect_x(self):
		self.__change_coors(symmetry_ox)

	def reflect_y(self):
		self.__change_coors(symmetry_oy)

	def reflect_yx(self):
		self.__change_coors(symmetry_yx)

	def scalex_up(self):
		self.__change_coors(scale_x_up)

	def scalex_down(self):
		self.__change_coors(scale_x_down)

	def scaley_up(self):
		self.__change_coors(scale_y_up)

	def scaley_down(self):
		self.__change_coors(scale_y_down)

	def turn_star(self, angel: float):
		angel = (angel * np.pi) / 180
		self.__change_coors(rotation_matrix(angel))

	def turn_star_to_point(self, coordinates: (float, float), angel: float):
		angel = (angel * np.pi) / 180
		self.__change_coors(rotation_matrix_relative_point(coordinates, angel))

	def go_begin(self):
		self.__points: list[Point] = [Point(*coor) for coor in start_pos]
		self.__change_lines()
