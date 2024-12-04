data_structure = [ [1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}]) ]

def calculate_structure_sum(data_structure):
    summa = 0
    if isinstance(data_structure, int):
        summa += data_structure
    if isinstance(data_structure, str):
        summa += len(data_structure)
    if isinstance(data_structure, list):
        for i in data_structure:
            summa += calculate_structure_sum(i)
    if isinstance(data_structure, tuple):
        for i in data_structure:
            summa += calculate_structure_sum(i)
    if isinstance(data_structure, set):
        for i in data_structure:
            summa += calculate_structure_sum(i)
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
    return summa



result = calculate_structure_sum(data_structure)
print(result)
