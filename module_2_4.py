numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] > 2 and numbers[i] % 2 == 0:
            not_primes.append(int(numbers[i]))
            break
        elif numbers[i] > 3 and numbers[i] % 3 == 0:
            not_primes.append(int(numbers[i]))
            break
        elif numbers[i] > 1 and numbers[i] % numbers[j] == 0:
            primes.append(int(numbers[i]))
            break
        elif numbers[i] > 1 and numbers[i] / numbers[j] != True:
            not_primes.append(int(numbers[i]))
            break
print('Primers: ', primes)
print('Not Primers: ', not_primes)