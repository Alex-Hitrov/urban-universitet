class WordsFinder:
    def __init__(self, *name):
        self.file_name = name
        self.line = []
        self.all_words = {}

    def get_all_words(self):
        for i in self.file_name:
            with open(i, encoding='utf-8') as file:
                file = ''.join(file)
                file = str(file.lower())
                file = file.replace('\n', ' ')
                file = file.replace(', ', ' ')
                file = file.replace('. ', ' ')
                file = file.replace('=', '')
                file = file.replace('!', '')
                file = file.replace('?', '')
                file = file.replace(';', '')
                file = file.replace(':', '')
                file = file.replace(' - ', ' ')
                self.all_words.update({i: file.split()})
        return  self.all_words

    def find(self, word):
        self.get_all_words()
        word = word.lower()
        for name, words in self.all_words.items():
            print({name: words.index(word)+1})

    def count(self, word):
        self.get_all_words()
        word = word.lower()
        for name, words in self.all_words.items():
            count_w = words.count(word)
            print({name: count_w})

#Пример результата выполнения программы:
#Представим, что файл 'test_file.txt' содержит следующий текст:
#It's a text for task Найти везде,
#Используйте его для самопроверки.
#Успехов в решении задачи!
#text text text

#Пример выполнения программы:
finder2 = WordsFinder('test_file.txt', 'products.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

#Вывод на консоль:
#{'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
#{'test_file.txt': 3}
#{'test_file.txt': 4}