import tkinter as tk
import math

class Subfigure:
    def __init__(self, canvas, vertices, color='lightgray'):
        self.canvas = canvas
        self.vertices = vertices
        self.subfigure_id = None
        self.color = color
        self.draw_subfigure()

    def draw_subfigure(self):
        if self.subfigure_id:
            self.canvas.delete(self.subfigure_id)
        self.subfigure_id = self.canvas.create_polygon(self.vertices, outline='black', fill=self.color, width=3)


    def rotate(self, angle):
        angle_rad = math.radians(angle)
        center = self.calculate_center()
        for i in range(len(self.vertices)):
            x = self.vertices[i][0] - center[0]
            y = self.vertices[i][1] - center[1]
            self.vertices[i] = (x * math.cos(angle_rad) - y * math.sin(angle_rad) + center[0],
                                x * math.sin(angle_rad) + y * math.cos(angle_rad) + center[1])
        self.draw_subfigure()

    def calculate_center(self):
        x_sum = sum(point[0] for point in self.vertices)
        y_sum = sum(point[1] for point in self.vertices)
        center_x = x_sum / len(self.vertices)
        center_y = y_sum / len(self.vertices)
        return center_x, center_y

class CompoundFigure:
    def __init__(self, canvas):
        self.canvas = canvas
        self.subfigures = []

    def add_subfigure(self, subfigure):
        self.subfigures.append(subfigure)

    def rotate_all(self, angle):
        for subfigure in self.subfigures:
            subfigure.rotate(angle)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Compound Figure Rotation Example")

        # Получить размеры экрана
        screen_width = 1000
        screen_height = 800

        # Установить размеры окна
        self.root.geometry(f"{screen_width}x{screen_height}")

        # Создать холст
        self.canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg='white')
        self.canvas.pack(expand=True, fill=tk.BOTH)

        self.compound_figure = CompoundFigure(self.canvas)
        x_val = 400
        y_val = 300
        
        square_kvadrat = Subfigure(self.canvas, [(x_val + 50, y_val + 100), (x_val + 150, y_val + 100), (x_val + 150, y_val + 200), (x_val + 50, y_val + 200)], color='')
        square_krisha = Subfigure(self.canvas, [(x_val + 50, y_val + 100), (x_val + 100, y_val + 50), (x_val + 150, y_val + 100)], color='')
        square_seredina = Subfigure(self.canvas, [(x_val + 50, y_val + 150), (x_val + 150, y_val + 150)], color='')
        square_vvpalka = Subfigure(self.canvas, [(x_val + 50, y_val + 150), (x_val + 150, y_val + 100)], color='')
        square_nnpalka = Subfigure(self.canvas, [(x_val + 50, y_val + 150), (x_val + 150, y_val + 200)], color='')


        self.compound_figure.add_subfigure(square_kvadrat)
        self.compound_figure.add_subfigure(square_krisha)
        self.compound_figure.add_subfigure(square_seredina)
        self.compound_figure.add_subfigure(square_vvpalka)
        self.compound_figure.add_subfigure(square_nnpalka)

        self.rotate_button = tk.Button(root, text="Rotate All", command=self.rotate_all_subfigures)
        self.rotate_button.pack(pady=10)

    def rotate_all_subfigures(self):
        angle = 30
        self.compound_figure.rotate_all(angle)
# пук пук пук ger
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
