"""
                                        4.6 Множественное наследование  4
Подвиг 4. С помощью множественного наследования удобно описывать принадлежность объектов к нескольким разным группам.
Выполним такой пример.

https://ucarecdn.com/741ba813-8581-4fc1-af56-725649404fe3/

Определите в программе классы в соответствии с их иерархией, представленной на рисунке выше:

Digit, Integer, Float, Positive, Negative

Каждый объект этих классов должен создаваться однотипной командой вида:

obj = Имя_класса(value)
где value - числовое значение. В каждом классе следует делать свою проверку на корректность значения value:

- в классе Digit: value - любое число;
- в классе Integer: value - целое число;
- в классе Float: value - вещественное число;
- в классе Positive: value - положительное число;
- в классе Negative: value - отрицательное число.

Если проверка не проходит, то генерируется исключение командой:

raise TypeError('значение не соответствует типу объекта')
После этого объявите следующие дочерние классы:

PrimeNumber - простые числа; наследуется от классов Integer и Positive;
FloatPositive - наследуется от классов Float и Positive.

Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с произвольными допустимыми для них
значениями. Сохраните все эти объекты в виде списка digits.

Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:

lst_positive - все объекты, относящиеся к классу Positive;
lst_float - все объекты, относящиеся к классу Float.

P.S. В программе требуется объявить только классы и создать списки. На экран выводить ничего не нужно."""


class Digit:
    def __init__(self, value):
        self._value = value

    def __setattr__(self, name, value):
        if not self._check_value(value):
            raise TypeError('значение не соответствует типу объекта')
        super().__setattr__(name, value)

    def _check_value(self, value):
        return type(value) in (int, float)


class Integer(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and type(value) is int


class Float(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and type(value) is float


class Positive(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and value > 0


class Negative(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and value < 0


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(1), PrimeNumber(2), PrimeNumber(3),
          FloatPositive(1.2), FloatPositive(1.3), FloatPositive(1.4),
          FloatPositive(1.5), FloatPositive(1.6)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
