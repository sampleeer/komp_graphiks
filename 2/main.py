from Root import Window
import subprocess


def main():
    while True:
        command = input("Введите команду (1 или 2 для запуска поворота фигуры или человечка, 'exit' для выхода): ")
        if command == '1':
            win = Window()
            win.root.mainloop()
        elif command == '2':
            subprocess.run(['python', 'WalkingMan.py'])
        elif command.lower() == 'exit':
            break
        else:
            print("Неправильная команда. Пожалуйста, введите 1 или 2.")


if __name__ == "__main__":
    main()
