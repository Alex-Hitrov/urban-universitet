import random

def string_info():
    global calls_into
    calls_into += 1
    a = len(string)
    b = string.upper()
    c = string.lower()
    d = (a, b, c)
    print(d)

def is_constant():
    global string, calls_constant, a
    list_to_search = []
    calls_constant += 1
    i = 0
    while i < a:
        if i > a:
            break
        else:
            b = ''.join(random.sample(string, len(string)))
            list_to_search.append(b)
            i += 1
            continue
    #print(list_to_search)
    if string in list_to_search:
        print(True)
    else:
        print(False)

def count_calls():
    global calls, calls_into, calls_constant
    calls = calls_into + calls_constant
    print(calls)




string = input('Введите слово: ')
number_info = int(input('Введите число повторов функции string_info: '))
number_constant = int(input('Введите число повторов функции is_constant: '))
calls = 0
calls_into = 0
calls_constant = 0
a = len(string) +1
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

















