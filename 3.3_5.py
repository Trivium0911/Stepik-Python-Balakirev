"""
                            3.3 Методы __str__, __repr__, __len__, __abs__ 5

Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:

https://ucarecdn.com/bcf85c84-405f-4d53-a494-156db39a123f/

Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:

obj = ObjList(data)
где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие
локальные атрибуты:

__data - ссылка на строку с данными;
__prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
__next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).

В свою очередь, объекты класса LinkedList должны создаваться командой:

linked_lst = LinkedList()
и содержать локальные атрибуты:

head - ссылка на первый объект связного списка (если список пуст, то head = None);
tail - ссылка на последний объект связного списка (если список пуст, то tail = None).

А сам класс содержать следующие методы:

add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс
отсчитывается с нуля.

Также с объектами класса LinkedList должны поддерживаться следующие операции:

len(linked_lst) - возвращает число объектов в связном списке;
linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx
(в связном списке).

Пример использования классов (эти строчки в программе писать не нужно):

linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev
P.S. На экран в программе ничего выводить не нужно.

"""


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.linked_lst = []
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        obj.prev = self.tail
        if self.tail:
            self.tail.next = obj
        self.tail = obj
        if not self.head:
            self.head = obj

    def _get_obj_by_index(self, indx):
        x = self.head
        n = 0
        while x and n < indx:
            x = x.next
            n += 1
        return x

    def remove_obj(self, indx):
        obj = self._get_obj_by_index(indx)
        if obj is None:
            return
        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p
        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p

    def __len__(self):
        n = 0
        h = self.head
        while h:
            n += 1
            h = h.next
        return n

    def __call__(self, indx, *args, **kwargs):
        obj = self._get_obj_by_index(indx)
        return obj.data if obj else None
class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is str:
            self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__next = obj

