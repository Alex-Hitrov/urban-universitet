result = 0
incorrect_data = 0
num = []

def personal_sum(numbers):
    global result, num, incorrect_data
    num = []
    result = 0
    for i in range(len(numbers)):
        try:
            if type(numbers[i]) is int:
                num.append(numbers[i])
            elif type(numbers[i]) is str:
                print('Некорректный тип данных для подсчёта суммы - ', numbers[i])
        except TypeError as exc:
            print('Некорректный тип данных для подсчёта суммы')
            i += 1
    numbers = num
    for i in range(len(numbers)):
        result += numbers[i]

def calculate_average(numbers):
    global result, incorrect_data, num
    try:
        personal_sum(numbers)
        if result == 0:
            return result
        else:
            return result/len(num)
    except TypeError as exc:
        print('В numbers записан некорректный тип данных')
    except ZeroDivisionError as exc:
        incorrect_data += 1


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
