"""
                                        3.7 Метод __bool__ 9
Подвиг 9 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, x3,..., xN)
где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

С каждым объектом класса Vector должны выполняться операторы:

v1 + v2 # суммирование соответствующих координат векторов
v1 - v2 # вычитание соответствующих координат векторов
v1 * v2 # умножение соответствующих координат векторов

v1 += 10 # прибавление ко всем координатам вектора числа 10
v1 -= 10 # вычитание из всех координат вектора числа 10
v1 += v2
v2 -= v1

v1 == v2 # True, если соответствующие координаты векторов равны
v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными)
координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.

Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться
исключение командой:

raise ArithmeticError('размерности векторов не совпадают')
P.S. В программе на экран выводить ничего не нужно, только объявить класс.
"""


class Vector:
    def __init__(self, *args):
        self.lst = []
        if args:
            [self.lst.append(i) for i in args]

    def _checker(self, it):
        if len(self.lst) != len(it.lst):
            raise ArithmeticError('размерности векторов не совпадают')
        return True

    def __add__(self, it):
        if self._checker(it):
            return Vector(*[self.lst[i] + it.lst[i] for i in range(len(self.lst))])

    def __radd__(self, it):
        return self.__add__(it)

    def __sub__(self, it):
        if self._checker(it):
            return Vector(*[self.lst[i] - it.lst[i] for i in range(len(self.lst))])

    def __rsub__(self, it):
        return self.__sub__(it)

    def __mul__(self, it):
        if self._checker(it):
            return Vector(*[self.lst[i] * it.lst[i] for i in range(len(self.lst))])

    def __iadd__(self, other):
        if type(other) in (int, float):
            self.lst = [i + other for i in self.lst]
            return self
        if isinstance(other, Vector):
            if self._checker(other):
                self.lst = [self.lst[i] + other.lst[i] for i in range(len(self.lst))]
        return self

    def __isub__(self, other):
        if type(other) in (int, float):
            self.lst = [i - other for i in self.lst]
            return self
        if isinstance(other, Vector):
            if self._checker(other):
                self.lst = [self.lst[i] - other.lst[i] for i in range(len(self.lst))]
        return self

    def __eq__(self, other):
        return self.lst == other.lst


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).lst)  # [5, 7, 9]
print((v1 - v2).lst)  # [-3, -3, -3]
print((v1 * v2).lst)  # [4, 10, 18]

v1 += 10
print(v1.lst)  # [11, 12, 13]
v1 -= 10
print(v1.lst)  # [1, 2, 3]
v1 += v2
print(v1.lst)  # [5, 7, 9]
v2 -= v1
print(v2.lst)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True