"""
                                5.4 Инструкция raise и пользовательские исключения 4

Подвиг 4. Объявите класс-исключение с именем StringException, унаследованным от базового класса Exception. После этого
объявите еще два класса-исключения:

NegativeLengthString - ошибка, если длина отрицательная;
ExceedLengthString - ошибка, если длина превышает заданное значение;

унаследованные от базового класса StringException.

Затем, в блоке try (см. программу) пропишите команду генерации исключения для перехода в блок обработки исключения
ExceedLengthString.
"""


class StringException(Exception):
    ...


class NegativeLengthString(StringException):
    ...


class ExceedLengthString(StringException):
    ...


try:
    raise ExceedLengthString()
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")
