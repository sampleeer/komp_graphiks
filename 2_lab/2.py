import tkinter as tk
import math

class TransformationsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transformations App")

        self.screen_width = 600
        self.screen_height = 600
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")

        self.canvas = tk.Canvas(self.root, width=self.screen_width, height=self.screen_height, bg='white')
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.square_size = 50
        self.square_coords = [
            [-self.square_size / 2, -self.square_size / 2, 1],
            [self.square_size / 2, -self.square_size / 2, 1],
            [self.square_size / 2, self.square_size / 2, 1],
            [-self.square_size / 2, self.square_size / 2, 1]
        ]

        self.draw_square()

        # Buttons for transformations
        self.translation_button = tk.Button(self.root, text="Перенос по OX", command=self.translate_along_x)
        self.translation_button.pack(side=tk.TOP, padx=10, pady=5)

        self.reflection_button = tk.Button(self.root, text="Отражение относительно OX", command=self.reflect_about_x)
        self.reflection_button.pack(side=tk.TOP, padx=10, pady=5)

        self.scaling_button = tk.Button(self.root, text="Масштабирование", command=self.scale)
        self.scaling_button.pack(side=tk.TOP, padx=10, pady=5)

        self.rotation_button = tk.Button(self.root, text="Поворот относительно центра", command=self.rotate_about_center)
        self.rotation_button.pack(side=tk.TOP, padx=10, pady=5)

    def draw_square(self):
        self.canvas.delete("square")
        scaled_coords = self.scale_coordinates(self.square_coords)
        flat_coords = [coord for sublist in scaled_coords for coord in sublist[:2]]
        self.canvas.create_polygon(flat_coords, fill='lightblue', outline='black', tags="square")

    def scale_coordinates(self, coordinates):
        return [(coord[0] + self.screen_width / 2, coord[1] + self.screen_height / 2) for coord in coordinates]

    def apply_transformation(self, transformation_matrix):
        self.square_coords = [list(np.dot(np.array(coord), transformation_matrix.T)) for coord in self.square_coords]
        self.draw_square()

    def translate_along_x(self):
        translation_matrix = np.array([
            [1, 0, 50],
            [0, 1, 0],
            [0, 0, 1]
        ])
        self.apply_transformation(translation_matrix)

    def reflect_about_x(self):
        reflection_matrix = np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
        self.apply_transformation(reflection_matrix)

    def scale(self):
        scale_matrix = np.array([
            [1.5, 0, 0],
            [0, 1.5, 0],
            [0, 0, 1]
        ])
        self.apply_transformation(scale_matrix)

    def rotate_about_center(self):
        rotation_matrix = np.array([
            [np.cos(np.radians(30)), -np.sin(np.radians(30)), 0],
            [np.sin(np.radians(30)), np.cos(np.radians(30)), 0],
            [0, 0, 1]
        ])
        self.apply_transformation(rotation_matrix)

if __name__ == "__main__":
    root = tk.Tk()
    app = TransformationsApp(root)
    root.mainloop()
