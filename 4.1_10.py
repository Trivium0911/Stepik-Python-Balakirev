"""



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
