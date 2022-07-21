"""
                                                3.6 Методы __eq__ и __hash__ 9

Подвиг 9 (релакс). Объявите класс с именем Dimensions, объекты которого создаются командой:

d = Dimensions(a, b, c)
где a, b, c - положительные числа (целые или вещественные), описывающие габариты некоторого тела: высота, ширина
и глубина.

Каждый объект класса Dimensions должен иметь аналогичные публичные атрибуты a, b, c (с соответствующими числовыми
значениями). Также для каждого объекта должен вычисляться хэш на основе всех трех габаритов: a, b, c.

С помощью функции input() прочитайте из входного потока строку, записанную в формате:

"a1 b1 c1; a2 b2 c2; ... ;aN bN cN"

Например:

"1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"

Если какой-либо габарит оказывается отрицательным значением или равен нулю, то при создании объектов должна
генерироваться ошибка командой:

raise ValueError("габаритные размеры должны быть положительными числами")
Сформируйте на основе прочитанной строки список lst_dims из объектов класса Dimensions. После этого отсортируйте этот
список по возрастанию (неубыванию) хэшей этих объектов так, чтобы объекты с равными хэшами стояли друг за другом.

P.S. На экран ничего выводить не нужно.

Sample Input:

1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5
Sample Output:

"""

s_inp = input()  # эту строку (переменную s_inp) в программе не менять


class Dimensions:
    def __init__(self, a, b, c):
        if not self._verify(a, b, c)[1]:
            raise ValueError("габаритные размеры должны быть положительными числами")

        self.a = self._verify(a, b, c)[0][0]
        self.b = self._verify(a, b, c)[0][1]
        self.c = self._verify(a, b, c)[0][2]

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    @staticmethod
    def _verify(*args):
        res = []
        for i in args:
            if float(i):
                res.append(float(i))
            elif int(i):
                res.append(int(i))
        return [res, all([i > 0 for i in res])]

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_dims = []
for i in s_inp.split('; '):
    j = i.split()
    lst_dims.append(Dimensions(j[0], j[1], j[2]))

lst_dims = sorted(lst_dims, key=hash)