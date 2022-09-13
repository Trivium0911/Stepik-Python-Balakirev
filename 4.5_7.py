"""
                                    4.5 Полиморфизм и абстрактные методы  7

Подвиг 7. Используя информацию о модуле abc из предыдущего подвига 6, объявите базовый класс с именем StackInterface
со следующими абстрактными методами:

def push_back(self, obj) - добавление объекта в конец стека;
def pop_back(self) - удаление последнего объекта из стека.

https://ucarecdn.com/1326f685-df54-4c2b-b798-b288d22cdeec/

На основе этого класса объявите дочерний класс с именем Stack. Объекты этого класса должны создаваться командой:

st = Stack()
и в каждом объекте этого класса должен формироваться локальный атрибут:

_top - ссылка на первый объект стека (для пустого стека _top = None).

В самом классе Stack переопределить абстрактные методы базового класса:

def push_back(self, obj) - добавление объекта в конец стека;
def pop_back(self) - удаление последнего объекта из стека.

Сами объекты стека должны определяться классом StackObj и создаваться командой:

obj = StackObj(data)
где data - информация, хранящаяся в объекте (строка). В каждом объекте класса StackObj должны автоматически
формироваться атрибуты:

_data - информация, хранящаяся в объекте (строка);
_next - ссылка на следующий объект стека (если следующий отсутствует, то _next = None).

Пример использования классов (эти строчки в программе писать не нужно):

st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""


from abc import ABC, abstractmethod


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value


class StackInterface(ABC):

    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def __iter__(self):
        h = self._top
        while h:
            yield h
            h = h.next

    def push_back(self, obj):
        if not self._top:
            self._top = obj
            return
        *_, last = self
        last.next = obj

    def pop_back(self):
        if not self._top:
            return None
        if not self._top.next:
            obj = self._top
            self._top = None
            return obj
        *_, p_last, last = self
        p_last.next = None
        return last


st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)