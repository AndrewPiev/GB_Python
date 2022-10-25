# 30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл users_hobby.txt. 

file_1 = open('users.txt', 'r', encoding='utf8')
content1 = file_1.read()
file_2 = open('hobby.txt', 'r', encoding='utf8')
content2 = file_2.read()
users = content1.splitlines()
hobbies = content2.splitlines()
users_hobbies = {}
for i in range (len(users)):
    users_hobbies [users[i]] = hobbies [i]

file_1.close()
file_2.close()

print (users_hobbies)

with open('users_hobby.txt','w', encoding='utf8') as out:
    for key,val in users_hobbies.items():
        out.write('{}:{}\n'.format(key,val))

print ('Словарь записан в файл users_hobby.txt')
