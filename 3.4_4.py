"""
                            3.4 Методы __add__, __sub__, __mul__, __truediv__ 4

Подвиг 4. Известно, что в Python мы можем соединять два списка между собой с помощью оператора +:

coords = [1, 2, 3] + [4.5, -3.6, 0.78]
Но нет реализации оператора -, который бы убирал из списка все значения вычитаемого списка:

coords = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования оставшихся элементов списка должен
сохраняться)
Давайте это поправим и создадим такой функционал. Для этого нужно объявить класс с именем NewList, объекты которого
создаются командами:

coords = NewList() # пустой список
coords = NewList([-1, 0, 7.56, True]) # список с начальными значениями
Реализуйте для этого класса работу с оператором вычитания, чтобы над объектами класса NewList можно было выполнять
следующие действия:

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
Также в классе NewList необходимо объявить метод:

get_list() - для возвращения результирующего списка объекта класса NewList

Например:

coords = res_2.get_list() # [1, 2, 3]
P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно.

"""


class NewList:
    def __init__(self, lst=None):
        self._lst = lst[:] if lst and type(lst) == list else []

    def get_list(self):
        return self._lst

    @staticmethod
    def __diff_list(lst1, lst2):
        if len(lst2) == 0:
            return lst1
        sub = lst2[:]
        return [i for i in lst1 if not NewList.__is_elem(i, sub)]

    @staticmethod
    def __is_elem(x, sub):
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res

    def __sub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError("Type must been list or NewList")
        other_list = other if type(other) is list else other.get_list()
        return NewList(self.__diff_list(self._lst, other_list))

    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError("Type must been list or NewList")
        return NewList(self.__diff_list(other, self._lst))


lst = NewList() # пустой список
lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями
lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]