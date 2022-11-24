import random

second_names = ['Иванов', 'Петров', 'Сидоров', 'Орлов', 'Потемкин', 'Попов', 'Андреев', 'Семенов', 'Сергеев', 'Синицын', 'Голубев']
first_names = ['Иван', 'Петр', 'Андрей','Михаил','Сергей', 'Вячеслав', 'Аркадий', 'Николай']
hobby = ['футбол', 'саморазвитие', 'рыбалка', 'авто', 'путешествия', 'музеи', 'баня', 'театры', 'прочее']
depart = ['дирекция', 'бухгалтерия', 'кадры', 'маректинг', 'продажи', 'сервис', 'логистика', 'снабжение', 'юристы']

f = open('base_rows.txt', 'w')
f.close()

with open ('base_rows.txt', 'a', encoding='utf-8') as file:
    file.writelines ('id,Фамилия,Имя,Отдел,Телефон,Дата_рождения,Хобби\n')
    for i in range (120):
        file.writelines(f'{i+1},{random.choice(second_names)},{random.choice(first_names)},{random.choice(depart)},+79{str(random.randrange(100000000, 999999999))},{random.randrange(1,29)}-{random.randrange(1,13)}-{random.randrange(1960,2000)},{random.choice(hobby)}\n')

f = open('base_cols.txt', 'w')
f.close()

with open ('base_cols.txt', 'a', encoding='utf-8') as file:
    for i in range (120):
        file.writelines(f'{i+1}\n')
        file.writelines(f'{random.choice(second_names)}\n')
        file.writelines(f'{random.choice(first_names)}\n')
        file.writelines(f'{random.choice(depart)}\n')
        file.writelines(f'+79{str(random.randrange(100000000, 999999999))}\n')
        file.writelines(f'{random.randrange(1,29)}-{random.randrange(1,13)}-{random.randrange(1960,2000)}\n')
        file.writelines(f'{random.choice(hobby)}\n')

f = open('base_cols.xml', 'w')
f.close()

with open ('base_cols.xml', 'a', encoding='utf-8') as file:
    for i in range (120):
        file.writelines(f'{i+1}\n')
        file.writelines(f'{random.choice(second_names)}\n')
        file.writelines(f'{random.choice(first_names)}\n')
        file.writelines(f'{random.choice(depart)}\n')
        file.writelines(f'+79{str(random.randrange(100000000, 999999999))}\n')
        file.writelines(f'{random.randrange(1,29)}-{random.randrange(1,13)}-{random.randrange(1960,2000)}\n')
        file.writelines(f'{random.choice(hobby)}\n')

f = open('base_rows.xml', 'w')
f.close()

with open ('base_rows.xml', 'a', encoding='utf-8') as file:
    file.writelines ('id,Фамилия,Имя,Отдел,Телефон,Дата_рождения,Хобби\n')
    for i in range (120):
        file.writelines(f'{i+1},{random.choice(second_names)},{random.choice(first_names)},{random.choice(depart)},+79{str(random.randrange(100000000, 999999999))},{random.randrange(1,29)}-{random.randrange(1,13)}-{random.randrange(1960,2000)},{random.choice(hobby)}\n')

f = open('base_rows.csv', 'w')
f.close()

with open ('base_rows.csv', 'a', encoding='utf-8') as file:
    file.writelines ('id,Фамилия,Имя,Отдел,Телефон,Дата_рождения,Хобби\n')
    for i in range (120):
        file.writelines(f'{i+1},{random.choice(second_names)},{random.choice(first_names)},{random.choice(depart)},+79{str(random.randrange(100000000, 999999999))},{random.randrange(1,29)}-{random.randrange(1,13)}-{random.randrange(1960,2000)},{random.choice(hobby)}\n')