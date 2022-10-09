"""
                                                3.7 Метод __bool__  8

Большой подвиг 8. Вы начинаете разрабатывать игру "Сапер". Для этого вам нужно уметь представлять и управлять
игровым полем. Будем полагать, что оно имеет размеры N x M клеток. Каждая клетка будет представлена объектом класса
Cell и содержать либо число мин вокруг этой клетки, либо саму мину.

https://ucarecdn.com/d80778c6-b03e-451e-aa32-7ba65bcb644f/

Для начала в программе объявите класс GamePole, который будет создавать и управлять игровым полем. Объект этого класса
должен формироваться командой:

pole = GamePole(N, M, total_mines)
И, так как поле в игре одно, то нужно контролировать создание только одного объекта класса GamePole (используйте
паттерн Singleton, о котором мы с вами говорили, когда рассматривали магический метод __new__()).

Объект pole должен иметь локальный приватный атрибут:

__pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов (N строк и M столбцов), состоящий из объектов
класса Cell.

Для доступа к этой коллекции объявите в классе GamePole объект-свойство (property):

pole - только для чтения (получения) ссылки на коллекцию __pole_cells.

Далее, в самом классе GamePole объявите следующие методы:

init_pole() - для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);
open_cell(i, j) - открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля; метод меняет значение
атрибута __is_open объекта Cell в ячейке (i, j) на True;
show_pole() - отображает игровое поле в консоли (как именно сделать - на ваше усмотрение, этот метод -
домашнее задание).

Расстановку мин выполняйте случайным образом по игровому полю (для этого удобно воспользоваться функцией randint
модуля random). После расстановки всех total_mines мин, вычислите их количество вокруг остальных клеток (где нет мин).
Область охвата - соседние (прилегающие) клетки (8 штук).

В методе open_cell() необходимо проверять корректность индексов (i, j). Если индексы указаны некорректно,
то генерируется исключение командой:

raise IndexError('некорректные индексы i, j клетки игрового поля')
Следующий класс Cell описывает состояние одной ячейки игрового поля. Объекты этого класса создаются командой:

cell = Cell()
При этом в самом объекте создаются следующие локальные приватные свойства:

__is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
__number - число мин вокруг клетки (целое число от 0 до 8);
__is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

Для работы с этими приватными атрибутами объявите в классе Cell следующие объекты-свойства с именами:

is_mine - для записи и чтения информации из атрибута __is_mine;
number - для записи и чтения информации из атрибута __number;
is_open - для записи и чтения информации из атрибута __is_open.

В этих свойствах необходимо выполнять проверку на корректность переданных значений (либо булево значение True/False,
либо целое число от 0 до 8). Если передаваемое значение некорректно, то генерировать исключение командой:

raise ValueError("недопустимое значение атрибута")
С объектами класса Cell должна работать функция:

bool(cell)
которая возвращает True, если клетка закрыта и False - если открыта.

Пример использования классов (эти строчки в программе писать не нужно):

pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
P.S. В программе на экран выводить ничего не нужно, только объявить классы.
"""
from random import randint


# здесь объявляйте классы

class GamePole:
    _instance = None

    def __new__(cls, *argc, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, N, M, total_mines):
        if '_total_mines' not in self.__dict__:
            self.__N, self.__M, self.__total_mines = N, M, total_mines
            self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))
            # - двумерный (вложенный) кортеж, размерами N x M элементов (N строк и M столбцов), состоящий из объектов класса Cell.
            if '_debug' in globals():
                print(*self.__pole_cells, sep='\n')
                print(len(self.__pole_cells))

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        ''' - для инициализации начального состояния игрового поля расставляет мины и делает все клетки закрытыми);'''
        from random import randrange
        mines = set()
        # Сначала создадим множество точек для минирования
        while len(mines) < self.__total_mines:
            coords = (randrange(0, self.__N), randrange(0, self.__M))
            mines.add(coords)

        # Теперь проведём собственно минирование нужных точек и разминирование остальных
        for i in range(self.__N):
            for j in range(self.__M):
                self.__pole_cells[i][j].is_open = False
                self.__pole_cells[i][j].is_mine = ((i, j) in mines)
                if not self.__pole_cells[i][j].is_mine:
                    self.__pole_cells[i][j].number = len([*filter(
                        lambda x: x in mines,
                        (
                            (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                            (i, j - 1), (i, j + 1),
                            (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
                        )
                    )])
        self.__mines = mines

    def open_cell(self, i, j):
        ''' - открывает ячейку с индексами (i, j);
        нумерация индексов начинается с нуля; метод меняет значение атрибута __is_open
        объекта Cell в ячейке (i, j) на True;'''
        self.__pole_cells[i][j].is_open = True

    def show_pole(self):
        '''show_pole() - отображает игровое поле в консоли
        как именно сделать - на ваше усмотрение, этот метод - домашнее задание).
        '''
        for i in range(self.__N):
            for j in range(self.__M):
                cl = self.__pole_cells[i][j]

                if cl:
                    print('?', end='')
                else:
                    print('*' if cl.is_mine else cl.number, end='')

            print()

    def show_pole_all(self):
        for i in range(self.__N):
            for j in range(self.__M):
                cl = self.__pole_cells[i][j]
                print('*' if cl.is_mine else cl.number, end='')
            print()


class Cell:
    def __init__(self):
        self.__is_mine = False
        # - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
        self.__number = 0
        # - число мин вокруг клетки (целое число от 0 до 8);
        self.__is_open = False
        # - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not isinstance(value, int) or not 0 <= value <= 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        return not self.__is_open


