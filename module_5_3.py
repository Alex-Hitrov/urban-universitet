class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number = int(number_of_floors)

    def __str__(self):
        return (f'Название: {self.name}, количество этажей:  {self.number}')

    def __eq__(self, other):
        return self.number == other.number

    def __add__(self, value):
        self.number = self.number + value
        return self

    def __iadd__(self, other):
        return self + other

    def __radd__(self, other):
       return self + other

    def __gt__(self, other):
        return self.number > other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __lt__(self, other):
        return self.number < other.number

    def __le__(self, other):
        return self.number <= other.number

    def __ne__(self, other):
        return self.number != other.number


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)