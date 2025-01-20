import time
import datetime
import threading



def wite_words(*args):
    word_count, file_name = args
    with open(file_name, 'a', encoding = 'utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово №{i+1}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

started_at = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
ended_at = time.time()
time_format = str(datetime.timedelta(seconds = ended_at - started_at))
print(f'Работа функций {time_format}')


thread = threading.Thread(target = wite_words, args = (10, 'example5.txt'))
thread1 = threading.Thread(target = wite_words, args = (30, 'example6.txt'))
thread2 = threading.Thread(target = wite_words, args = (200, 'example7.txt'))
thread3 = threading.Thread(target = wite_words, args = (100, 'example8.txt'))
started_at = time.time()
thread.start()
thread1.start()
thread2.start()
thread3.start()
thread.join()
thread1.join()
thread2.join()
thread3.join()
ended_at = time.time()
time_format = str(datetime.timedelta(seconds = ended_at - started_at))
print(f'Работа потоков {time_format}')
