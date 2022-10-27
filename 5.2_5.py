"""
                            5.2 Обработка исключений. Блоки finally и else  5

Подвиг 5. Объявите в программе класс Point, объекты которого должны создаваться командами:

pt = Point()
pt = Point(x, y)
где x, y - произвольные числа (координаты точки).

В каждом объекте класса Point должны формироваться локальные атрибуты _x, _y с соответствующими значениями.
Если аргументы не указываются (первая команда), то _x = 0, _y = 0.

Далее, в программе вводятся два значения в одну строчку через пробел. Значениями могут быть числа, слова,
булевы величины (True/False). Необходимо прочитать эти значения из входного потока. Если оба значения являются
числами, то формировать объект pt командой:

pt = Point(x, y)
Если хотя бы одно из значений не числовое, то формировать объект pt командой:

pt = Point()
Реализовать этот функционал с помощью блоков try/except. А в блоке finally вывести на экран сообщение в формате
(без кавычек):

"Point: x = <значение x>, y = <значение y>"

Sample Input:

10 20
Sample Output:

Point: x = 10, y = 20
"""


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return f"Point: x = {self._x}, y = {self._y}"


input_data = input().split()
try:
    try:
        n, m = map(int, input_data)
    except ValueError:
        n, m = map(float, input_data)
    pt = Point(n, m)
except ValueError:
    pt = Point()
finally:
    print(f"Point: x = {pt.x}, y = {pt.y}")
