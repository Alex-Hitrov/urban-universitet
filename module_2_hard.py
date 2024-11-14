namber = int(input('Введите число c 3 до 20: '))
sum = 0
insert = []
for i in range(1, 20):
    for j in range(1, 20):
        sum = i+j
        if namber >= sum and i != j and j!=1 and namber % sum == 0:
            if j not in insert:
                insert.append(i)
                insert.append(j)
print(namber, '-', *insert)