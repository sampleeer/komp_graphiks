import tkinter as tk
import numpy as np
from scipy.spatial import Delaunay

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello JOPA.COM")
        self.root.geometry("1000x800")

        # Фреймы для размещения
        self.frame_main = tk.Frame(root)
        self.frame_main.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.frame_side = tk.Frame(root, width=200, bg='gray20')  # Темносерый цвет
        self.frame_side.pack(side=tk.RIGHT, fill=tk.Y)

        self.points = []

        self.canvas = tk.Canvas(self.frame_main, width=870, height=800, bg='lightblue')
        self.canvas.pack()

        self.btn_plot = tk.Button(self.frame_side, text="Старт", command=self.plot_triangulation)
        self.btn_plot.pack(pady=10)

        self.btn_clear = tk.Button(self.frame_side, text="Очистка", command=self.clear_canvas)
        self.btn_clear.pack(pady=10)

        self.canvas.bind("<Button-1>", self.add_point)

    def add_point(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))
        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill='white')

    def plot_triangulation(self):
        if len(self.points) < 3:
            print("минимум 3 для триангуляции ")
            return

        points_np = np.array(self.points)
        tri = Delaunay(points_np)

        self.canvas.delete("triangles")
        self.draw_triangles(tri, points_np, 0)

    def draw_triangles(self, tri, points_np, index):
        if index >= len(tri.simplices):
            return

        simplex = tri.simplices[index]
        p1, p2, p3 = points_np[simplex[0]], points_np[simplex[1]], points_np[simplex[2]]

        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill='white', tags="triangles")
        self.canvas.create_line(p2[0], p2[1], p3[0], p3[1], fill='white', tags="triangles")
        self.canvas.create_line(p3[0], p3[1], p1[0], p1[1], fill='white', tags="triangles")

        self.root.after(1500, self.draw_triangles, tri, points_np, index + 1)

        self.canvas.delete("points")
        for point in points_np:
            self.canvas.create_oval(point[0] - 3, point[1] - 3, point[0] + 3, point[1] + 3, fill='white', tags="points")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.points.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
