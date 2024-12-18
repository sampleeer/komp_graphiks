from Line import MATRIX_OY, MATRIX_OX
from Root import CELL_SIZE
from dot import Dot
from Line import RAD


def addDots(arr, x, y, center):
    dotSt = Dot(x*20, y*20)
    arr.append(Dot(dotSt.coors_norm[0] + center[0],
                   dotSt.coors_norm[1] + center[1]))
    dotSt.multMat(MATRIX_OY)
    arr.append(Dot(dotSt.coors_norm[0] + center[0],
                   dotSt.coors_norm[1] + center[1]))
    dotSt.multMat(MATRIX_OX)
    arr.append(Dot(dotSt.coors_norm[0] + center[0],
                   dotSt.coors_norm[1] + center[1]))
    dotSt.multMat(MATRIX_OY)
    arr.append(Dot(dotSt.coors_norm[0] + center[0],
                   dotSt.coors_norm[1] + center[1]))


class Circle:
    def __init__(self, canvas):
        self.center = Dot(0, 0)
        self.radius = 0
        self.canvas = canvas
        self.canvasOval = None
        self.__rastDots = []
        self.canvasDots = []

    def __changeLines(self):
        self.canvas.coords(self.canvasOval,
                           self.center.coors[0] - self.radius,
                           self.center.coors[1] - self.radius,
                           self.center.coors[0] + self.radius,
                           self.center.coors[1] + self.radius)

    def createCircle(self, center: Dot, radius):
        self.center = center
        self.radius = radius
        if self.canvasOval is None:
            self.canvasOval = self.canvas.create_oval(
                self.center.coors[0] - self.radius,
                self.center.coors[1] - self.radius,
                self.center.coors[0] + self.radius,
                self.center.coors[1] + self.radius, outline='black', width=2)
        else:
            self.__changeLines()
            if self.__rastDots:
                for elem in self.canvasDots:
                    self.canvas.delete(elem)
                self.__rastDots.clear()
                self.canvasDots.clear()
                self.bresenhamAlgorithm()
                self.printDots()

    def printDots(self):
        if not self.canvasDots:
            for dot in self.__rastDots:
                self.canvasDots.append(self.canvas.create_oval(dot.coors[0] - RAD,
                                                               dot.coors[1] - RAD,
                                                               dot.coors[0] + RAD,
                                                               dot.coors[1] + RAD,
                                                               fill='black', outline='black'))

    def bresenhamAlgorithm(self):
        x, y = self.radius // CELL_SIZE, 0
        delta = 2 * (1 - self.radius // CELL_SIZE)
        while x >= 0:
            addDots(self.__rastDots, x, y, self.center.coors_norm)
            deltaX = 2 * delta + 2 * x - 1
            deltaY = 2 * delta - 2 * y - 1
            if delta < 0 and deltaX <= 0:
                y += 1
                delta += 2 * y + 1
            elif delta > 0 and deltaY >= 0:
                x -= 1
                delta -= 2 * x - 1
            else:
                x -= 1
                y += 1
                delta += 2 * y - 2 * x + 2
