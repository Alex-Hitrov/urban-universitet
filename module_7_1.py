from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        self. name = name # str - название продукта
        self.weight = weight # float - общий вес товара
        self.category = category # str - категория товара

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop(Product):

    def __init__(self, name, weight, category):
        super().__init__(name, weight, category)
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        st = file.read()
        file.close()
        print(f'{st}')

    def add(self, *products):
        for i in products:
            goods = (str(i))
            a = goods.split(',')
            file = open(self.__file_name, 'r')
            f_read = file.read()
            file.close()
            if goods in f_read:
                print(f'Продукт {a[0]} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{goods}')
                file.close()

#Пример работы программы:
s1 = Shop(str, float, str)
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())

#Вывод на консоль:
#Первый запуск:
#Spaghetti, 3.4, Groceries
#Potato, 50.5, Vegetables
#Spaghetti, 3.4, Groceries
#Potato, 5.5, Vegetables

#Второй запуск:
#Spaghetti, 3.4, Groceries
#Продукт Potato уже есть в магазине
#Продукт Spaghetti уже есть в магазине
#Продукт Potato уже есть в магазине
#Potato, 50.5, Vegetables
#Spaghetti, 3.4, Groceries
#Potato, 5.5, Vegetables