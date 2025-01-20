import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        day = 0
        for i in range(enemy):
            if enemy > 0:
                enemy -= self.power
                time.sleep(1)
                day += 1
                print(f'{self.name} сражается {day}, осталось {enemy} воинов.')
                continue
            else:
                print(f'{self.name} одержал победу спустя {day}) дней(дня)!')
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')