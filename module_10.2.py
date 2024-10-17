import time
from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.enemy_power = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemy_power > 0:
            self.enemy_power -= self.power
            self.days +=1
            time.sleep(1)
            print(f'{self.name} сражается {self.days} дней(дня), осталось {self.enemy_power} воинов')
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')



# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
