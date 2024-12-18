import tkinter as tk
from Figure import *

from tkinter import PhotoImage
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import PhotoImage
from Figure import *


def function():
    canvas.delete('all')
    # Повторное отображение изображения фона
    canvas.create_image(0, 0, anchor=tk.NW, image=canvas.bg_image)


def Draw():
    head_color = 'white'
    body_color = 'darkblue'
    arm_color = 'blue'
    leg_color = 'red'
    eye_color = 'black'
    mouth_color = 'red'

    width_a, width_l = 5, 5
    function()

    # Координаты для квадрата
    x1, y1 = head.points[0].get_x(False), head.points[0].get_y(False)
    x2, y2 = head.points[1].get_x(False), head.points[1].get_y(False)

    # Рисуем квадрат для головы
    canvas.create_rectangle(x1, y1, x2, y2, fill=head_color)
    canvas.create_polygon((x1 + (x2 - x1) / 2, y1), (x1, y2), (x2, y2), fill=head_color)
    canvas.create_rectangle(body.points[0].get_x(False), body.points[0].get_y(False), body.points[1].get_x(False),
                            body.points[1].get_y(False), fill=body_color)
    canvas.create_line(left_arm.points[0].get_x(False), left_arm.points[0].get_y(False),
                       left_arm.points[1].get_x(False), left_arm.points[1].get_y(False), fill=arm_color, width=width_a)
    canvas.create_line(right_arm.points[0].get_x(False), right_arm.points[0].get_y(False),
                       right_arm.points[1].get_x(False), right_arm.points[1].get_y(False), fill=arm_color,
                       width=width_a)
    canvas.create_line(left_leg.points[0].get_x(False), left_leg.points[0].get_y(False),
                       left_leg.points[1].get_x(False), left_leg.points[1].get_y(False), fill=leg_color, width=width_l)
    canvas.create_line(right_leg.points[0].get_x(False), right_leg.points[0].get_y(False),
                       right_leg.points[1].get_x(False), right_leg.points[1].get_y(False), fill=leg_color,
                       width=width_l)
    canvas.create_oval(eye.points[0].get_x(False), eye.points[0].get_y(False), eye.points[1].get_x(False),
                       eye.points[1].get_y(False), fill=eye_color)
    mouth_center_x = (mouth.points[0].get_x(False) + mouth.points[1].get_x(False)) / 2
    mouth_center_y = mouth.points[0].get_y(False) + 10
    canvas.create_arc(mouth.points[0].get_x(False), mouth.points[0].get_y(False),
                      mouth.points[1].get_x(False), mouth.points[1].get_y(False),
                      start=0, extent=-180, style=tk.ARC, outline=mouth_color, width=2)


def animate():
    global x_speed, flag, direction

    if flag == 0:
        flag = 1
    else:
        flag = 0

    head.x_axis_shift(x_speed)
    body.x_axis_shift(x_speed)
    left_arm.x_axis_shift(x_speed)
    right_arm.x_axis_shift(x_speed)
    left_leg.x_axis_shift(x_speed)
    right_leg.x_axis_shift(x_speed)
    eye.x_axis_shift(x_speed)
    mouth.x_axis_shift(x_speed)

    alfa_left_arm = 90
    x_shift_rigth_arm = 20
    alfa_right_arm = 90
    alfa_right_leg = 55
    x_shift_left_leg = 8
    alfa_left_leg = 70

    left_arm.turn((-1) ** flag * alfa_left_arm, left_arm.points[0])
    right_arm.x_axis_shift((-1) ** flag * x_shift_rigth_arm)
    right_arm.turn((-1) ** (flag - 1) * alfa_right_arm, right_arm.points[0])
    right_leg.turn((-1) ** (flag - 1) * alfa_right_leg, right_leg.points[0])
    left_leg.x_axis_shift((-1) ** (flag - 1) * x_shift_left_leg)
    left_leg.turn((-1) ** flag * alfa_left_leg, left_leg.points[0])

    if max(left_arm.points[1].get_x(False),
           right_arm.points[1].get_x(False),
           left_leg.points[1].get_x(False),
           right_leg.points[1].get_x(False)) > 550 or min(left_arm.points[1].get_x(False),
                                                          right_arm.points[1].get_x(False),
                                                          left_leg.points[1].get_x(False),
                                                          right_leg.points[1].get_x(False)) < 50:
        x_speed *= -1
        if direction == 0:
            direction = 1
        else:
            direction = 0
        eye.x_axis_shift((-1) ** (direction - 1) * 20)
        mouth.x_axis_shift((-1) ** (direction - 1) * 20)

    Draw()
    root.after(500, animate)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Walking Man')
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=600, height=600)
    canvas.pack()

    bg_image = PhotoImage(file="/Users/pavelnehaenko/Downloads/field.png")
    canvas.bg_image = bg_image

    canvas.create_image(0, 0, anchor=tk.NW, image=canvas.bg_image)

    x, y = 200, 500

    head = Figure(Point(x + 75, y - 250), Point(x + 125, y - 200))
    body = Figure(Point(x + 90, y - 200), Point(x + 110, y - 100))
    left_arm = Figure(Point(x + 100, y - 175), Point(x + 60, y - 140))
    right_arm = Figure(Point(x + 110, y - 175), Point(x + 140, y - 150))
    left_leg = Figure(Point(x + 95, y - 100), Point(x + 60, y - 50))
    right_leg = Figure(Point(x + 100, y - 120), Point(x + 140, y - 50))
    eye = Figure(Point(x + 118, y - 225), Point(x + 108, y - 235))
    mouth = Figure(Point(x + 100, y - 215), Point(x + 125, y - 215))

    x_speed = 30
    flag = 0
    direction = 1

    animate()
    root.mainloop()

    #bg_image = PhotoImage(file="/Users/pavelnehaenko/Downloads/field.png")
