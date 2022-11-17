import csv

# Вывод
# with open('base_rows.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# Приветствие
# with open('base_rows.csv', 'r', encoding='utf-8') as f:
#     print()
#     print ('Вы находитесь в телефонном справочнике нашего предприятия')
#     file_reader = csv.reader(f, delimiter = ",")
#     count = 0
#     for row in file_reader:
#         if count ==0:
#             print(f'Файл содержит столбцы: {" / ".join(row)}')
#         count +=1
#     max_id = count-1
#     print(f'Всего записей в справочнике: {max_id}')
#     print()
#     print('Краткие правила пользования справочником при поиске и внесении информации:')
#     print(f'Фамилия и имя пишутся с большой буквы\nОтдел и хобби пишутся с маленькой буквы\nДля поиска по дате рождения желательно использовать только год\nНомера телефонов в базе начинаются с префикса +7\nID в базе не повторяются, начинаются с 1 и заканчиваются на {max_id}')
#     print()


# Поиск
# with open('base_rows.csv', 'r', encoding='utf-8') as f:
#     file_reader = csv.reader(f, delimiter = ",")
#     count = 0
#     search_row = int(input('Введите параметр для поиска: 0 - id, 1 - Фамилия, 2 - Имя, 3- Отдел, 4- Телефон,5 - Дата_рождения, 6 - Хобби: '))
#     search_content = input (f'Введите данные для поиска: ')
#     for row in file_reader:
#         if search_content in row [search_row]:
#             count +=1
#             print(row)
#     print (f'Всего найдено {count} позиций')
   

# Дописываем строку в базу
# new_row ='101'
# new_id = str(101) # в рабочей версии max_id из блока Приветствие в main.py
# new_row += ','+ input('Добавьте фамилию: ')
# new_row += ','+ input('Добавьте имя: ')
# new_row += ','+ input('Добавьте отдел: ')
# new_row += ','+ input('Добавьте телефон: ')
# new_row += ','+ input('Добавьте дату рождения в формате День-Месяц-Год: ')
# new_row += ','+ input('Добавьте хобби: ')
# new_row += '\n'
# with open('base_rows.csv', mode='a', encoding='utf-8') as f:
#     f.writelines(new_row)

# Удаление строки по id
# with open('temp.csv', 'w', encoding='utf-8') as f:
#     with open('base_rows.csv', 'r', encoding='utf-8') as f1:
#         for line in f1:
#             if line.startswith('51'): # добавить переменную для ввода с клавиатуры
#                 continue
#             f.write(line)
# f = open('base_rows.scv', 'w')
# f.close()
# with open('base_rows.csv', 'w', encoding='utf-8') as f:
#     with open('temp.csv', 'r', encoding='utf-8') as f1:
#         for line in f1:
#             f.write(line)

# Правка (замена) элемента строки


# change_id = input('Введите id записи для исправления элемента: ')
# change_row = int(input('Определите ячейку для внесения исправления: 1 - Фамилия, 2 - Имя, 3- Отдел, 4- Телефон,5 - Дата_рождения, 6 - Хобби: '))
# with open('base_rows.csv', 'r', encoding='utf-8') as f:
#     file_reader = csv.reader(f, delimiter = ",")
#     for row in file_reader:
#         if row [0] == change_id: 
#             print ('\n', row)
#             changed_cell = input('Введите исправленное значение: ')
#             row [change_row] = changed_cell 
#             changed_string = ",".join(map(str, row))
#             print ('\n', changed_string)

# with open('temp.csv', 'w', encoding='utf-8') as f:
#     with open('base_rows.csv', 'r', encoding='utf-8') as f1:
#         for line in f1:
#             if line.startswith(change_id): # добавить переменную для ввода с клавиатуры
#                 f.writelines(changed_string+'\n')
#             else:
#                 f.write(line)

# f = open('base_rows.scv', 'w')
# f.close()
# with open('base_rows.csv', 'w', encoding='utf-8') as f:
#     with open('temp.csv', 'r', encoding='utf-8') as f1:
#         for line in f1:
#             f.write(line)
# print ('Исправление внесено')


# delete_id = input('Введите id записи для удаления строки: ')
# with open('temp.csv', 'w', encoding='utf-8') as f:
#     with open('base_rows.csv', 'r', encoding='utf-8') as f1:
#         for line in f1:
#             if line.split(',')[0] == delete_id:
#                 print (f'Удалена строка: {line}')
#                 continue
#             f.write(line)
# f = open('base_rows.scv', 'w')
# f.close()
# with open('base_rows.csv', 'w', encoding='utf-8') as f:
#     with open('temp.csv', 'r', encoding='utf-8') as f1:
#         for line in f1:
#             f.write(line)

line = '9 2 3 4 5 1 1 4 5 6 7 9 9 9'
print (line.split(' ')[0])


