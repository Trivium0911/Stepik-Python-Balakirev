"""
                            3.5 Сравнения __eq__, __ne__, __lt__, __gt__ и другие 9

body = Body(name, ro, volume)
где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное); volume - объем тела
(число: вещественное или целочисленное).

Для объектов класса Body должны быть реализованы операторы сравнения:

body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5
Масса тела вычисляется по формуле:

m = ro * volume

P.S. В программе только объявить класс, выводить на экран ничего не нужно.

"""


class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.m = self.ro * self.volume

    @staticmethod
    def _get_value(val):
        if type(val) not in (Body, int, float):
            raise ValueError('Type must been int, float or Body.')
        if type(val) is Body:
            return val.m
        return val

    def __eq__(self, other):
        return self.m == self._get_value(other)

    def __lt__(self, other):
        return self.m < self._get_value(other)

    def __gt__(self, other):
        return self.m > self._get_value(other)





