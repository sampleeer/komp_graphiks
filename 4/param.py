import numpy as np

width = 600
height = 600
mid = (width // 2, height // 2)

matrix_up = [[1, 0, 0],
			 [0, 1, 0],
			 [0, 5, 1]]

matrix_down = [[1, 0, 0],
			   [0, 1, 0],
			   [0, -5, 1]]

matrix_right = [[1, 0, 0],
				[0, 1, 0],
				[5, 0, 1]]

matrix_left = [[1, 0, 0],
			   [0, 1, 0],
			   [-5, 0, 1]]

scale_x_up = [[2, 0, 0],
			  [0, 1, 0],
			  [0, 0, 1]]

scale_y_up = [[1, 0, 0],
			  [0, 2, 0],
			  [0, 0, 1]]

scale_x_down = [[0.5, 0, 0],
				[0, 1, 0],
				[0, 0, 1]]

scale_y_down = [[1, 0, 0],
				[0, 0.5, 0],
				[0, 0, 1]]

symmetry_ox = [[-1, 0, 0],
			   [0, 1, 0],
			   [0, 0, 1]]

symmetry_oy = [[1, 0, 0],
			   [0, -1, 0],
			   [0, 0, 1]]

symmetry_yx = [[0, 1, 0],
			   [1, 0, 0],
			   [0, 0, 1]]


def rotation_matrix(angel: float):
	return [[np.cos(angel), np.sin(angel), 0],
			[-np.sin(angel), np.cos(angel), 0],
			[0, 0, 1]]


def rotation_matrix_relative_point(coordinates: (float, float), angel: float):
	matr_coord1 = np.array([[1, 0, 0],
				   [0, 1, 0],
				   [-coordinates[0], -coordinates[1], 1]])
	matr_coord2 = np.array([[1, 0, 0],
				   [0, 1, 0],
				   [coordinates[0], coordinates[1], 1]])

	return matr_coord1 @ rotation_matrix(angel) @ matr_coord2
