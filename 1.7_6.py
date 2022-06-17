"""


"""


class Viber:
    msges = []

    def add_message(msg):
        self.msges.append(msg)

    def remove_message(msg):
        self.msges.remove(msg)

    def set_like(msg):
        self.msges[self.msges.index(msg)].fl_like = True

    def show_last_message(num):
        print(self.msges[-num:])

    def total_messages():
        return len(msges)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)