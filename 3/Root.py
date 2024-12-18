import tkinter as tk
from constants import WIDTH, HEIGHT, MIDDLE

CELL_SIZE = 20
SUM = 0


def drawGrid(canvas, fill: str = "grey"):
    for i in range(0, WIDTH, 20):
        canvas.create_line(i, 0, i, WIDTH, fill=fill)
    for i in range(0, HEIGHT, 20):
        canvas.create_line(0, i, HEIGHT, i, fill=fill)


def drawAxes(canvas):
    canvas.create_line(WIDTH // 2, WIDTH, WIDTH // 2, 0, width=2,
                       arrow=tk.LAST, fill="black")
    canvas.create_line(0, HEIGHT // 2, HEIGHT, HEIGHT // 2, width=2,
                       arrow=tk.LAST, fill="black")



def changeScaleX(root, star):
    label_above_button = tk.Label(root, text="Масштаб по OX")
    label_above_button.place(x=WIDTH + 70, y=HEIGHT // 5 + 65)

    SCALE_X_UP = tk.Button(root, text="Увеличить", command=star.scaleOX_UP)
    SCALE_X_UP.place(x=WIDTH + 130, y=HEIGHT // 5 + 85)

    SCALE_X_DOWN = tk.Button(root, text="Уменьшить", command=star.scaleOX_DOWN)
    SCALE_X_DOWN.place(x=WIDTH + 25, y=HEIGHT // 5 + 85)


def changeScaleY(root, star):
    label_above_button = tk.Label(root, text="Масштаб по OY")
    label_above_button.place(x=WIDTH + 70, y=HEIGHT // 5 + 115)

    SCALE_X_UP = tk.Button(root, text="Увеличить", command=star.scaleOY_UP)
    SCALE_X_UP.place(x=WIDTH + 130, y=HEIGHT // 5 + 135)

    SCALE_X_DOWN = tk.Button(root, text="Уменьшить", command=star.scaleOY_DOWN)
    SCALE_X_DOWN.place(x=WIDTH + 25, y=HEIGHT // 5 + 135)


def changeTurn(root, star):
    def turnStar():
        angle = int(entry.get())
        entry.delete(0, tk.END)
        star.turnStar(angle)

    label_above_button = tk.Label(root, text="Поворот относительно начала")
    label_above_button.place(x=WIDTH + 30, y=HEIGHT // 5 + 165)

    entry = tk.Entry(root, width=10)
    entry.place(x=WIDTH + 25, y=HEIGHT // 5 + 195)

    btn = tk.Button(root, text="Повернуть", command=turnStar)
    btn.place(x=WIDTH + 130, y=HEIGHT // 5 + 194)


def changeTurnToPoint(root, star):
    def turnStar():
        x = int(entryX.get())
        y = int(entryY.get())
        angle = int(entry.get())
        entry.delete(0, tk.END)
        entryX.delete(0, tk.END)
        entryY.delete(0, tk.END)
        star.turnStarToDot(angle, (x, y))

    label_above_button = tk.Label(root, text="Поворот относительно точки")
    label_above_button.place(x=WIDTH + 30, y=HEIGHT // 5 + 235)

    tk.Label(root, text="Координата x:").place(x=WIDTH + 30,
                                               y=HEIGHT // 5 + 265)

    entryX = tk.Entry(root, width=10)
    entryX.place(x=WIDTH + 25, y=HEIGHT // 5 + 295)

    tk.Label(root, text="Координата y:").place(x=WIDTH + 130, y=HEIGHT // 5 +
                                                                265)

    entryY = tk.Entry(root, width=10)
    entryY.place(x=WIDTH + 125, y=HEIGHT // 5 + 295)

    entry = tk.Entry(root, width=10)
    entry.place(x=WIDTH + 25, y=HEIGHT // 5 + 325)

    btn = tk.Button(root, text="Повернуть", command=turnStar)
    btn.place(x=WIDTH + 126, y=HEIGHT // 5 + 324)


def goToBegin(root, star):
    tk.Button(root, text="Вернуть в исходное положение",
              command=star.goToBegin).place(x=WIDTH + 5, y=HEIGHT // 5 + 354)


def lab2():
    root = tk.Tk()
    root.title("LAB3.COM")
    canvas = tk.Canvas(root, width=600, height=600, background='white')
    canvas.pack()
    drawGrid(canvas, '#C1C0B9')
    plane = Plane(canvas)
    p = Propeller(canvas, root)

    def goDown():
        global SUM
        p.shiftDown()
        plane.shiftDown()
        SUM += 100
        if SUM // 1000 % 2 == 0:
            root.after(100, goDown)
        else:
            root.after(100, goUp)

    def goUp():
        global SUM
        p.shiftUp()
        plane.shiftUp()
        SUM += 100
        if SUM // 1000 % 2 == 0:
            root.after(100, goDown)
        else:
            root.after(100, goUp)

    goDown()
    p.turnPropeller()
    root.mainloop()


def goToLab2(root):
    tk.Button(root, text="перейти ко второй части",
              command=lab2).place(x=WIDTH + 5, y=HEIGHT // 5 + 394)


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("2")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, background='white')
        drawGrid(self.canvas)
        drawAxes(self.canvas)
        self.star = Star(self.canvas)
        self.canvas.pack(side=tk.LEFT)
        self.down_button = tk.Button(self.root, text="↓", width=10,
                                     command=self.star.shiftDown)
        self.down_button.place(x=WIDTH + 60, y=HEIGHT // 10 - 10)
        self.up_button = tk.Button(self.root, text="↑", width=10,
                                   command=self.star.shiftUp)
        self.up_button.place(x=WIDTH + 60, y=HEIGHT // 10 - 40)
        self.left_button = tk.Button(self.root, text="←", width=1, height=3,
                                     command=self.star.shiftLeft)
        self.left_button.place(x=WIDTH + 10, y=HEIGHT // 10 - 38)

        right_button = tk.Button(self.root, text="→", width=1, height=3,
                                 command=self.star.shiftRight)
        right_button.place(x=WIDTH + 190, y=HEIGHT // 10 - 38)

        reflectOX = tk.Button(self.root, text="симметрия OY",
                              command=self.star.reflectOX)
        reflectOX.place(x=WIDTH + 60, y=HEIGHT // 5)

        reflectOY = tk.Button(self.root, text="симметрия OX",
                              command=self.star.reflectOY)
        reflectOY.place(x=WIDTH + 60, y=HEIGHT // 5 - 30)

        reflect = tk.Button(self.root, text="симметрия по прямой",
                            command=self.star.reflect)
        reflect.place(x=WIDTH + 40, y=HEIGHT // 5 + 30)

        changeScaleX(self.root, self.star)
        changeScaleY(self.root, self.star)

        changeTurn(self.root, self.star)
        changeTurnToPoint(self.root, self.star)

        goToBegin(self.root, self.star)

        goToLab2(self.root)
