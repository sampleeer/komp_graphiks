import tkinter as tk

class WalkingStickFigure:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.draw_figure()

    def draw_figure(self):
        # Рисуем голову
        self.head = self.canvas.create_oval(self.x - 10, self.y - 30, self.x + 10, self.y - 10, fill='black')

        # Рисуем тело
        self.body = self.canvas.create_line(self.x, self.y - 10, self.x, self.y + 20, fill='black', width=2)

        # Рисуем левую ногу
        self.left_leg = self.canvas.create_line(self.x, self.y + 20, self.x - 10, self.y + 40, fill='black', width=2)

        # Рисуем правую ногу
        self.right_leg = self.canvas.create_line(self.x, self.y + 20, self.x + 10, self.y + 40, fill='black', width=2)

    def walk(self):
        # Симулируем шаг, перемещая ноги
        self.canvas.move(self.left_leg, 0, 20)
        self.canvas.move(self.right_leg, 0, -20)
        self.canvas.after(500, self.reverse_walk)  # Ждем 500 миллисекунд и вызываем reverse_walk

    def reverse_walk(self):
        # Обратное движение ног
        self.canvas.move(self.left_leg, 0, -20)
        self.canvas.move(self.right_leg, 0, 20)
        self.canvas.after(500, self.walk)  # Ждем 500 миллисекунд и вызываем walk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Walking Stick Figure")

        screen_width = 800
        screen_height = 800
        self.root.geometry(f"{screen_width}x{screen_height}")

        self.canvas = tk.Canvas(self.root, width=screen_width, height=screen_height, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Располагаем человечка в центре
        x_center = screen_width // 2
        y_center = screen_height // 2
        self.stick_figure = WalkingStickFigure(self.canvas, x_center, y_center)

        # Запускаем анимацию ходьбы
        self.stick_figure.walk()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
