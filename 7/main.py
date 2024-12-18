import math
import tkinter as tk
from typing import Union
from functools import cmp_to_key

# Константы ______________________________________________________________________

width = 800
height = 800
center = (400, 400)
radius = 5

Dots = []
Lines = []
interLines = []


# Классы точки ___________________________________________________________________

class Dot:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

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
    def coors(self):
        return center[0] + self.__x, center[1] - self.__y

    @property
    def coorsNorm(self):
        return self.__x, self.__y

    def __add__(self, dot):
        return Dot(self.__x + dot.x, self.__y + dot.y)

    def __eq__(self, dot):
        return self.__x == dot.x and self.__y == dot.y

    def __sub__(self, dot):
        return Dot(self.__x - dot.x, self.__y - dot.y)

    def __truediv__(self, num: int):
        return Dot(self.__x / num, self.__y / num)

    def __mul__(self, num: Union[int, 'Dot', float]):
        if isinstance(num, int) or isinstance(num, float):
            return Dot(self.__x * num, self.__y * num)
        else:
            return Dot(self.__x * num.x, self.__y * num.y)


# Основные функции __________________________________________________________________

SIGNS = {'>=': lambda elem: elem[0] >= elem[1], '<=': lambda elem: elem[0] <= elem[1]}


def orientationAllDots(a, b, arr, sign):
    for elem in arr:
        if not SIGNS[sign]([orientation(a, b, elem), 0]):
            return False
    return True


def orientation(a, b, c):
    res = (b.y - a.y) * (c.x - b.x) - (c.y - b.y) * (b.x - a.x)
    if res == 0:
        return 0
    if res > 0:
        return 1
    return -1


def sortByHour(dots):
    centre = Dot(0, 0)

    def comparatorDots(dot1, dot2):
        angle1 = (math.atan2(*(dot1 - centre).coorsNorm)) * 180 / 3.14
        angle2 = (math.atan2(*(dot2 - centre).coorsNorm)) * 180 / 3.14
        return (angle1 > angle2) - (angle1 < angle2)

    for dot in dots:
        centre += dot
    centre /= len(dots)
    newDots = sorted(dots, key=cmp_to_key(comparatorDots))
    return newDots


def convex_hull(dots):
    centre = Dot(0, 0)

    def comparatorDots(dot1, dot2):
        angle1 = (math.atan2(*(dot1 - centre).coorsNorm)) * 180 / 3.14
        angle2 = (math.atan2(*(dot2 - centre).coorsNorm)) * 180 / 3.14
        return (angle1 > angle2) - (angle1 < angle2)

    borderDots = []
    for i in range(len(dots)):
        for j in range(i + 1, len(dots)):
            start, end = dots[i], dots[j]
            a, b, c = start.y - end.y, end.x - start.x, start.x * end.y - start.y * end.x
            pos, neg = 0, 0
            for k in range(len(dots)):
                if (k == i) or (k == j) or (a * dots[k].x + b * dots[k].y + c <= 0):
                    neg += 1
                if (k == i) or (k == j) or (a * dots[k].x + b * dots[k].y + c >= 0):
                    pos += 1
            if pos == len(dots) or neg == len(dots):
                if dots[i] not in borderDots:
                    centre += dots[i]
                    borderDots.append(dots[i])
                if dots[j] not in borderDots:
                    centre += dots[j]
                    borderDots.append(dots[j])

    centre /= len(borderDots)
    borderDots = sorted(borderDots, key=cmp_to_key(comparatorDots))
    return borderDots


def checkAngle(a, b):
    vectorComp = a.x * b.y - a.y * b.x
    return vectorComp >= 0


def isLine(arr):
    setX = set()
    setY = set()
    for elem in arr:
        setX.add(elem.x)
        setY.add(elem.y)
    return len(setY) == 1 or len(setX) == 1


def drawing(idx):
    global Lines
    global interLines
    if idx == len(interLines):
        return
    if idx >= 1 and interLines[idx - 1][2] == 'blue':
        canvas.delete(Lines[idx - 1])
    Lines.append(
        canvas.create_line(interLines[idx][0].coors, interLines[idx][1].coors, fill=interLines[idx][2], width=4))

    frame.after(500, lambda: drawing(idx + 1))


def comparatorDots(dot1, dot2):
    if dot1.x - dot2.x > 0:
        return 1
    elif dot1.x - dot2.x < 0:
        return -1
    else:
        if dot1.y - dot2.y > 0:
            return -1
        elif dot1.y - dot2.y < 0:
            return 1
    return 0


def point_in_hull(p1, p2, p3, p0):
    hull = convex_hull([p0, p1, p2, p3])
    return len(hull) != 3 or p0 in hull


def triangulate_between(leftFigure, rightFigure, upRibIdx, downRibIdx):
    global interLines
    idxLeft, idxRight = upRibIdx
    isFirstIter = False
    interLines.append([rightFigure[idxRight], leftFigure[idxLeft], 'purple'])

    while idxLeft != downRibIdx[0] or idxRight != downRibIdx[1]:
        idxLeftNext = (idxLeft + 1) % len(leftFigure)
        idxRightNext = (idxRight - 1) % len(rightFigure)

        if isFirstIter:
            if idxLeft == downRibIdx[0]:
                interLines.append([rightFigure[idxRightNext], leftFigure[idxLeft], 'purple'])
                idxRight = idxRightNext
                continue
            elif idxRight == downRibIdx[1]:
                interLines.append([leftFigure[idxLeftNext], rightFigure[idxRight], 'purple'])
                idxLeft = idxLeftNext
                continue

        angle = (leftFigure[idxLeft] - rightFigure[idxRight], rightFigure[idxRightNext] - rightFigure[idxRight])
        if checkAngle(*angle) and point_in_hull(rightFigure[idxRightNext], leftFigure[idxLeft], rightFigure[idxRight], leftFigure[idxLeftNext]):
            interLines.append([rightFigure[idxRightNext], leftFigure[idxLeft], 'purple'])
            idxRight = idxRightNext
        else:
            interLines.append([rightFigure[idxRight], leftFigure[idxLeftNext], 'purple'])
            idxLeft = idxLeftNext
        isFirstIter = True


def mergerHull(leftFigure, rightFigure):
    global interLines
    idxLeft, idxRight = 0, 0
    for i in range(len(leftFigure)):
        if leftFigure[i].x > leftFigure[idxLeft].x:
            idxLeft = i
    for i in range(len(rightFigure)):
        if rightFigure[i].x < rightFigure[idxRight].x:
            idxRight = i
    lenLeft, lenRight = len(leftFigure), len(rightFigure)
    upperLeft, upperRight = idxLeft, idxRight
    done = False
    interLines.append([leftFigure[upperLeft], rightFigure[upperRight], 'blue'])
    while not done:
        done = True
        while not orientationAllDots(rightFigure[upperRight], leftFigure[upperLeft], leftFigure, '<='):
            upperLeft = (upperLeft - 1) % lenLeft
            interLines.append([leftFigure[upperLeft], rightFigure[upperRight], 'blue'])
        while not orientationAllDots(leftFigure[upperLeft], rightFigure[upperRight], rightFigure, '>='):
            upperRight = (upperRight + 1) % lenRight
            interLines.append([leftFigure[upperLeft], rightFigure[upperRight], 'blue'])
            done = False
    downLeft, downRight = idxLeft, idxRight
    interLines.append([leftFigure[upperLeft], rightFigure[upperRight], 'purple'])
    done = False
    while not done:
        done = True
        while not orientationAllDots(rightFigure[downRight], leftFigure[downLeft], leftFigure, '>='):
            downLeft = (downLeft + 1) % lenLeft
            interLines.append([leftFigure[downLeft], rightFigure[downRight], 'blue'])
        while not orientationAllDots(leftFigure[downLeft], rightFigure[downRight], rightFigure, '<='):
            downRight = (downRight - 1) % lenRight
            interLines.append([leftFigure[downLeft], rightFigure[downRight], 'blue'])
            done = False
    newFigure = []
    i = upperRight
    while i % len(rightFigure) != downRight:
        newFigure.append(rightFigure[i % len(rightFigure)])
        i += 1
    else:
        if upperRight % len(rightFigure) == downRight:
            newFigure.append(rightFigure[i % len(rightFigure)])
            i += 1
            while i % len(rightFigure) != downRight and orientation(leftFigure[upperLeft], rightFigure[upperRight], rightFigure[i % len(rightFigure)]) == 0:
                newFigure.append(rightFigure[i % len(rightFigure)])
                i += 1
        else:
            newFigure.append(rightFigure[downRight])
    i = downLeft
    while i % len(leftFigure) != upperLeft:
        newFigure.append(leftFigure[i % len(leftFigure)])
        i += 1
    else:
        if downLeft % len(leftFigure) == upperLeft:
            newFigure.append(leftFigure[i % len(leftFigure)])
            i += 1
            while i % len(leftFigure) != upperLeft and orientation(rightFigure[downRight], leftFigure[downLeft], leftFigure[i % len(leftFigure)]) == 0:
                newFigure.append(leftFigure[i % len(leftFigure)])
                i += 1
        else:
            newFigure.append(leftFigure[upperLeft])
    interLines.append([leftFigure[downLeft], rightFigure[downRight], 'purple'])
    triangulate_between(leftFigure, rightFigure, (upperLeft, upperRight), (downLeft, downRight))
    newFigure = sortByHour(newFigure)
    if isLine(newFigure):
        newFigure = sorted(newFigure, key=cmp_to_key(comparatorDots))
        return [newFigure[0], newFigure[-1]]
    return sortByHour(newFigure)


def draw_triangle(dots):
    for i in range(len(dots)):
        interLines.append([dots[i], dots[(i + 1) % len(dots)], 'purple'])


def divide(dots):
    if len(dots) == 3:
        draw_triangle(dots)
        return convex_hull(dots)
    elif len(dots) == 4:
        convexHull = convex_hull(dots)
        if len(convexHull) == 3:
            centerDot = [dot for dot in dots if dot not in convexHull][0]
            for i in range(len(convexHull)):
                draw_triangle([centerDot, convexHull[i % len(convexHull)], convexHull[(i + 1) % len(convexHull)]])
        else:
            if not point_in_hull(*dots):
                draw_triangle([convexHull[0], convexHull[1], convexHull[2]])
                draw_triangle([convexHull[2], convexHull[3], convexHull[0]])
            else:
                draw_triangle([convexHull[0], convexHull[1], convexHull[3]])
                draw_triangle([convexHull[1], convexHull[3], convexHull[2]])
        return convex_hull(dots)
    elif len(dots) == 5:
        dots.append(dots[-1])
        start = len(dots) // 2
        left, right = dots[:start], dots[start:]
        left_hull, right_hull = divide(left), divide(right)
        newFigure = mergerHull(left_hull, right_hull)
        return newFigure
    elif len(dots) == 8:
        start = len(dots) // 2
        left, right = dots[:start], dots[start:]
        left_hull, right_hull = divide(left), divide(right)
        newFigure = mergerHull(left_hull, right_hull)
        return newFigure
    elif len(dots) < 12:
        left, right = dots[:3], dots[3:]
        left_hull, right_hull = divide(left), divide(right)
        newFigure = mergerHull(left_hull, right_hull)
        return newFigure
    else:
        start = len(dots) // 2
        left, right = dots[:start], dots[start:]
        left_hull, right_hull = divide(left), divide(right)
        newFigure = mergerHull(left_hull, right_hull)
        return newFigure


def algorithm():
    global Dots
    Dots = sorted(Dots, key=cmp_to_key(comparatorDots))
    divide(Dots)
    drawing(0)


def input_info():
    global Dots
    print("Введите количество точек:")
    n = int(input())

    print("Введите точки:")
    for i in range(n):
        x, y = map(int, input().split())
        Dots.append(Dot(x * 40, y * 40))


def draw_input():
    global Dots
    # Рисуем сетку
    for i in range(20):
        canvas.create_line(i * 40, 0, i * 40, 800)
        canvas.create_line(0, i * 40, 800, i * 40)
    for point in Dots:
        x1 = point.x
        y1 = point.y
        canvas.create_oval(400 + x1 - 3, 400 - y1 - 3,
                           400 + x1 + 3, 400 - y1 + 3, fill='purple')


frame = tk.Tk()
frame.title("Лабораторная 7")
frame.geometry("800x850")
frame.resizable(False, False)
frame.configure(bg='purple')
canvas = tk.Canvas(frame, bg="pink", width=width, height=height)
tk.Button(frame, text='''Погнали''', command=algorithm).place(x=100, y=height + 15)
canvas.place(x=0, y=0)

input_info()
draw_input()
frame.mainloop()
