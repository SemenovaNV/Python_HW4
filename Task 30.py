# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. 
# Известно, что при хранении данных используется принцип: одна строка — один пользователь. 
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: 
# ключи — ФИО, значения — данные о хобби.

# Сохранить словарь в файл users_hobby.txt. 
# Фрагмент файла с данными о пользователях (users.txt):
# Фрагмент файла с данными о хобби (hobby.txt):

# user = '/D:\Hidden\Desktop\Python\HW 4\user.txt'
# hobby = '/HW 4\hobby.txt'
user = open('user.txt', 'r', encoding='utf8')
keys = user.read().split('\n')
print(keys)

hobby = open('hobby.txt', 'r', encoding='utf8')
values = hobby.read().split('\n')
print(values)

dictionary = dict(zip(keys, values))
print(dictionary)

with open('test.txt', 'w') as out:
    for key, val in dictionary.items():
        out.write('{}: {}\n'.format(key, val))


