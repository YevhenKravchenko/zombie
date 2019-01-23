from random import randrange as rnd
from tkinter import *

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

m = 20  # размер ячеек
d = 2  # размер поля вокруг ячейки
N = 30
nr = N  # количество строк
nc = N  # количество столбцов
x0 = m // 2  # отступ от левого края
y0 = m // 2  # отступ от вернего края
colors = ['red', 'yellow', 'cyan', 'green']

a = []
for r in range(N):
    a.append([])
    for c in range(N):
        k = int(rnd(100)/40 - 1.25)
        a[r].append(k)  # начальное положение


class Cell():

    def __init__(self, r, c):  # при создании указываем номер строки и столбца, в который помещаем
        self.n = rnd(10)  # значение, с которым будем работать
        self.r = r  # Номер сторки в двумерном списке.
        self.c = c  # Номер столбца ...
        if a[r][c] == 0:
            self.color = 'white'
        if a[r][c] == 1:
            self.color = 'green'
        if a[r][c] == -1:
            self.color = 'red'
        if a[r][c] == 2:
            self.color = 'cyan'
        self.id = canv.create_rectangle(-100, 0, -100, 0, fill=self.color)
        self.paint()

    def paint(self):
        x1 = x0 + self.c * m + d
        # рассчитать координаты левого верхнего угла.
        y1 = y0 + self.r * m + d
        # координаты правого нижнего угла.
        x2 = x1 + m - 2 * d  # - r
        y2 = y1 + m - 2 * d
        canv.coords(self.id, x1, y1, x2, y2)
        canv.itemconfig(self.id, fill=self.color)
# графическое отображение


for y in range(N):
    for x in range(N):
        c_test = Cell(x, y)


def zombie_search(x, y):
    
    le = 1
    found = 0
    nearest_goal = None
    while found == 0 and le < 10:
        for i in range(2*le+1):
            if N > x+le > -1 and N > y-le+i > -1 and a[x+le][y-le+i] == 1:
                nearest_goal = [x+le, y-le+i]
                found = 1
            if N > x-le+i > -1 and N > y-le > -1 and a[x-le+i][y-le] == 1:
                nearest_goal = [x-le+i, y-le]
                found = 1
            if N > x-le > -1 and N > y+le-i > -1 and a[x-le][y+le-i] == 1:
                nearest_goal = [x-le, y+le-i]
                found = 1
            if N > x+le-i > -1 and N > y+1 > -1 and a[x+le-i][y+1] == 1:
                nearest_goal = [x+le-i, y+1]
                found = 1
        le = le+1
    return nearest_goal
    # поиск ближайшего человека


def zombie_move(x, y):

    nearest_goal = zombie_search(x, y)
    if abs(x - nearest_goal[0]) < 2 and abs(y - nearest_goal[1]) < 2:
        a[nearest_goal[0]][nearest_goal[1]] = 3


for t in range(1):

    t = t + 1
    for y in range(N):
        for x in range(N):
            if a[x][y] == -1:
                zombie_move(x, y)

        # первый проход, людей едят

    for y in range(N):
        for x in range(N):
            if a[x][y] == 3:
                a[x][y] = -1
        # второй проход, люди становятся зомби
    for y in range(N):
        for x in range(N):
            c_test = Cell(x, y)


mainloop()
