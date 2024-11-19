def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = (8, 'sommer', True)
values_direct = {'a' : 'winter', 'b' : [1,2,3], 'c' : 8}
values_list_2 = [54.32, 'Строка' ]

print_params()
print_params(b = 25, c = [1,2,3])
print_params(*values_list)
print_params(**values_direct)
print_params(*values_list_2, 42)