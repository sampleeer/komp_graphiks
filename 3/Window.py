import tkinter as tk


from Root import drawGrid, drawAxes, CELL_SIZE
from dot import Dot
from Circle import Circle
from Line import Line
from constants import WIDTH, HEIGHT, MIDDLE
isLineDrown = False

def cleanEntry(entry: list):
    for elem in entry:
        elem.delete(0, tk.END)


def printDots(line):
    line.bresenhamAlgorithm()
    line.printDots()


def printDotsCircle(circle):
    circle.bresenhamAlgorithm()
    circle.printDots()


class WindowCircle:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("3.2")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, background='white')
        self.circle = Circle(self.canvas)
        drawGrid(self.canvas)
        drawAxes(self.canvas)
        self.canvas.pack(side=tk.LEFT)

        label_above_button = tk.Label(self.root, text="Координаты центра")
        label_above_button.place(x=WIDTH + 30, y=HEIGHT // 10 - 50)

        tk.Label(self.root, text="X, Y").place(x=WIDTH + 30,
                                                        y=HEIGHT // 10 - 25)

        entryX = tk.Entry(self.root, width=10)
        entryX.place(x=WIDTH + 60, y=HEIGHT // 10 - 25)

        entryY = tk.Entry(self.root, width=10)
        entryY.place(x=WIDTH + 150, y=HEIGHT // 10 - 25)

        label_above_button = tk.Label(self.root, text="Радиус окружности")
        label_above_button.place(x=WIDTH + 30, y=HEIGHT // 10 + 5)

        entryR = tk.Entry(self.root, width=10)
        entryR.place(x=WIDTH + 30, y=HEIGHT // 10 + 33)

        createLineButton = tk.Button(self.root, text='задать окружность',
                                     command=lambda: self.circle.createCircle(
                                         Dot(int(entryX.get()) * CELL_SIZE,
                                             int(entryY.get()) * CELL_SIZE),
                                         int(entryR.get()) * CELL_SIZE
                                     ))
        cleanEntry([entryX, entryY, entryR])
        createLineButton.place(x=WIDTH + 30, y=HEIGHT // 10 + 65)

        rastrButton = tk.Button(self.root, text="Растеризация",
                                command=lambda: printDots(self.circle))
        rastrButton.place(x=WIDTH + 30, y=HEIGHT // 10 + 97)


def openWindowCircle():
    win = WindowCircle()
    win.root.mainloop()


class WindowLine:
    def __init__(self):
        global isLineDrown
        self.root = tk.Tk()
        self.root.title("3.1")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, background='white')
        self.line = Line(self.canvas)
        drawGrid(self.canvas)
        drawAxes(self.canvas)
        # self.canvas.create_line((0, 0), (1, 1), fill='red', width=2)
        self.canvas.pack(side=tk.LEFT)

        tk.Label(self.root, text="X1, Y1").place(x=WIDTH + 30,
                                                        y=HEIGHT // 10 - 50)

        entryX = tk.Entry(self.root, width=10)
        entryX.place(x=WIDTH + 80, y=HEIGHT // 10 - 50)

        entryY = tk.Entry(self.root, width=10)
        entryY.place(x=WIDTH + 180, y=HEIGHT // 10 - 50)

        tk.Label(self.root, text="X2, Y2").place(x=WIDTH + 30,
                                                        y=HEIGHT // 10 - 10)

        entryX2 = tk.Entry(self.root, width=10)
        entryX2.place(x=WIDTH + 80, y=HEIGHT // 10 - 10)
        entryY2 = tk.Entry(self.root, width=10)
        entryY2.place(x=WIDTH + 180, y=HEIGHT // 10 - 10)
        createLineButton = tk.Button(self.root, text='задать прямую',
                                     command=lambda: self.line.createLine(
                                         Dot(int(entryX.get()) * CELL_SIZE,
                                             int(entryY.get()) * CELL_SIZE),
                                         Dot(int(entryX2.get()) * CELL_SIZE,
                                             int(entryY2.get()) * CELL_SIZE)
                                     ))
        cleanEntry([entryX, entryY2, entryX2, entryY])
        createLineButton.place(x=WIDTH + 30, y=HEIGHT // 10 + 20)

        reflectOX = tk.Button(self.root, text="симметрия OY",
                              command=self.line.reflectOX)
        reflectOX.place(x=WIDTH + 30, y=HEIGHT // 10 + 50)

        reflectOY = tk.Button(self.root, text="симметрия OX",
                              command=self.line.reflectOY)
        reflectOY.place(x=WIDTH + 30, y=HEIGHT // 10 + 80)

        reflect = tk.Button(self.root, text="симметрия по прямой",
                            command=self.line.reflect)
        reflect.place(x=WIDTH + 30, y=HEIGHT // 10 + 110)

        offsetButton = tk.Button(self.root, text="смещение к началу",
                                 command=self.line.offsetLineToDot)
        offsetButton.place(x=WIDTH + 30, y=HEIGHT // 10 + 140)

        rastrButton = tk.Button(self.root, text="Растеризация",
                                command=lambda: printDots(self.line))
        rastrButton.place(x=WIDTH + 30, y=HEIGHT // 10 + 170)

        startPos = tk.Button(self.root, text="Вернуть начальное положение",
                             command=self.line.goStartPos)
        startPos.place(x=WIDTH + 30, y=HEIGHT // 10 + 200)

        startPos = tk.Button(self.root, text="Открыть растеризацию окружности",
                             command=openWindowCircle)
        startPos.place(x=WIDTH + 30, y=HEIGHT // 10 + 230)
