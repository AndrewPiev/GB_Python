import csv
import controller

# Приветствие
with open('base_rows.csv', 'r', encoding='utf-8') as f:
    print()
    print ('Вы находитесь в телефонном справочнике предприятия')
    file_reader = csv.reader(f, delimiter = ",")
    count = 0
    for row in file_reader:
        if count ==0:
            print(f'Файл содержит столбцы: {" / ".join(row)}')           
        if count == 1:
            first_id = row [0]
        count +=1
        last_id = row[0]
    print(f'Всего записей в справочнике: {count-1}')
    print()
    print('Краткие правила пользования справочником при поиске и внесении информации:')
    print(f' - Фамилия и имя пишутся с большой буквы\n - Отдел и хобби пишутся с маленькой буквы\n - Для поиска по дате рождения желательно использовать только год\n - Номера телефонов в базе начинаются с префикса +7\n - ID в базе не повторяются, начинаются с {first_id} и заканчиваются на {last_id}')
    print()

controller.execution()