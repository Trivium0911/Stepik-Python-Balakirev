"""
                            5.2 Обработка исключений. Блоки finally и else  4


Подвиг 4. В программе вводятся два значения в одну строчку через пробел. Значениями могут быть числа, слова, булевы
величины (True/False). Необходимо прочитать эти значения из входного потока. Если оба значения являются числами, то
вычислить их сумму, иначе соединить их в одну строку с помощью оператора + (конкатенации строк). Результат вывести
на экран (в блоке finally).

P.S. Реализовать программу с использованием блоков try/except/finally.

Sample Input:

8 11
Sample Output:

19
"""

n, m = input().split()
try:
    n, m = int(n), int(m)
except:
    try:
        n, m = float(n), float(m)
    except:
        try:
            n, m = str(n), str(m)
        except:
            ...
finally:
    print(n + m)
