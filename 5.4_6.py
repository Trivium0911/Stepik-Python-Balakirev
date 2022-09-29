"""
                        5.4 Инструкция raise и пользовательские исключения  6

Подвиг 6. Объявите класс DateString для представления дат, объекты которого создаются командой:

date = DateString(date_string)
где date_string - строка с датой в формате:

"DD.MM.YYYY"

здесь DD - день (целое число от 1 до 31); MM - месяц (целое число от 1 до 12); YYYY - год (целое число от 1 до 3000).
Например:

date = DateString("26.05.2022")
или

date = DateString("26.5.2022") # незначащий ноль может отсутствовать
Если указанная дата в строке записана неверно (не по формату), то генерировать исключение с помощью собственного класса:

DateError - класс-исключения, унаследованный от класса Exception.

В самом классе DateString переопределить магический метод __str__() для формирования строки даты в формате:

"DD.MM.YYYY"

(здесь должны фигурировать незначащие нули, например, для аргумента "26.5.2022" должна
формироваться строка "26.05.2022").

Далее, в программе выполняется считывание строки из входного потока командой:

date_string = input()
Ваша задача создать объект класса DateString с аргументом date_string и вывести объект на экран командой:

print(date) # date - объект класса DateString
Если же произошло исключение, то вывести сообщение (без кавычек):

"Неверный формат даты"

Sample Input:

1.2.1812
Sample Output:

01.02.1812
"""


class DateError(Exception):
    ...


class DateString:
    def __init__(self, date_string):
        if date_string:
            day, month, year = map(int, date_string.split('.'))
            if not (1 <= int(day) <= 31) or not (1 <= int(month) <= 12) or \
                    not (1 <= int(year) <= 3000):
                raise DateError("Неверный формат даты")

            self.day = day
            self.month = month
            self.year = year

    def __str__(self):
        return f'{self.day:02}.{self.month:02}.{self.year:04}'


date_string = input()

try:
    print(DateString(date_string))
except DateError as e:
    print(e)
