class Figure:
    sides_count = 0
    __sides = [] #список сторон (целые числа)
    __color = []  #список цветов в формате RGB
    filled = False

    def __init__(self, rgb, *side):
        self.color = list(rgb)
        self.side = side[0]
        self.side3 = side
        self.filled = True #закрашенный

    def get_color(self):
        self.__color = self.color
        self.filled = True
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.color = [self.r, self.g, self.b]
            __color = self.color

    def __is_valid_sides(self, *args):
        ar = args
        if len(ar) > 1:
            for i in ar:
                if len(ar) == self.sides_count and i > 0 and type(i) == int:
                    return True
                else:
                    return False
        else:
            if self.sides_count == 1 and self.side > 0 and type(self.side) == int:
                return True
            else:
                return False

    def get_sides(self):
        self.__sides = self.side3
        return self.__sides

    def __len__(self):
        if self.sides_count == 3:
            self.sum_t = sum(self.side3)
            return sum(self.side3)
        else:
            return self.side3[0] * self.sides_count

    def set_sides(self, *args):
        new_sides = []
        self.side_new = list(args)
        if self.__is_valid_sides(args) is True:
            self.side3 = self.side_new
            self.get_sides()
        else:
            if len(self.side3) == 1:
                if self.sides_count == 3 or self.sides_count == 12:
                    for i in range(self.sides_count):
                        new_sides.append(self.side3[0])
                    self.side3 = new_sides
                    self.__sides = new_sides
                    self.get_sides()
            else:
                for i in range(self.sides_count):
                    new_sides.append(1)
                self.side3 = new_sides
                self.__sides = new_sides
                self.get_sides()

class Circle(Figure):
    sides_count = 1
    __radius = 0

    def radius(self):
        self.__radius = round(self.side3[0]/(2*3.14), 2)
        return self.__radius

    def get_square(self):
        self.radius()
        return (self.__radius**2)*3,14

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        self.__len__()
        a, b, c = self.side3
        p = (a + b + c)/ 2
        return (p * (p - a) * (p - b) * (p - c))**0.5

class Cube (Figure):
    sides_count = 12

    def get_volume(self):
        return self.side ** 3

#Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка треугольника
#triangle1 = Triangle((200, 115, 18), 13, 15, 14)
#print(len(triangle1)) # проверка периметра
#triangle1.set_sides(15, 12) # проверка изменения сторон
#print(triangle1.get_sides())
#print(triangle1.get_square()) # проверка площади

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
#print(circle1.get_square()) # проверка площади круга

# Проверка объёма (куба):
print(cube1.get_volume())