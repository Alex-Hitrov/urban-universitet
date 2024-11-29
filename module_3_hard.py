data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
a = 0


def list_cal(*args):
    global a
    for f in range(len(list_structure)):
        if isinstance(list_structure[f], str):
            a += len(list_structure[f])
        if isinstance(list_structure[f], int):
            a += list_structure[f]


def dict_cal(*args):
    global a
    dict_keys = list(dict_structure.keys())
    dict_values = list(dict_structure.values())
    for s in range(len(dict_keys)):
        if type(dict_keys[s]) == str:
            a += len(dict_keys[s])
            continue
        if type(dict_keys[s]) == int:
            a += dict_keys[s]
            continue
    for s in range(len(dict_values)):
        if type(dict_values[s]) == str:
            a += len(dict_values[s])
            continue
        if type(dict_values[s]) == int:
            a += dict_values[s]
            continue

def tuple_cal(*args):
    global a
    for d in range(len(tuple_structure)):
        if isinstance(tuple_structure[d], str):
            a += len(tuple_structure[d])
        if isinstance(tuple_structure[d], int):
            a += tuple_structure[d]
        if isinstance(tuple_structure[d], list):
            list_structure = tuple_structure[d]
            list_cal(list_structure)
        if isinstance(tuple_structure[d], dict):
            dict_structure = tuple_structure[d]
            dict_cal(dict_structure)
        #print(tuple_structure[d], type(tuple_structure[d]))




for i in range(len(data_structure)):
    print(data_structure[i], type(data_structure[i]))
    if isinstance(data_structure[i], str):
        a += len(data_structure[i])
    if isinstance(data_structure[i], int):
        a += data_structure[i]
    if isinstance(data_structure[i], list):
        list_structure = data_structure[i]
        list_cal(list_structure)
    if isinstance(data_structure[i], dict):
        dict_structure = data_structure[i]
        dict_cal(dict_structure)
    if isinstance(data_structure[i], tuple):
        tuple_structure = list(data_structure[i])
        tuple_cal(tuple_structure)

    print(a)





y = ((), [{(2, 'Urban', ('Urban2', 35))}])
print('y = ', y, type(y))
a  = 0
for i in range(len(y)):
    print('y[i] =', y[i])
    for j in range(len(y[i])):
        print('y[i][j] =',y[i][j])
        if isinstance(y[i][j], set):
            w = list(y[i][j])
            s = w[0]
            for i in range(len(s)):
                if isinstance(s[i], str):
                    a += len(s[i])
                if isinstance(s[i], int):
                    a += s[i]
                if isinstance(s[i], tuple):
                    s = s[i]
                    for i in range(len(s)):
                        if isinstance(s[i], str):
                            a += len(s[i])
                        if isinstance(s[i], int):
                            a += s[i]

        print(s, type(s))
print(a)
    
