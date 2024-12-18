from matplotlib.lines import Line2D
from matplotlib.patches import Polygon
from andrew import convex_hull

import matplotlib.pyplot as plt
from celluloid import Camera
import os

import numpy as np
def points_to_data(points: list[tuple[int]]) -> tuple[list[int]]:

    x, y = [], []
    for item in points:
        x.append(item[0])
        y.append(item[1])

    return x, y

# Функция для вычисления векторного произведения трех точек
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


# Функция для вычисления уравнения прямой по двум точкам
def line_by_points(point0, point1):
    a = point1[1] - point0[1]
    b = point0[0] - point1[0]
    c = point1[0] * point0[1] - point0[0] * point1[1]
    return a, b, c

# Функция для определения, находится ли точка на прямой или справа от нее
def on_line(point, a, b, c):
    return (point[0] * a + point[1] * b + c) >0

# Основная функция для построения выпуклой оболочки
def convex_hull(points, ax, cam):
    # Сортируем точки
    points = sorted(set(points))

    # Находим крайние левую и правую точки
    left_point = points[0]
    right_point = points[0]
    for point in points:
        if point[0] < left_point[0]:
            left_point = point
        if point[0] > right_point[0]:
            right_point = point

    # Вычисляем уравнение прямой через крайние точки
    ln = line_by_points(left_point, right_point)

    # Разделяем точки на верхнюю и нижнюю части от прямой
    upper_points = sorted(set([item for item in points if on_line(item, *ln)]))
    lower_points = sorted(set([item for item in points if not on_line(item, *ln)]), reverse=True)
    upper_points = [left_point , *upper_points, right_point]

    # Проверка на возможность построения оболочки
    if len(points) <= 1 or len(upper_points) <= 1 or len(lower_points) <= 1:
        return points

    # Строим нижнюю оболочку
    lower = []
    for p in lower_points:
        # Если точки образуют невыпуклый угол
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
        # Визуализируем ребра нижней оболочки
        if len(lower) > 1:
            size = len(lower)
            for idx in range(size):
                line = [lower[idx], lower[(idx + 1) % size]]
                ax.add_line(Line2D(*points_to_data(line), color='red'))
            cam.snap()

    # Строим верхнюю оболочку
    upper = []
    for p in upper_points:
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            # Если точки образуют невыпуклый угол
            upper.pop()
        upper.append(p)
        # Визуализируем ребра верхней оболочки
        if len(upper) > 1:
            ax.add_patch(Polygon(lower, fc='none', ec='blue'))
            size = len(upper)
            for idx in range(size):
                line = [upper[idx], upper[(idx + 1) % size]]
                ax.add_line(Line2D(*points_to_data(line), color='green'))
            cam.snap()

    # Объединяем нижнюю и верхнюю оболочки
    hull = lower + upper
    # Визуализируем точки и оболочку
    ax.scatter(*points_to_data(points), color='blue')
    ax.add_patch(Polygon(hull, fc='none', ec='black'))
    cam.snap()

    # Возвращаем точки оболочки за исключением последних точек (дубликатов)
    return lower + upper






def read_file_points():
    return list(map(lambda item: tuple(item), np.loadtxt('7.txt').tolist()))
def points_to_data(points: list[tuple[int]]) -> tuple[list[int]]:

    x, y = [], []
    for item in points:
        x.append(item[0])
        y.append(item[1])

    return x, y

def main():

    while True:

        fig = plt.figure()
        camera = Camera(fig)
        ax = fig.add_subplot()

        points = read_file_points()
        convex_hull(points, ax, camera)
        ax.scatter(*points_to_data(points), color='blue')
        animation = camera.animate(interval=1800)
        animation.save('anim.gif')
        plt.show()
        os.system('clear')



if __name__ == '__main__':
    main()










