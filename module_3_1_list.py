import random

def string_info():
    global calls_into
    string = input('Введите слово для преобразования: ')
    calls_into += 1
    a = len(string)
    b = string.upper()
    c = string.lower()
    d = (a, b, c)
    print(d)

def is_constant():
    global calls_constant
    string = input('Введите слово для поиска в списке: ')
    list_to_search = input('Введите через запятую список слов: ')
    calls_constant += 1
    a = string.lower()
    b = list_to_search.lower()
    if a in b:
        print(True)
    else:
        print(False)

def count_calls():
    global calls, calls_into, calls_constant
    calls = calls_into + calls_constant
    print(calls)


number_info = int(input('Введите число повторов функции string_info для преобразования слова: '))
number_constant = int(input('Введите число повторов функции is_constant для поиска слова в списке: '))
calls = 0
calls_into = 0
calls_constant = 0
i = 1
j = 1
while i <= number_info:
    if i > number_info:
        break
    else:
        string_info()
        i += 1
while j <= number_constant:
    if j > number_constant:
        break
    else:
        is_constant()
        j += 1
count_calls()