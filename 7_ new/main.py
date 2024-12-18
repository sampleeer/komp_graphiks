import time
from tkinter import *
from copy import deepcopy, copy
from math import sqrt

Vertex = []


def orientation(a, b, c):
    res = ((b.y - a.y) * (c.x - b.x) -
              (c.y - b.y) * (b.x - a.x))

    if (res == 0):
        return 0
    if (res > 0):
        return 1
    return -1


def check_rotate(A, B, C):
  return -(B.x-A.x)*(C.y-B.y)+(B.y-A.y)*(C.x-B.x)

#def cercle_circonscrit(T):
#    (x1, y1), (x2, y2), (x3, y3) = T
#    A = np.array([[x3-x1,y3-y1],[x3-x2,y3-y2]])
#    Y = np.array([(x3**2 + y3**2 - x1**2 - y1**2),(x3**2+y3**2 - x2**2-y2**2)])
#    if np.linalg.det(A) == 0:
#        return False
#    Ainv = np.linalg.inv(A)
#    X = 0.5*np.dot(Ainv,Y)
#    x,y = X[0],X[1]
#    r = sqrt((x-x1)**2+(y-y1)**2)
#    return (x,y),r

def check_rotate_a(A, B, C):
  return -(B[0]-A[0])*(C[1]-B[1])+(B[1]-A[1])*(C[0]-B[0])


class Node:
    def __init__(self, x_=0, y_=0):
        self.x = x_
        self.y = y_

    def __str__(self):
        return f'[{self.x} {self.y}]'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y



class Triangle:

    def __init__(self, nodes_: list[Node]):
        self.nodes = nodes_
        self.adjacent = []
        if check_rotate(self.nodes[0], self.nodes[1], self.nodes[2]) < 0:
            self.nodes[1], self.nodes[2] = self.nodes[2], self.nodes[1]

    def draw(self):
        for i in range(3):
            graph.create_line(self.nodes[i].x, self.nodes[i].y, self.nodes[(i+1)%3].x, self.nodes[(i+1)%3].y,
                            tags=f'{self.nodes[i].x}.{self.nodes[i].y}.{self.nodes[(i+1)%3].x}.{self.nodes[(i+1)%3].y}')

    def draw_circle(self):
        n = self.nodes
        x_c = -1/2 * (  n[0].y*(n[1].x**2+n[1].y**2-n[2].x**2-n[2].y**2)+n[1].y*(n[2].x**2+n[2].y**2-n[0].x**2-n[0].y**2)+n[2].y*(n[0].x**2+n[0].y**2-n[1].x**2-n[1].y**2)) \
        / (n[0].x*(n[1].y-n[2].y)+n[1].x*(n[2].y-n[0].y)+n[2].x*(n[0].y-n[1].y))

        y_c = 1/2 * (  n[0].x*(n[1].x**2+n[1].y**2-n[2].x**2-n[2].y**2)+n[1].x*(n[2].x**2+n[2].y**2-n[0].x**2-n[0].y**2)+n[2].x*(n[0].x**2+n[0].y**2-n[1].x**2-n[1].y**2)) \
        / (n[0].x*(n[1].y-n[2].y)+n[1].x*(n[2].y-n[0].y)+n[2].x*(n[0].y-n[1].y))

        r = sqrt( (x_c - n[0].x)**2 + (y_c - n[0].y)**2)

        graph.create_oval(x_c - r, y_c-r,x_c + r, y_c+r, outline='blue')

    def __str__(self):
        return f'( {str(self.nodes[0])}, {str(self.nodes[1])}, {str(self.nodes[2])})'





def clear():
    Vertex.clear()
    graph.delete('all')


def set_point(event):
    x1 = event.x
    y1 = event.y

    Vertex.append([x1, y1])
    print([x1, y1])
    graph.create_oval(x1 - 2, y1 + 2,
                      x1 + 2, y1 - 2, fill='blue', tags='mark_point')

def check_smeg(trg1: Triangle, trg2: Triangle):
    if trg1.nodes[0] in trg2.nodes and trg1.nodes[1] in trg2.nodes or \
       trg1.nodes[1] in trg2.nodes and trg1.nodes[2] in trg2.nodes or \
       trg1.nodes[0] in trg2.nodes and trg1.nodes[2] in trg2.nodes:
        return True
    return False


def flip(tg1: Triangle, tg2: Triangle):
    a2 = None
    a0 = None
    idx = 0
    for i in range(3):
        if tg1.nodes[i] not in tg2.nodes:
            a2 = tg1.nodes[i]
            idx = i
            break
    for node in tg2.nodes:
        if node not in tg1.nodes:
            a0 = node
            break
    a1 = tg1.nodes[idx - 1]
    a3 = tg1.nodes[(idx + 1) % 3]

    tg1.nodes = [a0, a2, a1]
    tg2.nodes = [a0, a2, a3]
    return

def check_delone(tg1: Triangle, tg2: Triangle):
    """ РћСЃСѓС‰РµСЃС‚РІР»СЏРµС‚ РїСЂРѕРІРµСЂРєСѓ СѓСЃР»РѕРІРёСЏ РґРµР»РѕРЅРµ РґР»СЏ 2 С‚СЂРµСѓРіРѕР»СЊРЅРёРєРѕРІ Рё РґРµР»Р°РµС‚ С„Р»РёРї"""
    a2 = None
    a0 = None
    idx = 0
    for i in range(3):
        if tg1.nodes[i] not in tg2.nodes:
            a2 = tg1.nodes[i]
            idx = i
            break
    for node in tg2.nodes:
        if node not in tg1.nodes:
            a0 = node
            break
    if a2 is None and a0 is None:
        return []
    a1 = tg1.nodes[idx-1]
    a3 = tg1.nodes[(idx+1)%3]
    # РЈСЃР»РѕРІРёРµ РґР»СЏ РїСЂРѕРІРµСЂРєРё СЃСѓРјРјС‹ СѓРіР»РѕРІ
    check_value = abs((a0.x - a1.x)*(a0.y - a3.y) - (a0.x - a3.x)*(a0.y - a1.y)) * ((a2.x - a1.x)*(a2.x - a3.x) + (a2.y - a1.y)*(a2.y-a3.y))\
        + ((a0.x - a1.x)*(a0.x - a3.x) + (a0.y - a3.y)*(a0.y - a1.y)) * abs((a2.x - a1.x)*(a2.y - a3.y) - (a2.x - a3.x)*(a2.y-a1.y))

    if check_value < 0:
        tg1.nodes = [a0, a2, a1]
        tg2.nodes = [a0, a2, a3]
        graph.delete(f'{a1.x}.{a1.y}.{a3.x}.{a3.y}')
        graph.delete(f'{a3.x}.{a3.y}.{a1.x}.{a1.y}')
        graph.create_line(a0.x,a0.y, a2.x, a2.y, tags=f'{a0.x}.{a0.y}.{a2.x}.{a2.y}')
        graph.update()
        time.sleep(2)
        i = 0
        n = len(tg1.adjacent)
        while i < n:
            if not check_smeg(tg1, tg1.adjacent[i]):
                tg1.adjacent[i].adjacent.append(tg2)
                tg1.adjacent[i].adjacent.remove(tg1)
                tg2.adjacent.append(tg1.adjacent[i])
                tg1.adjacent.pop(i)
                n -= 1
            else:
                i += 1
        i = 0
        n = len(tg2.adjacent)
        while i < n:
            if not check_smeg(tg2, tg2.adjacent[i]):
                tg2.adjacent[i].adjacent.append(tg1)
                tg2.adjacent[i].adjacent.remove(tg2)
                tg1.adjacent.append(tg2.adjacent[i])
                tg2.adjacent.pop(i)
                n -= 1
            else:
                i += 1
        return [tg1, tg2]
    return []

def checker(trg: Triangle):
    for adj_trg in trg.adjacent:
        new = check_delone(trg, adj_trg)
        if new:
            return new

    return []

def sgn(a):
    if a<0:
        return -1
    elif a>0:
        return 1
    return 0

def is_point_in_triangle(pt: Node, tri: Triangle) -> bool:
    # Проверка, находится ли точка внутри треугольника
    a = (tri.nodes[1].y - tri.nodes[0].y) * (pt.x - tri.nodes[0].x) - (tri.nodes[1].x - tri.nodes[0].x) * (pt.y - tri.nodes[0].y)
    b = (tri.nodes[2].y - tri.nodes[1].y) * (pt.x - tri.nodes[1].x) - (tri.nodes[2].x - tri.nodes[1].x) * (pt.y - tri.nodes[1].y)
    c = (tri.nodes[0].y - tri.nodes[2].y) * (pt.x - tri.nodes[2].x) - (tri.nodes[0].x - tri.nodes[2].x) * (pt.y - tri.nodes[2].y)
    return (a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0)


def segments_intersect(p1, p2, p3, p4):
    # Проверка пересечения двух отрезков, заданных точками
    d1 = check_rotate(p3, p4, p1)
    d2 = check_rotate(p3, p4, p2)
    d3 = check_rotate(p1, p2, p3)
    d4 = check_rotate(p1, p2, p4)

    if (d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0):
        return (d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)

    return (d1 == 0 and on_segment(p1, p3, p4)) or (d2 == 0 and on_segment(p2, p3, p4)) or \
           (d3 == 0 and on_segment(p3, p1, p2)) or (d4 == 0 and on_segment(p4, p1, p2))


def are_collinear(a, b, c, threshold=1e-9):
    # Проверка на коллинеарность с учётом порога
    return abs((b.y - a.y) * (c.x - b.x) - (c.y - b.y) * (b.x - a.x)) < threshold


def is_point_collinear(pt: Node, line_start: Node, line_end: Node, threshold=1e-9):
    # Проверка коллинеарности точки относительно линии
    return abs((line_end.y - line_start.y) * (pt.x - line_start.x) - (line_end.x - line_start.x) * (pt.y - line_start.y)) < threshold


def on_segment(p, q, r):
    # Проверяет, находится ли точка q на отрезке pr
    return (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and
            q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y))




def sort_points(points):
    """Сортировка точек по оси Y, затем по оси X."""
    return sorted(points, key=lambda p: (p[1], p[0]))


def is_valid_triangle(new_triangle: Triangle, existing_triangles: list[Triangle]) -> bool:
    """Проверка на валидность нового треугольника."""
    for existing in existing_triangles:
        # Проверка на пересечения между ребрами нового и существующего треугольников
        for i in range(3):
            if segments_intersect(new_triangle.nodes[i], new_triangle.nodes[(i + 1) % 3],
                                  existing.nodes[0], existing.nodes[1]) or \
                    segments_intersect(new_triangle.nodes[i], new_triangle.nodes[(i + 1) % 3],
                                       existing.nodes[1], existing.nodes[2]) or \
                    segments_intersect(new_triangle.nodes[i], new_triangle.nodes[(i + 1) % 3],
                                       existing.nodes[2], existing.nodes[0]):
                return False
    return True


def find_triangle(triangles: list[Triangle], node: Node):
    """Поиск подходящего треугольника и добавление новой точки."""

    # Сначала проверяем, в каком треугольнике находится новая точка
    for cur in triangles:
        if is_point_in_triangle(node, cur):
            return (cur, -1)

    # Проходим по всем треугольникам, чтобы найти подходящий для добавления новой точки
    for cur in triangles:
        for i in range(3):
            # Проверка и выбор соседнего треугольника
            if sgn(check_rotate(cur.nodes[i - 1], cur.nodes[(i + 1) % 3], node)) != \
                    sgn(check_rotate(cur.nodes[i - 1], cur.nodes[(i + 1) % 3], cur.nodes[i])):

                # Теперь проверим соседние треугольники (adjacent)
                for adj in cur.adjacent:
                    # Убедимся, что сосед не содержит узел, с которым мы работаeм
                    if cur.nodes[i] not in adj.nodes:
                        new_triangle = Triangle([cur.nodes[i], adj.nodes[0], node])
                        if is_valid_triangle(new_triangle, triangles):
                            triangles.append(new_triangle)  # Добавить новый треугольник
                            return (new_triangle, -1)
                break

    return [None, -1]


def check_vp_obl(v_obl: list[Node], point:Node):
    """Подсчитывает суммы всех интервалов"""
    n = len(v_obl)
    ind = 0

    for i in range(1, n):
        if ((point.x - v_obl[i].x)**2 + (point.y - v_obl[i].y)**2) < ((point.x - v_obl[ind].x)**2 + (point.y - v_obl[ind].y)**2):
            ind = i

    # Find the upper tangent
    up = ind
    while check_rotate(point, v_obl[up], v_obl[(up + 1) % n]) < 0:
        up = (up + 1) % n

    # Find the lower tangent
    low = ind
    while check_rotate(v_obl[(low - 1) % n], v_obl[low], point) < 0:
        low = (low - 1) % n
    return [low, up]



# Сортировка точек перед началом триангуляции
def delone_algorithm():

    tgs = []
    a = Node(Vertex[0][0], Vertex[0][1]); b = Node(Vertex[1][0], Vertex[1][1]); c = Node(Vertex[2][0], Vertex[2][1]);
    if check_rotate(a, b, c) < 0:
        b, c = c, b
    tgs.append(Triangle([a, b, c]))
    vp_ob = [a, b, c]

    tgs[0].draw()
    graph.update()
    time.sleep(1)


    for v_idx in range(3, len(Vertex)):
        new_node = Node(Vertex[v_idx][0], Vertex[v_idx][1])
        graph.create_oval(new_node.x - 2, new_node.y + 2,
                          new_node.x + 2, new_node.y - 2, fill='red', tags='mark_point')
        graph.update()
        time.sleep(1)
        cur_triangle, flag = find_triangle(tgs, new_node)
        new_triangles = []

        # Далее точки в форме треугольника
        if cur_triangle is None:
            up, low = check_vp_obl(vp_ob, new_node)
            n = len(vp_ob)
            #sn = sgn(check_rotate(vp_ob[0], vp_ob[1], vp_ob[2]))
            graph.create_line(new_node.x, new_node.y, vp_ob[low].x, vp_ob[low].y,
                              tags=f'{new_node.x}.{new_node.y}.{vp_ob[low].x}.{vp_ob[low].y}')
            low_copy = low
            while up != low:
                new_triangles.append(Triangle([Node(new_node.x, new_node.y), Node(vp_ob[low].x, vp_ob[low].y),
                                               Node(vp_ob[(low - 1) % n].x, vp_ob[(low - 1) % n].y)]))
                tgs.append(new_triangles[-1])

                if len(new_triangles) > 1:
                    new_triangles[-1].adjacent.append(new_triangles[-2])
                    new_triangles[-2].adjacent.append(new_triangles[-1])

                low = (low - 1)%n
                graph.create_line(new_node.x, new_node.y, vp_ob[low].x, vp_ob[low].y,
                                  tags=f'{new_node.x}.{new_node.y}.{vp_ob[low].x}.{vp_ob[low].y}')
            if low_copy < up:
                vp_ob = vp_ob[low_copy:up+1]
                vp_ob.append(new_node)
            else:
                vp_ob = vp_ob[:up+1] + [new_node] + vp_ob[low_copy:]

            for tg in new_triangles:
                for tg_adj in tgs:
                    if tg != tg_adj:
                        if tg.nodes[1] in tg_adj.nodes and tg.nodes[2] in tg_adj.nodes:
                            tg.adjacent.append(tg_adj)
                            tg_adj.adjacent.append(tg)
            graph.update()
            time.sleep(1)
        elif flag == -1:
            for adj_trg in cur_triangle.adjacent:
                adj_trg.adjacent.remove(cur_triangle)

            new_triangle1 = copy(cur_triangle)
            new_triangle1.nodes = copy(cur_triangle.nodes)
            new_triangle1.adjacent = copy(cur_triangle.adjacent)
            new_triangle2 = copy(cur_triangle)
            new_triangle2.nodes = copy(cur_triangle.nodes)
            new_triangle2.adjacent = copy(cur_triangle.adjacent)
            cur_triangle.adjacent.append(new_triangle1)
            cur_triangle.adjacent.append(new_triangle2)
            new_triangle1.adjacent.append(cur_triangle)
            new_triangle1.adjacent.append(new_triangle2)
            new_triangle2.adjacent.append(cur_triangle)
            new_triangle2.adjacent.append(new_triangle1)

            new_triangles = [cur_triangle, new_triangle1, new_triangle2]

            nodes = cur_triangle.nodes
            new_triangle1.nodes = [nodes[1], new_node, nodes[2]]
            new_triangle2.nodes = [new_node, nodes[2], nodes[0]]
            cur_triangle.nodes = [nodes[0], nodes[1], new_node]

            for cur_trg in new_triangles:
                n = len(cur_trg.adjacent)
                i = 0
                while i < n:
                    if not check_smeg(cur_trg, cur_trg.adjacent[i]):
                        cur_trg.adjacent.pop(i)
                        n -= 1
                    elif cur_trg not in cur_trg.adjacent[i].adjacent:
                        cur_trg.adjacent[i].adjacent.append(cur_trg)
                        i += 1
                    else:
                        i += 1

            tgs.append(new_triangle1)
            tgs.append(new_triangle2)

            new_triangle1.draw()
            new_triangle2.draw()
            cur_triangle.draw()
            graph.update()
            time.sleep(1)

        count = 0
        while count < 100 and len(new_triangles) != 0:
            cur_trg = new_triangles.pop(0)
            new_trgs = checker(cur_trg)
            if new_trgs:
                new_triangles += new_trgs
            count += 1
        if count == 100:
            print('я не раб')


    #for tg in tgs:
    #    tg.draw_circle()
    print('complete')






root = Tk()
root.title("Hello JOPA.COM")
root.geometry("1000x800")
root.resizable(False, False)

start_bt = Button(root, command=delone_algorithm, text='Старт', font=('Arial', 12), background='red')
start_bt.place(x=820, y=30, width=160)

clear_bt = Button(root, command=clear, text='Очистить', font=('Arial', 12), background='red')
clear_bt.place(x=820, y=70, width=160)

graph = Canvas(root, width=800, height=800, background='lightblue')
graph.place(x=0, y=0)
graph.bind('<Button-1>', set_point)

root.mainloop()