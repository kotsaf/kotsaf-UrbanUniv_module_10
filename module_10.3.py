import random
import time
from threading import Thread, Lock

class Bank(Thread):

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            add_m = random.randint(50, 501)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += add_m
            print(f'Пополнение: {add_m}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            take_m = random.randint(50, 501)
            print(f'Запрос на {take_m}')
            if take_m <= self.balance:
                self.balance -= take_m
                print(f'Снятие: {take_m}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)



bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
