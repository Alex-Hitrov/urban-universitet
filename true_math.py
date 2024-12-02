from math import inf
def divide(first, second):
    try:
        result = first / second
    except ZeroDivisionError as zde:
        result = inf


    print(result)

