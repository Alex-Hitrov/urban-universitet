import threading
from itertools import count
from time import sleep
from random import  randint

balance = 0
lock = threading.Lock()

class Bank(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def deposit(self):
        global balance
        for i in range(100):
            a = randint(50, 500)
            balance += a
            print(f'\nОперация пополнения № {i+1}')
            print(f'Пополнение: {a}. Баланс: {balance}')
            if balance > 500 and lock.locked() is True:
                lock.release()
            sleep(0.001)

    def take(self):
        global balance
        for i in range(100):
            a = randint(50, 500)
            print(f'\nОперация снятия № {i+1}')
            print(f'Запрос на {a}')
            if a <= balance:
                balance -= a
                print(f'Снятие: {a}. Баланс: {balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                lock.acquire()



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {balance}')
