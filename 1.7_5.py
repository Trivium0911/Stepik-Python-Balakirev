"""
                        1.7 Методы класса (classmethod) и статические методы (staticmethod) 5

Подвиг 10 (на повторение). Объявите класс AppStore - интернет-магазин приложений для устройств под iOS. В этом классе должны быть реализованы следующие методы:

add_application(self, app) - добавление нового приложения app в магазин;
remove_application(self, app) - удаление приложения app из магазина;
block_application(self, app) - блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);
total_apps(self) - возвращает общее число приложений в магазине.

Класс AppStore предполагается использовать следующим образом (эти строчки в программе не писать):

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
Здесь Application - класс, описывающий добавляемое приложение с указанным именем. Каждый объект класса Application должен содержать локальные свойства:

name - наименование приложения (строка);
blocked - булево значение (True - приложение заблокировано; False - не заблокировано, изначально False).

Как хранить список приложений в объектах класса AppStore решите сами.

P.S. В программе нужно только объявить классы с указанным функционалом.



"""


class Viber:
    msges = []

    @classmethod
    def add_message(cls, msg):
        cls.msges.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.msges.remove(msg)

    @classmethod
    def set_like(cls, msg):
        cls.msges[cls.msges.index(msg)].fl_like = True

    @classmethod
    def show_last_message(cls, num):
        print(cls.msges[-num:])

    @classmethod
    def total_messages(cls):
        return len(cls.msges)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


