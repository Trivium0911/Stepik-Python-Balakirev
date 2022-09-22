"""
                        4.1 Наследование в объектно-ориентированном программировании  10

Подвиг 10 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, ..., xN)
где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).

С объектами этого класса должны выполняться команды:

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:

raise TypeError('размерности векторов не совпадают')
В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих координат вектора.

На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:

v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
При операциях сложения и вычитания с объектом класса VectorInt:

v = v1 + v2  # v1 - объект класса VectorInt
v = v1 - v2  # v1 - объект класса VectorInt
должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной. Иначе,
v должен быть объектом класса VectorInt.

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.


"""


class Vector:
    _allowed_types = (int, float)

    def __init__(self, *coords):
        self.__check_coords(coords)
        self._coords = coords

    def __check_coords(self, coords):
        if not all(type(x) in self._allowed_types for x in coords):
            raise ValueError('неверный тип координат')

    @staticmethod
    def __is_vector(vector):
        if not isinstance(vector, Vector):
            raise TypeError('операнд должен быть объектом класса Vector или дочернего от него класса')

    def get_coords(self):
        return tuple(self._coords)

    def __check_vector_dims(self, other):
        if len(self._coords) != len(other.get_coords()):
            raise TypeError('размерности векторов не совпадают')

    def __make_vector(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        self.__is_vector(other)
        self.__check_vector_dims(other)
        coords = tuple(a + b for a,b in zip(self._coords, other.get_coords()))
        return self.__make_vector(coords)

    def __sub__(self, other):
        self.__is_vector(other)
        self.__check_vector_dims(other)
        coords = tuple(a - b for a,b in zip(self._coords, other.get_coords()))
        return self.__make_vector(coords)


class VectorInt(Vector):
    _allowed_types = (int,)
