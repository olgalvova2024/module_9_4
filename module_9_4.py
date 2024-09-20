from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x,y: True if x == y else False, first, second)))

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        for i in data_set:
            file = open(file_name, 'a', encoding='utf-8')
            i = str(i)
            file.write(i)
            file.write('\n')
            file.close()

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *word):
        self.word = word
    def __call__(self, *word):
        return choice(self.word)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
