import copy
import math
import time
from tkinter import *
from tkinter import filedialog  
from copy import deepcopy

SIZE = 25
Vertex = []
Pixels_field = []
All_Marks = []


def create_grid(size, width, height):
    x, y = 0, 0
    while x < width:
        x += size
        if x == width // 2:
            graph.create_line(x, 0, x, height, fill='black')
        else:
            graph.create_line(x, 0, x, height)
    while y < height:
        y += size
        if y == height // 2:
            graph.create_line(0, y, width, y, fill='black')
        else:
            graph.create_line(0, y, width, y)


def load_points_from_file():
    global Vertex
    file_path = 'points.txt'
    if file_path:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            Vertex.clear()  # Сначала очищаем текущие точки
            for line in lines:
                x, y = map(int, line.strip().split())
                Vertex.append([x, y])
                # Отрисовываем точки
                graph.create_oval(x * SIZE + 400 - 2, 400 - SIZE * y - 2,
                                  SIZE * x + 400 + 2, 400 - SIZE * y + 2,
                                  fill='blue', tags='mark_point')


def join_dots():
    global Vertex

    vertex = []
    graph.delete('mark_point')
    for i in range(len(Vertex)):
        vertex.append([SIZE * Vertex[i][0] + 400,
                        400 - SIZE * Vertex[i][1]])
    graph.create_polygon(vertex, fill='', outline='blue', tags='pol')


def set_point(event):
    x1 = event.x
    y1 = event.y

    x1 = round((x1-400)/SIZE)
    y1 = round((400-y1)/SIZE)
    Vertex.append([x1, y1])

    graph.create_oval(x1*SIZE + 400 - 2, 400 - SIZE*y1 + 2,
                      SIZE*x1 + 400 + 2, 400 - SIZE*y1 - 2, fill='blue', tags='mark_point')

def mark_border():
    global Vertex, Pixels_field, All_Marks

    # Determine the bounding box of the vertices
    x_max = max(Vertex, key=lambda x: x[0])[0]
    y_max = max(Vertex, key=lambda x: x[1])[1]
    x_min = min(Vertex, key=lambda x: x[0])[0]
    y_min = min(Vertex, key=lambda x: x[1])[1]

    Pixels_field = [[False] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]

    n = len(Vertex)

    for idx in range(n):
        x1, y1 = Vertex[idx]
        x2, y2 = Vertex[(idx + 1) % n]

        marked_points = bresenham_line(x1, y1, x2, y2)

        for point in marked_points:
            px, py = point
            All_Marks.append(point)
            Pixels_field[py - y_min][px - x_min] = True

            graph.create_oval(SIZE * px + 400 - 2, 400 - SIZE * py - 2,
                              SIZE * px + 400 + 2, 400 - SIZE * py + 2,
                              fill='black',
                              tags=['point', f'p{px - x_min}{py - y_min}'])

        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                All_Marks.append((x, y1))
                Pixels_field[y1 - y_min][x - x_min] = True

                graph.create_oval(SIZE * x + 400 - 2, 400 - SIZE * y1 - 2,
                                  SIZE * x + 400 + 2, 400 - SIZE * y1 + 2,
                                  fill='black',
                                  tags=['point', f'p{x - x_min}{y1 - y_min}'])


def bresenham_line(x0, y0, x1, y1):
    pixels = []
    slope = abs(y1 - y0) > abs(x1 - x0)
    if slope:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = abs(y1 - y0)
    error = dx / 2
    ystep = 1 if y0 < y1 else -1
    y = y0

    for x in range(x0, x1 + 1):
        coord = (y, x) if slope else (x, y)
        pixels.append(coord)
        error -= dy
        if error < 0:
            y += ystep
            error += dx

    return pixels


def is_inside_polygon(x, y, polygon):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def xor_algorythm():
    global Vertex, Pixels_field

    x_max = max(Vertex, key=lambda x: x[0])[0]
    y_max = max(Vertex, key=lambda x: x[1])[1]
    x_min = min(Vertex, key=lambda x: x[0])[0]
    y_min = min(Vertex, key=lambda x: x[1])[1]

    for i in range(len(Pixels_field)):
        for j in range(1, len(Pixels_field[0])):
            # проверка на то внутри ли полигона
            if is_inside_polygon(j + x_min, i + y_min, Vertex):
                graph.create_oval(SIZE * (j + x_min) + 400 - 2, 400 - SIZE * (i + y_min) - 2,
                                  SIZE * (j + x_min) + 400 + 2, 400 - SIZE * (i + y_min) + 2,
                                  fill='black', tags='point')
                graph.update()
                time.sleep(0.5)

    print('Done!')


def fill_border():
    global All_Marks
    for point in All_Marks:
        # Check if the pixel is inside the polygon
        if is_inside_polygon(point[0], point[1], Vertex):
            graph.create_oval(SIZE * point[0] + 400 - 2, 400 - SIZE * point[1] - 2,
                              SIZE * point[0] + 400 + 2, 400 - SIZE * point[1] + 2,
                              fill='black', tags='point')

def clear():
    Vertex.clear()
    Pixels_field.clear()
    All_Marks.clear()
    graph.delete('point', 'pol', 'mark_point')


root = Tk()
root.title("Hello JOPA.COM")
root.geometry("1000x800")
root.resizable(False, False)

# Добавляем кнопку для загрузки точек из файла
load_bt = Button(root, command=load_points_from_file, text='Загрузить точки из файла',
                 font=('Arial', 12), background='red')
load_bt.place(x=820, y=20, width=160)

join_bt = Button(root, command=join_dots, text='Завершить фигуру',
                 font=('Arial', 12), background='red')
join_bt.place(x=820, y=60, width=160)

start_bt = Button(root, command=mark_border, text='Разметить границу', font=(
    'Arial', 12), background='red')
start_bt.place(x=820, y=100, width=160)

xor_bt = Button(root, command=xor_algorythm, text='Запустить XOR ',
                font=('Arial', 12), background='red')
xor_bt.place(x=820, y=140, width=160)

end_bt = Button(root, command=fill_border, text='Заполнить границу',
                font=('Arial', 12), background='red')
end_bt.place(x=820, y=180, width=160)

clear_bt = Button(root, command=clear, text='Очистить',
                  font=('Arial', 12), background='red')
clear_bt.place(x=820, y=220, width=160)

graph = Canvas(root, width=800, height=800, background='lightblue')
graph.place(x=0, y=0)
graph.bind('<Button-1>', set_point)
create_grid(SIZE, 800, 800)

root.mainloop()
