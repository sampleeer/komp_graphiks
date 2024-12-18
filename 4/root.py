import tkinter as tk
from param import height, width

def draw_grid(canvas):
	for i in range(0, width, 20):
		canvas.create_line(i, 0, i, width)
	for i in range(0, height, 20):
		canvas.create_line(0, i, height, i)

def draw_axes(canvas):
	canvas.create_line(width // 2, 0, width // 2, width, width=2, arrow=tk.FIRST)
	canvas.create_line(height, height // 2, 0, height // 2, width=2, arrow=tk.FIRST)

class Window:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('LABA2')
		self.canvas = tk.Canvas(self.root, width=width, height=height)
		draw_grid(self.canvas)
		draw_axes(self.canvas)
		self.star = Star(self.canvas)
		self.canvas.pack(side=tk.LEFT)
		down_button = tk.Button(self.root, text="↓", width=10,
									 command=self.star.shift_down)
		down_button.place(x=width + 60, y=height // 10 - 10)
		up_button = tk.Button(self.root, text="↑", width=10,
								   command=self.star.shift_up)
		up_button.place(x=width + 60, y=height // 10 - 40)
		left_button = tk.Button(self.root, text="←", width=1, height=3,
									 command=self.star.shift_left)
		left_button.place(x=width + 10, y=height // 10 - 38)

		right_button = tk.Button(self.root, text="→", width=1, height=3,
								 command=self.star.shift_right)
		right_button.place(x=width + 190, y=height // 10 - 38)

		reflectOX = tk.Button(self.root, text="симметрия OY",
							  command=self.star.reflect_x)
		reflectOX.place(x=width + 60, y=height // 5)

		reflectOY = tk.Button(self.root, text="симметрия OX",
							  command=self.star.reflect_y)
		reflectOY.place(x=width + 60, y=height // 5 - 30)

		reflect = tk.Button(self.root, text="симметрия по прямой",
							command=self.star.reflect_yx)
		reflect.place(x=width + 40, y=height // 5 + 30)

		SCALE_X_UP = tk.Button(self.root, text="Увеличить по x",
							   command=self.star.scalex_up)
		SCALE_X_UP.place(x=width + 130, y=height // 5 + 85)

		SCALE_X_DOWN = tk.Button(self.root, text="Уменьшить по x",
								 command=self.star.scalex_down)
		SCALE_X_DOWN.place(x=width + 25, y=height // 5 + 85)

		SCALE_Y_UP = tk.Button(self.root, text="Увеличить по y",
							   command=self.star.scaley_up)
		SCALE_Y_UP.place(x=width + 130, y=height // 5 + 135)

		SCALE_Y_DOWN = tk.Button(self.root, text="Уменьшить по y",
								 command=self.star.scaley_down)
		SCALE_Y_DOWN.place(x=width + 25, y=height // 5 + 135)

		GO_BEGIN = tk.Button(self.root, text='вернуться в начало координат',
							 command=self.star.go_begin)
		GO_BEGIN.place(x=width + 5, y=height // 5 + 354)

		def turn_star00():
			angle = int(entry1.get())
			entry1.delete(0, tk.END)
			self.star.turn_star(angle)

		tk.Label(self.root, text="Поворот относительно начала").place(
			x=width + 30, y=height // 5 + 165)

		entry1 = tk.Entry(self.root, width=10)
		entry1.place(x=width + 25, y=height // 5 + 195)

		TURN_STAR00 = tk.Button(self.root, text="Повернуть", command=turn_star00)
		TURN_STAR00.place(x=width + 130, y=height // 5 + 194)

		def turn_star_point():
			angle = int(entry2.get())
			x = int(entry_x.get())
			y = int(entry_y.get())
			entry2.delete(0, tk.END)
			entry_x.delete(0, tk.END)
			entry_y.delete(0, tk.END)
			self.star.turn_star_to_point((x, y), angle)

		tk.Label(self.root, text="Поворот относительно точки").place(
			x=width + 30, y=height // 5 + 235)

		tk.Label(self.root, text="Координата x:").place(
			x=width + 30, y=height // 5 + 265)

		tk.Label(self.root, text="Координата y:").place(
			x=width + 130, y=height // 5 + 265)

		entry2 = tk.Entry(self.root, width=10)
		entry2.place(x=width + 25, y=height // 5 + 325)

		entry_x = tk.Entry(self.root, width=10)
		entry_x.place(x=width + 25, y=height // 5 + 295)

		entry_y = tk.Entry(self.root, width=10)
		entry_y.place(x=width + 125, y=height // 5 + 295)

		TURN_STAR_POINT = tk.Button(self.root, text="Повернуть",
								command=turn_star_point)
		TURN_STAR_POINT.place(x=width + 125, y=height // 5 + 325)



