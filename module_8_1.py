def add_everything_up(a, b):
    try:
        print(round(a + b, 3))
    except TypeError:
        print(str(a), str(b))



add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)