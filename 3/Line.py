from Root import CELL_SIZE
from dot import Dot


RAD = 5
ACTIONS = []

MATRIX_OX = [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]
MATRIX_OY = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
MATRIX_XY = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]

class Line:
    def __init__(self, canvas):
        self.canvasLine = None
        self.canvasDots = []
        self.__dotSt = None
        self.__dotFn = None
        self.__canvas = canvas
        self.__rastDots = []

    def createLine(self, dotStart: Dot, dotFinish: Dot):
        self.__dotSt = dotStart
        self.__dotFn = dotFinish
        if self.canvasLine is None:
            self.canvasLine = self.__canvas.create_line(self.__dotSt.coors,
                                                        self.__dotFn.coors,
                                                        fill='blue', width=2)
        else:
            self.__changeLines()
            if self.__rastDots:
                for elem in self.canvasDots:
                    self.__canvas.delete(elem)
                self.__rastDots.clear()
                self.canvasDots.clear()
                self.bresenhamAlgorithm()
                self.printDots()

    def __changeLines(self):
        self.__canvas.coords(self.canvasLine,
                             *self.__dotSt.coors,
                             *self.__dotFn.coors)

    def __changeDots(self):
        for canvDot, dot in zip(self.canvasDots, self.__rastDots):
            self.__canvas.coords(canvDot, dot.coors[0] - RAD,
                                 dot.coors[1] - RAD, dot.coors[0] + RAD,
                                 dot.coors[1] + RAD)

    def __changeCoors(self, mat):
        self.__dotSt.multMat(mat)
        self.__dotFn.multMat(mat)
        for dot in self.__rastDots:
            dot.multMat(mat)
        self.__changeLines()
        self.__changeDots()

    def offsetLineToDot(self, dot: tuple = (0, 0)):
        if len(self.__rastDots) == 0:
            ACTIONS.append([4, (self.__dotSt.x, self.__dotSt.y)])  # Используем координаты x и y
        diffX = dot[0] - self.__dotSt.x
        diffY = dot[1] - self.__dotSt.y
        self.__dotSt.x += diffX
        self.__dotSt.y += diffY
        self.__dotFn.x += diffX
        self.__dotFn.y += diffY
        for dotRast in self.__rastDots:
            dotRast.x += diffX
            dotRast.y += diffY
        self.__changeLines()
        self.__changeDots()

    def reflectOX(self):
        if len(self.__rastDots) == 0:
            ACTIONS.append([1])
        self.__changeCoors(MATRIX_OX)

    def reflectOY(self):
        if len(self.__rastDots) == 0:
            ACTIONS.append([2])
        self.__changeCoors(MATRIX_OY)

    def reflect(self):
        if len(self.__rastDots) == 0:
            ACTIONS.append([3])
        self.__changeCoors(MATRIX_XY)

    def bresenhamAlgorithm(self):
        dx = self.__dotFn.coors_norm[0] // CELL_SIZE
        dy = self.__dotFn.coors_norm[1] // CELL_SIZE
        y = 0
        error = dx / 2
        for x in range(0, self.__dotFn.coors_norm[0] // CELL_SIZE + 1):
            self.__rastDots.append(Dot(x * CELL_SIZE, y * CELL_SIZE))
            error -= dy
            if error < 0:
                y += 1
                error += dx

    def printDots(self):
        for dot in self.__rastDots:
            self.canvasDots.append(self.__canvas.create_oval(dot.coors[0] - RAD,
                                                             dot.coors[1] - RAD,
                                                             dot.coors[0] + RAD,
                                                             dot.coors[1] + RAD,
                                                             fill='black'))

    def goStartPos(self):
        for num in ACTIONS:
            if num[0] == 1:
                self.reflectOX()
            elif num[0] == 2:
                self.reflectOY()
            elif num[0] == 3:
                self.reflect()
            elif num[0] == 4:
                self.offsetLineToDot(num[1])
