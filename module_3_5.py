def get_multiplied_digits(number = int(input('Введите целое число больше 9: '))):
    number_list = []
    result = 1
    str_number = str(number)
    a = 0
    b = int(str_number[a])
    if len(str_number) == 1:
        print('Ошибка ввода числа. Введите число больше 9')
    else:
        for i in range(len(str_number)):
            b = int(str_number[a])
            if b > 0:
                number_list.append(b)
                a += 1
                continue
            if b == 0:
                a += 1
                continue
        #print(number_list)
        for c in number_list:
            result *= c
        print(result)

get_multiplied_digits()
get_multiplied_digits(4223)
get_multiplied_digits(7)