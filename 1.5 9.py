"""
                                1.5 Инициализатор __init__ и финализатор __del__ 9

Большой подвиг 10. Объявите два класса:

Cell - для представления клетки игрового поля;
GamePole - для управления игровым полем, размером N x N клеток.

С помощью класса Cell предполагается создавать отдельные клетки командой:

c1 = Cell(around_mines, mine)
Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False), означающая наличие мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться локальные свойства:

around_mines - число мин вокруг клетки (начальное значение 0);
mine - наличие мины в текущей клетке (True/False);
fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).

С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:

pole_game = GamePole(N, M)
Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса Cell и все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole.

В классе GamePole должны быть также реализованы, следующие методы:

init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, разумеется каждая мина должна находиться в отдельной клетке).
show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта, то отображается символ #).

При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для первоначальной инициализации игрового поля.

В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12.

P.S. На экран в программе ничего выводить не нужно.

"""

from random import randrange


class Cell:
    def __init__(self, mine, around_mines=0, fl_open=True):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open

    def change_around_mines(self, value):
        self.around_mines = value


class GamePole:
    def __init__(self, n, m=0):
        self.n = n
        self.m = m
        self.pole = [[Cell(False) for _ in range(n)] for _ in range(n)]
        self.init()

    def init(self):
        mines = 0
        while mines != self.m:
            x, y = randrange(self.n), randrange(self.n)
            if not self.pole[x][y].mine:
                mines += 1
                self.pole[x][y] = Cell(True, fl_open=True)

    def show(self):
        for row in self.pole:
            for elem in row:
                if not elem.fl_open:
                    print('#', end=' ')
                elif elem.mine:
                    print("*", end=' ')
                else:
                    print(elem.around_mines, end=' ')
            print()

    def count_around_mines(self):
        for i in range(self.n):
            for j in range(self.n):
                count = 0
                if self.pole[i][j].around_mines == 0 and not self.pole[i][j].mine:
                    for delta_i in range(-1, 2):
                        if i + delta_i in range(self.n):
                            for delta_j in range(-1, 2):
                                if j + delta_j in range(self.n):
                                    if self.pole[i + delta_i][j + delta_j].mine:
                                        count += 1
                if count > 0:
                    self.pole[i][j].change_around_mines(count)


pole_game = GamePole(10, 12)
pole_game.count_around_mines()
print(pole_game.show())
