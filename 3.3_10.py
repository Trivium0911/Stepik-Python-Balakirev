"""
                                3.3 Методы __str__, __repr__, __len__, __abs__ 10
10 из 11 шагов пройдено
26 из 29 баллов  получено
Подвиг 10 (на повторение). Объявите класс PolyLine (полилиния) для представления линии из последовательности
прямолинейных сегментов. Объекты этого класса должны создаваться командой:

poly = PolyLine(start_coord, coord_2, coord_3, ..., coord_N)
Здесь start_coord - координата начала полилинии (кортеж из двух чисел x, y); coord_2, coord_3, ... - последующие
координаты точек на плоскости (представленные кортежами), соединенных прямыми линиями.

Например:

poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))

https://ucarecdn.com/e1216ffb-6a6d-4213-a7b6-4aba5600d9d1/

В классе PolyLine должны быть объявлены следующие методы:

add_coord(x, y) - добавление новой координаты (в конец);
remove_coord(indx) - удаление координаты по индексу (порядковому номеру, начинается с нуля);
get_coords() - получение списка координат (в виде списка из кортежей).

P.S. На экран ничего выводить не нужно, только объявить класс.

"""


class PolyLine:
    def __init__(self, start_coord, *args):
        self.coords = [start_coord]
        if args:
            self.coords = self.coords + list(args)

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        self.coords.remove(self.coords[indx])

    def get_coords(self):
        return self.coords


p = PolyLine((1,0))
pt = PolyLine((1,2), (3,4))
pt.add_coord(4,5)
print(pt.get_coords())
