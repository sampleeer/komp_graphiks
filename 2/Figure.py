from math import pi, sin, cos
import numpy as np


class Point:
    def __init__(self, x=0, y=0, z=1):
        self.coordinate = np.array([x, y, z])

    def __eq__(self, other):
        return self.coordinate == other.coordinate

    def get_x(self, flag=True):
        if flag:
            return self.coordinate[0] + 500
        return self.coordinate[0]

    def get_y(self, flag=True):
        if flag:
            return -self.coordinate[1] + 500
        return self.coordinate[1]

class Figure:
    def __init__(self, *args):
        self.points = args
        self.count = len(args)
        self.actions = []

    def x_axis_shift(self, a):
        matrix = np.array([[1, 0, a],
                           [0, 1, 0],
                           [0, 0, 1]])

        for i in range(self.count):
            self.points[i].coordinate = np.dot(matrix, self.points[i].coordinate)
        self.actions.append([1, a])

    def y_axis_shift(self, a):
        matrix = np.array([[1, 0, 0],
                           [0, 1, a],
                           [0, 0, 1]])

        for i in range(self.count):
            self.points[i].coordinate = np.dot(matrix, self.points[i].coordinate)
        self.actions.append([2, a])

    def x_reflection(self):
        matrix = np.array([[1, 0, 0],
                           [0, -1, 0],
                           [0, 0, 1]])

        for i in range(self.count):
            self.points[i].coordinate = np.dot(matrix, self.points[i].coordinate)
        self.actions.append([3])

    def y_reflection(self):
        matrix = np.array([[-1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])

        for i in range(self.count):
            self.points[i].coordinate = np.dot(matrix, self.points[i].coordinate)
        self.actions.append([4])

    def centre_reflection(self):
        matrix = np.array([[-1, 0, 0],
                           [0, -1, 0],
                           [0, 0, 1]])

        for i in range(self.count):
            self.points[i].coordinate = np.dot(matrix, self.points[i].coordinate)
        self.actions.append([5])

    def xy_reflection(self):
        matrix = np.array([[0, 1, 0],
                           [1, 0, 0],
                           [0, 0, 1]])

        for i in range(self.count):
            self.points[i].coordinate = np.dot(matrix, self.points[i].coordinate)
        self.actions.append([6])

    def x_scaling(self, k):
        matrix = np.array([[k, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])

        for i in range(self.count):
            self.points[i].coordinate = np.dot(matrix, self.points[i].coordinate)
        self.actions.append([7, k])

    def y_scaling(self, k):
        matrix = np.array([[1, 0, 0],
                           [0, k, 0],
                           [0, 0, 1]])

        for i in range(self.count):
            self.points[i].coordinate = np.dot(matrix, self.points[i].coordinate)
        self.actions.append([8, k])

    def xy_scaling(self, k):
        matrix = np.array([[k, 0, 0],
                           [0, k, 0],
                           [0, 0, 1]])

        for i in range(self.count):
            self.points[i].coordinate = np.dot(matrix, self.points[i].coordinate)
        self.actions.append([9, k])

    def turn(self, alpha=0, point=Point()):
        alpha = alpha * pi / 180
        s, c = sin(alpha), cos(alpha)
        matrix = np.array([[c, -s, -c * point.coordinate[0] + s * point.coordinate[1] + point.coordinate[0]],
                           [s, c, -s * point.coordinate[0] - c * point.coordinate[1] + point.coordinate[1]],
                           [0, 0, 1]])

        for i in range(self.count):
            self.points[i].coordinate = np.dot(matrix, self.points[i].coordinate)
        self.actions.append([10, alpha * 180 / pi, point])

    def delete(self):
        del self.actions[-1]

    def get_count_actions(self):
        return len(self.actions)

    def get_last_action(self):
        return self.actions[-1]

