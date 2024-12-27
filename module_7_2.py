
def custom_write(file_name, strings):
    name = file_name
    number_str = 0
    total = {}
    with open(name, 'w',  encoding='UTF-8') as file:
        for i in strings:
            tell = file.tell()
            file.write(i)
            file.write('\n')
            number_str +=1
            total[(number_str, tell)] = i
    return total

#Пример выполняемого кода:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

#Вывод на консоль:
#((1, 0), 'Text for tell.')
#((2, 16), 'Используйте кодировку utf-8.')
#((3, 66), 'Because there are 2 languages!')
#((4, 98), 'Спасибо!')
