import tkinter as tk
from gear import gear
import numpy as np
import time
root = tk.Tk()
root.title('LABA2')
canvas = tk.Canvas(root, width=600, height=600)
grer1 = gear(canvas)
grer1.move(300.0, 300.0)
grer1.rotation_gear(np.pi / 8)
grer2 = gear(canvas)
grer2.move(235.0, 235.0)
grer3 = gear(canvas)
grer3.move(365.0, 235.0)
canvas.pack(side=tk.LEFT)
while True:
	grer1.rotation_gear(np.pi / 16)
	grer2.rotation_gear(-np.pi / 16)
	grer3.rotation_gear(-np.pi / 16)
	canvas.delete('all')
	grer1.paint()
	grer2.paint()
	grer3.paint()
	root.update()
	time.sleep(0.05)

