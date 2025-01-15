def is_prime(func):
    def wrapper(*args, **kwargs):
        num = func(*args)
        for i in range(2, (num // 2) + 1):
            if (num % i) == 0:
                print('Составное число')
                return num
                break
        else:
            print('Простое число')
            return num
    return wrapper

@is_prime
def sum_three(*args):
    a, b, c = args
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

