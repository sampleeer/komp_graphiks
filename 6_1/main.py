import time
from tkinter import *
from copy import deepcopy

Vertex = []


def clear():
    Vertex.clear()
    graph.delete('point', 'line', 'mark_point')


# Определяем сторону нахождения точки C относительно AB
# путём нахождения z координаты в векторном произведении AB и BC
def check_rotate(A, B, C):
  return -(B[0]-A[0])*(C[1]-B[1])+(B[1]-A[1])*(C[0]-B[0])


def set_point(event):
    x1 = event.x
    y1 = event.y

    Vertex.append([x1, y1])

    graph.create_oval(x1 - 2, y1 + 2,
                      x1 + 2, y1 - 2, fill='blue', tags='mark_point')


def graham_algorithm():
    srt_vertexes = deepcopy(Vertex)
    srt_vertexes.sort(key=lambda x: x[0])

    for i in range(1, len(srt_vertexes)):
        for j in range(1, len(srt_vertexes) - i):
            if check_rotate(srt_vertexes[0], srt_vertexes[j], srt_vertexes[j+1]) < 0:
                srt_vertexes[j], srt_vertexes[j+1] = srt_vertexes[j+1], srt_vertexes[j]

    #for v in srt_vertexes:
    #    graph.create_oval(v[0] - 2, v[1] + 2,
    #                      v[0] + 2, v[1] - 2, fill='red', tags='mark_point')
    #    graph.update()
    #    time.sleep(1)

    # Выбираем нужные вершины
    rez = [srt_vertexes[0], srt_vertexes[1]]
    graph.create_line(rez[0][0], rez[0][1], rez[1][0], rez[1][1], width=2, fill='white', tags='line')
    graph.update()
    time.sleep(1)
    count_lines = 1
    for i in range(2, len(srt_vertexes)):
        graph.update()
        time.sleep(1)

        while check_rotate(rez[-2], rez[-1], srt_vertexes[i]) < 0:
            graph.delete(f'line{count_lines}')
            count_lines -= 1
            del rez[-1]  # pop(S)
            graph.update()
            time.sleep(1)

        rez.append(srt_vertexes[i])  # push(S,P[i])
        count_lines += 1
        graph.create_line(rez[-2][0], rez[-2][1], rez[-1][0], rez[-1][1], width=2, fill='white', tags=['line', f'line{count_lines}'])
        graph.update()
        time.sleep(1)
    graph.create_line(rez[0][0], rez[0][1], rez[-1][0], rez[-1][1], width=2, fill='white', tags='line')
    print('complete')





root = Tk()
root.title("Hello JOPA.COM")
root.geometry("1000x800")
root.resizable(False, False)

start_bt = Button(root, command=graham_algorithm, text='Старт', font=('Arial', 12), background='red')
start_bt.place(x=820, y=30, width=160)

clear_bt = Button(root, command=clear, text='Очистить', font=('Arial', 12), background='red')
clear_bt.place(x=820, y=70, width=160)

graph = Canvas(root, width=800, height=800, background='lightblue')
graph.place(x=0, y=0)
graph.bind('<Button-1>', set_point)

root.mainloop()
