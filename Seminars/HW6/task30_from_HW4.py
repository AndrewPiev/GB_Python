# 30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл users_hobby.txt. 

with open('users.txt','r', encoding='utf8') as out1, open('hobby.txt','r', encoding='utf8') as out2, open('users_hobby.txt','w', encoding='utf8') as in1:
    users = [line.rstrip() for line in out1]
    hobbies = [line.rstrip() for line in out2]
    users_hobbies = (dict(zip(users,hobbies)))
    print (users_hobbies)
    for key,val in users_hobbies.items():
        in1.write('{}:{}\n'.format(key,val))


