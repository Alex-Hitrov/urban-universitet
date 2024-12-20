import random
class Animal:
    live = True
    sound = None #звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0 #степень опасности существа

    def __init__(self, _cords, speed):
        self._cords = [0, 0, 0] #координаты в пространстве
        self.speed = speed #скорость передвижения существа

    def move(self, x, y, z):
        self._cords1 = [x, y, z]
        self.dx = x * self.speed
        self.dy = y * self.speed
        self.dz = z * self.speed
        if self.dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [self.dx, self.dy, self.dz]

    def get_cords(self):
        print(f'X: {self.dx}, Y: {self.dy}, Z: {self.dz}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal): #птицы
    beak = True #наличие клюва

    def lay_eggs(self):
        print(f'Here are(is)', random.randrange(1, 4), ' eggs for you')

class AquaticAnimal(Animal): #плавающее животное
    _DEGREE_OF_DANGER = 3

    def __init__(self):
        super().__init__(self._cords1, self._cords)


    def dive_in(self, speed):
        self.speed = speed
        self.dz = int(abs(self._cords1[2] - self.speed/2))
        self._cords = [self.dx, self.dy, self.dz]

class PoisonousAnimal(Animal): # ядовитые животные
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal): # утконос
    sound = "Click-click-click" #звук, который издаёт утконос

    def __init__(self, speed):
        self.speed = speed
        self._DEGREE_OF_DANGER = super()._DEGREE_OF_DANGER

db = Duckbill(10)

print(db.live)
print(db.beak)
db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
