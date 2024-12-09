class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.new_floor = int(input('Введите нужный этаж: '))
        self.go_to(self.new_floor)

    def go_to(self, new_floor):
        if self.new_floor > self.number_of_floors or self.new_floor < 1:
            print("Такого этажа не существует")
        else:
            i = 1
            while i <= self.new_floor:
                print(i)
                i = i +1


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)