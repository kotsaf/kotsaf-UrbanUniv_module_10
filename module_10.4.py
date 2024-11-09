from threading import Thread
import time
import random
from queue import Queue


class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randrange(3, 10))


class Cafe:

    def __init__(self, *tables):
        self.tables = set(tables)
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            seat = False
            for stol in self.tables:
                if stol.guest == None:
                    stol.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {stol.number}')
                    seat = True
                    break
            if not seat:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guest(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for stol in self.tables:
                if stol.guest is not None:
                    if not stol.guest.is_alive():
                        print(f"{stol.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {stol.number} свободен")
                        stol.guest = None

                if not self.queue.empty():
                    if stol.guest is None:
                        guest_2 = self.queue.get()
                        stol.guest = guest_2
                        guest_2.start()
                        print(f'{guest_2.name} вышел(-ла) из очереди и сел(-а) за стол номер {stol.number}')


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guest()
