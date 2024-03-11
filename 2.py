import tkinter as tk
import time

class WalkingMan:
    def __init__(self, canvas):
        self.canvas = canvas
        self.head = canvas.create_oval(40, 10, 60, 30, fill='black')
        self.body = canvas.create_line(50, 30, 50, 60, fill='black')
        self.left_leg = canvas.create_line(50, 60, 40, 80, fill='black')
        self.right_leg = canvas.create_line(50, 60, 60, 80, fill='black')
        self.left_arm = canvas.create_line(50, 40, 40, 30, fill='black')
        self.right_arm = canvas.create_line(50, 40, 60, 30, fill='black')

    def move(self, dx, dy):
        self.canvas.move(self.head, dx, dy)
        self.canvas.move(self.body, dx, dy)
        self.canvas.move(self.left_leg, dx, dy)
        self.canvas.move(self.right_leg, dx, dy)
        self.canvas.move(self.left_arm, dx, dy)
        self.canvas.move(self.right_arm, dx, dy)

def animate_man(walking_man, steps):
    for _ in range(steps):
        walking_man.move(10, 0)
        root.update()
        time.sleep(0.2)

def main():
    global root
    root = tk.Tk()
    root.title("Walking Man")

    canvas = tk.Canvas(root, width=100, height=100)
    canvas.pack()

    walking_man = WalkingMan(canvas)

    while True:
        walking_man.move(10, 0)
        root.update()
        time.sleep(0.5)  # Increase the sleep time to slow down the animation

    root.mainloop()

if __name__ == "__main__":
    main()
