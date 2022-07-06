"""
                                3.3 Методы __str__, __repr__, __len__, __abs__ 8

Подвиг 8. Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса должны создаваться командой:

dt = DeltaClock(clock1, clock2)
где clock1, clock2 - объекты другого класса Clock для хранения текущего времени. Эти объекты должны создаваться
командой:

clock = Clock(hours, minutes, seconds)
где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные числа).

В классе Clock также должен быть (по крайней мере) один метод (возможны и другие):

get_time() - возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).

После создания объекта dt класса DeltaClock, с ним должны выполняться команды:

str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
Если разность получается отрицательной, то разницу времен считать нулевой.

Пример использования классов (эти строчки в программе писать не нужно):

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
Обратите внимание, добавляется незначащий ноль, если число меньше 10.

P.S. На экран ничего выводить не нужно, только объявить классы.

"""


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        lst = self.differ()
        if len([i for i in lst if i >= 0]) == 3:
            for i in range(len(lst)):
                if 0 <= lst[i] < 10:
                    lst[i] = "0" + str(lst[i])
            return f"{lst[0]}: {lst[1]}: {lst[2]}"
        return f"00: 00: 00"

    def __len__(self):
        lst = self.differ()
        return lst[0] * 3600 + lst[1] * 60 + lst[2]

    def differ(self):
        h = self.clock1.hours - self.clock2.hours
        m = self.clock1.minutes - self.clock2.minutes
        s = self.clock1.seconds - self.clock2.seconds
        return [h, m, s]


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        if self.check_val(self.hours) and self.check_val(self.minutes) and self.check_val(self.seconds):
            return self.hours * 3600 + self.minutes * 60 + self.seconds

    @staticmethod
    def check_val(val):
        return type(val) is int and val >= 0


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)
