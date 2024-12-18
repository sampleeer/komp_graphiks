import tkinter as tk
from cmath import cos, sin, pi, sqrt, acos, asin
import time
from math import ceil


def print_dots(x, y, color):
    global canvas
    x1 = x
    # y1 = 800 - y
    y1 = y
    canvas.create_oval(x1 - 2, y1 - 2, x1 + 2, y1 + 2, fill=color)


def print_pixel(x, y, color):
    global canvas
    x1 = x
    # y1 = 800 - y
    y1 = y
    canvas.create_line(x1, y1, x1, y1 + 1, fill=color)


def cross_AB_AC(A, B, C):
    AB = [B[0] - A[0], B[1] - A[1]]
    AC = [C[0] - A[0], C[1] - A[1]]
    return AB[0] * AC[1] - AB[1] * AC[0]


class triangle:
    d = []

    def set(self, A, B, C):
        l = [A, B, C]
        l.sort()
        self.d = l


def make_triangle(a, b, c):
    buf = triangle()
    buf.set(a, b, c)
    return buf


def print_triangle(list_tr, dots):
    canvas.create_rectangle(0, 0, 800, 800, fill='white', outline='white')

    for i in list_tr:
        canvas.create_line(dots[i.d[0]][0], dots[i.d[0]][1], dots[i.d[1]][0], dots[i.d[1]][1])
        canvas.create_line(dots[i.d[1]][0], dots[i.d[1]][1], dots[i.d[2]][0], dots[i.d[2]][1])
        canvas.create_line(dots[i.d[0]][0], dots[i.d[0]][1], dots[i.d[2]][0], dots[i.d[2]][1])
    for i in dots:
        print_dots(i[0], i[1], 'black')
    win.update()
    # time.sleep(1)


def check_in_tr(A, B, C, D):
    if abs(cross_AB_AC(A, B, C)) == abs(cross_AB_AC(A, B, D)) + abs(cross_AB_AC(A, D, C)) + abs(cross_AB_AC(D, B, C)):
        return 1
    return 0


def check_not_pere(A, B, C, D):
    # if A == C or A == D or B == C or B == D:
    #     if (min(A[0], B[0]) <= min(C[0], D[0]) <= max(C[0], D[0]) <= max(A[0], B[0]) and min(A[1], B[1]) <= min(C[1], D[
    #         1]) <= max(C[1], D[1]) <= max(A[1], B[1])) or (
    #             min(C[0], D[0]) <= min(A[0], B[0]) <= max(A[0], B[0]) <= max(C[0], D[0]) and min(C[1], D[1]) <= min(
    #         A[1], B[1]) <= max(A[1], B[1]) <= max(C[1], D[1])):
    #         return 0
    #     return 1
    cr_abc, cr_abd, cr_cda, cr_cdb = cross_AB_AC(A, B, C), cross_AB_AC(A, B, D), cross_AB_AC(C, D, A), cross_AB_AC(
        C, D, B)
    if cross_AB_AC(A, B, C) * cross_AB_AC(A, B, D) < 0 and cross_AB_AC(C, D, A) * cross_AB_AC(C, D, B) <= 0:
        return 0
    if cr_abc != 0 or cr_abd != 0 or cr_cda != 0 or cr_cdb != 0:
        return 1
    AB, AC, AD = [B[0] - A[0], B[1] - A[1]], [C[0] - A[0], C[1] - A[1]], [D[0] - A[0], D[1] - A[1]]
    if AB[0] != 0:
        t1 = AC[0] / AB[0]
        t2 = AD[0] / AB[0]
        if (t1<=0 and t2<=0) or (1<=t1 and 1<=t2):
            return 1
    else:
        t1 = AC[1] / AB[1]
        t2 = AD[1] / AB[1]
        if (t1 <= 0 and t2 <= 0) or (1 <= t1 and 1 <= t2):
            return 1
    return 0


# def check_not_pere(P1, P2, A, B):
#
#     P2P1 = [P1[0] - P2[0], P1[1] - P2[1]]
#     N = [-P2P1[1], P2P1[0]]
#     if (N[0] * (B[0] - A[0]) + N[1] * (B[1] - A[1])) == 0:
#         return 1
#     tt = (N[0] * P1[0] - A[0] * N[0] + N[1] * P1[1] - N[1] * A[1]) / (N[0] * (B[0] - A[0]) + N[1] * (B[1] - A[1]))
#     if tt > 1 or tt < 0:
#         return 1
#     if min(P1[0], P2[0]) <= A[0] + tt * (B[0] - A[0]) <= max(P1[0], P2[0]) and min(P1[1], P2[1]) <= A[1] + tt * (
#             B[1] - A[1]) <= max(P1[1], P2[1]):
#         return 0


def find_ungle(vec):
    if asin(vec[1] / sqrt(vec[0] ** 2 + vec[1] ** 2)).real >= 0:
        return acos(vec[0] / sqrt(vec[0] ** 2 + vec[1] ** 2)).real
    else:
        return 2 * pi - acos(vec[0] / sqrt(vec[0] ** 2 + vec[1] ** 2)).real


def check_in_circle_ABC(A, B, C, D):
    a = A[0] * B[1] + A[1] * C[0] + B[0] * C[1] - (C[0] * B[1] + B[0] * A[1] + A[0] * C[1])
    b = (A[0] ** 2 + A[1] ** 2) * B[1] + A[1] * (C[0] ** 2 + C[1] ** 2) + (B[0] ** 2 + B[1] ** 2) * C[1] - (
            (C[0] ** 2 + C[1] ** 2) * B[1] + (B[0] ** 2 + B[1] ** 2) * A[1] + (A[0] ** 2 + A[1] ** 2) * C[1])
    c = (A[0] ** 2 + A[1] ** 2) * B[0] + A[0] * (C[0] ** 2 + C[1] ** 2) + (B[0] ** 2 + B[1] ** 2) * C[0] - (
            (C[0] ** 2 + C[1] ** 2) * B[0] + (B[0] ** 2 + B[1] ** 2) * A[0] + (A[0] ** 2 + A[1] ** 2) * C[0])
    d = (A[0] ** 2 + A[1] ** 2) * B[0] * C[1] + (B[0] ** 2 + B[1] ** 2) * C[0] * A[1] + (C[0] ** 2 + C[1] ** 2) * A[0] * \
        B[1] - ((A[0] ** 2 + A[1] ** 2) * C[0] * B[1] + (B[0] ** 2 + B[1] ** 2) * A[0] * C[1] + (
            C[0] ** 2 + C[1] ** 2) * B[0] * A[1])
    x = D[0]
    y = D[1]
    print(A, B, C)
    print(a, b, c, d)
    if a == 0:
        return 0
    if (a / abs(a)) * (a * (x ** 2 + y ** 2) - x * b + y * c - d) >= 0:
        return 0
    return 1


def make_new_hull(current):
    global dots, list_tr, hull
    cur_list = []
    for i in hull:
        flag = 1
        for j in range(len(hull)):
            if check_not_pere(dots[hull[j % len(hull)]], dots[hull[(j + 1) % len(hull)]], dots[i], dots[current]) == 0:
                flag = 0
                break
        if flag == 1:
            cur_list.append(i)
    new_list = [[find_ungle([dots[i][0] - dots[current][0], dots[i][1] - dots[current][1]]), i] for i in cur_list]
    flag = 0
    for i in range(len(new_list)):
        for j in range(i + 1, len(new_list)):
            if abs(new_list[i][0] - new_list[j][0]) > pi:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        for i in new_list:
            if i[0] <= pi:
                i[0] += 2 * pi
    new_list.sort()
    buf = [new_list[0][1], current, new_list[len(new_list) - 1][1]]
    pos = -1
    for i in range(len(hull)):
        if hull[i] == new_list[len(new_list) - 1][1]:
            pos = (i + 1) % len(hull)
    while hull[pos] != new_list[0][1]:
        buf.append(hull[pos])
        pos = (pos + 1) % len(hull)
    hull = buf.copy()

    del_list = []
    st = set()
    for i in range(len(list_tr)):
        if check_in_circle_ABC(dots[list_tr[i].d[0]], dots[list_tr[i].d[1]], dots[list_tr[i].d[2]], dots[current]) == 1:
            del_list.append(i)
            for j in range(3):
                if list_tr[i].d[j] not in cur_list:
                    st.add(list_tr[i].d[j])
            # st.add(list_tr[i].d[1])
            # st.add(list_tr[i].d[2])

    del_list.reverse()
    for i in del_list:
        list_tr.pop(i)
    add_l = list(st)
    new_add_list = [[find_ungle([dots[i][0] - dots[current][0], dots[i][1] - dots[current][1]]), i] for i in add_l]
    if flag == 1:
        for i in new_add_list:
            if i[0] <= pi:
                i[0] += 2 * pi
    new_list += new_add_list
    new_list.sort()
    for i in range(len(new_list) - 1):
        if cross_AB_AC(dots[current], dots[new_list[i][1]], dots[new_list[i + 1][1]])!=0:
            list_tr.append(make_triangle(current, new_list[i][1], new_list[i + 1][1]))


def make_new_tr(current, tr_in):
    global dots, list_tr, hull

    def find_tr(a, b):
        global list_tr
        if a > b:
            a, b = b, a
        for j in range(len(list_tr)):
            if list_tr[j].d[0] == a and list_tr[j].d[1] == b or list_tr[j].d[0] == a and list_tr[j].d[2] == b or \
                    list_tr[j].d[1] == a and list_tr[j].d[2] == b:
                return j
        return None

    def merge(e1, e2, current):
        cur_tr = find_tr(e1, e2)
        if cur_tr is None:
            if cross_AB_AC(dots[current], dots[e1], dots[e2]) != 0:
                list_tr.append(make_triangle(current, e1, e2))
            return
        if check_in_circle_ABC(dots[list_tr[cur_tr].d[0]], dots[list_tr[cur_tr].d[1]], dots[list_tr[cur_tr].d[2]],
                               dots[current]) == 0:
            list_tr.append(make_triangle(current, e1, e2))
        else:
            buf = list_tr[cur_tr].d.copy()
            b = -1
            for j in range(3):
                if e1 != buf[j] and e2 != buf[j]:
                    b = buf[j]
                    break
            list_tr.pop(cur_tr)
            list_tr.append(make_triangle(current, b, e1))
            list_tr.append(make_triangle(current, b, e2))

    del_list = []
    st = set()
    for i in range(len(list_tr)):
        if check_in_circle_ABC(dots[list_tr[i].d[0]], dots[list_tr[i].d[1]], dots[list_tr[i].d[2]], dots[current]) == 1:
            del_list.append(i)
            for j in range(3):
                st.add(list_tr[i].d[j])
            # st.add(list_tr[i].d[1])
            # st.add(list_tr[i].d[2])

    del_list.reverse()
    for i in del_list:
        list_tr.pop(i)
    add_l = list(st)
    new_add_list = [[find_ungle([dots[i][0] - dots[current][0], dots[i][1] - dots[current][1]]), i] for i in add_l]
    flag = 0
    for i in range(len(new_add_list)):
        for j in range(i + 1, len(new_add_list)):
            if abs(new_add_list[i][0] - new_add_list[j][0]) > pi:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        for i in new_add_list:
            if i[0] <= pi:
                i[0] += 2 * pi
    new_add_list.sort()
    for i in range(len(new_add_list)):
        list_tr.append(make_triangle(current, new_add_list[i][1], new_add_list[(i + 1) % len(new_add_list)][1]))


def make_step(current):
    global dots, list_tr, hull
    tr_in = []
    for i in range(len(list_tr)):
        if check_in_tr(dots[list_tr[i].d[0]], dots[list_tr[i].d[1]], dots[list_tr[i].d[2]], dots[current]):
            tr_in.append(i)

    if len(tr_in) == 0:
        make_new_hull(current)
    else:
        make_new_tr(current, tr_in)

    print_triangle(list_tr, dots)
    print(hull)


win = tk.Tk()
win.title("lab 7")
win.geometry("800x800")
win.resizable(False, False)
# ------------------------------------------------------------
canvas = tk.Canvas(win, bg="white", width=800, height=800)
canvas.place(x=0, y=0)

f_file = open("7.txt", "r")
n = int(f_file.readline())
dots = []
for i in range(n):
    dots.append(list(map(int, f_file.readline().split())))
list_tr = []
uses_dots = []

for i in range(2, n):
    if cross_AB_AC(dots[0], dots[1], dots[i]) != 0:
        list_tr.append(make_triangle(0, 1, i))
        if cross_AB_AC(dots[0], dots[1], dots[i]) > 0:
            uses_dots.append(1)
            uses_dots.append(0)
            uses_dots.append(i)
        else:
            uses_dots.append(1)
            uses_dots.append(i)
            uses_dots.append(0)
        break
hull = uses_dots.copy()

print(hull)
print_triangle(list_tr, dots)
for i in range(2, n):
    if i not in uses_dots:
        uses_dots.append(i)
        make_step(i)
print('i am here')
win.mainloop()