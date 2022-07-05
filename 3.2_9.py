"""
                                    3.2 Метод __call__. Функторы и классы-декораторы 9

Подвиг 9. Объявите класс-декоратор InputDigits для декорирования стандартной функции input так, чтобы при вводе строки
из целых чисел, записанных через пробел, например:

"12 -5 10 83"

на выходе возвращался список из целых чисел:

[12, -5, 10, 83]

Назовите декорированную функцию input_dg и вызовите ее командой:

res = input_dg()
P.S. На экран ничего выводить не нужно.

"""


class InputDigits:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        return [int(i) for i in self.__func().split()]


input_dg = InputDigits(input)
res = input_dg()
print(res)
