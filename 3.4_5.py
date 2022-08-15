"""
                                3.4 Методы __add__, __sub__, __mul__, __truediv__ 5

Подвиг 5. Объявите класс с именем ListMath, объекты которого можно создавать командами:

lst1 = ListMath() # пустой список
lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
В качестве значений элементов списка объекты класса ListMath должны отбирать только целые и вещественные числа,
остальные игнорировать (если указываются в списке). Например:

coords = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
В каждом объекте класса ListMath должен быть публичный атрибут:

lst_math - ссылка на текущий список объекта (для каждого объекта создается свой список).

Также с объектами класса ListMath должны работать следующие операторы:

coords = coords + 76 # сложение каждого числа списка с определенным числом
coords = 6.5 + coords # сложение каждого числа списка с определенным числом
coords += 76.7  # сложение каждого числа списка с определенным числом
coords = coords - 76 # вычитание из каждого числа списка определенного числа
coords = 7.0 - coords # вычитание из числа каждого числа списка
coords -= 76.3
coords = coords * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
coords = 5 * coords # умножение каждого числа списка на указанное число (в данном случае на 5)
coords *= 5.54
coords = coords / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
coords = 3 / coords # деление числа на каждый элемент списка
coords /= 13.0
При использовании бинарных операторов +, -, *, / должны формироваться новые объекты класса ListMath с новыми списками,
прежние списки не меняются.

При использовании операторов +=, -=, *=, /= значения должны меняться внутри списка текущего объекта (новый объект не
создается).

P.S. В программе достаточно только объявить класс. На экран ничего выводить не нужно.

"""


class ListMath:
    def __init__(self, lst_math=None):
        self.lst_math = [i for i in lst_math if type(i) in (int, float)] if lst_math and type(lst_math) is list else []

    def get_list(self):
        return self.lst_math

    @staticmethod
    def __veryfy_val(val):
        if type(val) not in (int, float):
            raise ArithmeticError("Type must been int, float or ListMath")

    def __add__(self, other):
        self.__veryfy_val(other)
        return ListMath([int(i) + other for i in self.lst_math])

    def __radd__(self,other):
        return self + other

    def __sub__(self, other):
        self.__veryfy_val(other)
        return ListMath([i - other for i in self.lst_math])

    def __rsub__(self, other):
        return ListMath([other - i for i in self.lst_math])

    def __mul__(self, other):
        self.__veryfy_val(other)
        return ListMath([i * other for i in self.lst_math])

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        self.__veryfy_val(other)
        return ListMath([i / other for i in self.lst_math])

    def __rtruediv__(self, other):
        return ListMath([other / i for i in self.lst_math])

    def __iadd__(self, other):
        self.__veryfy_val(other)
        self.lst_math = [i + other for i in self.lst_math]
        return self

    def __isub__(self, other):
        self.__veryfy_val(other)
        self.lst_math = [i - other for i in self.lst_math]
        return self

    def __imul__(self, other):
        self.__veryfy_val(other)
        self.lst_math = [i * other for i in self.lst_math]
        return self

    def __itruediv__(self, other):
        self.__veryfy_val(other)
        self.lst_math = [i / other for i in self.lst_math]
        return self


lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
lst = lst + 76 # сложение каждого числа списка с определенным числом
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0