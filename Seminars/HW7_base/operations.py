import csv

# Просмотр базы
def view_base ():
    with open('base_rows.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


# Поиск по столбцам базы
def search ():
    with open('base_rows.csv', 'r', encoding='utf-8') as f:
        file_reader = csv.reader(f, delimiter = ",")
        count = 0
        search_row = input('Введите параметр для поиска: 0 - id, 1 - Фамилия, 2 - Имя, 3- Отдел, 4- Телефон, 5 - Дата_рождения, 6 - Хобби: ')
        if search_row in ['0', '1', '2', '3', '4', '5', '6']:
            search_content = input (f'Введите данные для поиска: ')
            for row in file_reader:
                if search_content in row [int(search_row)]:
                    count +=1
                    print(row)
            print (f'Всего найдено позиций: {count} ')
        else:
            print('Неверный ввод данных')

# Создание новой записи
def new_record ():
    with open('base_rows.csv', 'r', encoding='utf-8') as f:
        file_reader = csv.reader(f, delimiter = ",")
        for row in file_reader:       
            max_id = row[0]
    new_row = str(int(max_id) + 1)
    new_row += ','+ input('Добавьте фамилию: ')
    new_row += ','+ input('Добавьте имя: ')
    new_row += ','+ input('Добавьте отдел: ')
    new_row += ','+ input('Добавьте телефон: ')
    new_row += ','+ input('Добавьте дату рождения в формате День-Месяц-Год: ')
    new_row += ','+ input('Добавьте хобби: ')
    new_row += '\n'
    with open('base_rows.csv', mode='a', encoding='utf-8') as f:
        f.writelines(new_row)
    print (f'Создана новая запись: {new_row}')

# Правка в ячейке (замена значения)
def cell_correction ():
    change_id = input('Введите id записи для исправления элемента: ')
    change_row = int(input('Определите ячейку для внесения исправления: 1 - Фамилия, 2 - Имя, 3- Отдел, 4- Телефон,5 - Дата_рождения, 6 - Хобби: '))
    changed_string = ''
    with open('base_rows.csv', 'r', encoding='utf-8') as f:
        file_reader = csv.reader(f, delimiter = ",")
        for row in file_reader:
            if row [0] == change_id:
                if change_row in [1, 2, 3, 4, 5]:
                    print (f'Исправляем запись: {row}')                    
                    changed_cell = input('Введите новое значение: ')
                    row [change_row] = changed_cell 
                    changed_string = ",".join(map(str, row))
                    print (f'Исправленная запись: {changed_string}')

    if changed_string != '':
        # Перезапись копии с новой строкой
        with open('temp.csv', 'w', encoding='utf-8') as f:
            with open('base_rows.csv', 'r', encoding='utf-8') as f1:
                for line in f1:
                    if line.split(',')[0] == change_id:
                        f.writelines(changed_string+'\n')
                    else:
                        f.write(line)
        # Перезапись из копии с новой строкой
        f = open('base_rows.scv', 'w')
        f.close()
        with open('base_rows.csv', 'w', encoding='utf-8') as f:
            with open('temp.csv', 'r', encoding='utf-8') as f1:
                for line in f1:
                    f.write(line)
    else:
        print ('Неверный ввод данных, внесение изменений невозможно')

# Удаление строки по id
def delete_record ():
    delete_id = input('Введите id записи для удаления строки: ')
    with open('temp.csv', 'w', encoding='utf-8') as f:
        with open('base_rows.csv', 'r', encoding='utf-8') as f1:
            for line in f1:
                if line.split(',')[0] == delete_id:
                    print (f'Удалена строка: {line}')
                    continue
                f.write(line)
    f = open('base_rows.scv', 'w')
    f.close()
    with open('base_rows.csv', 'w', encoding='utf-8') as f:
        with open('temp.csv', 'r', encoding='utf-8') as f1:
            for line in f1:
                f.write(line)









    # delete_id = input('Введите id записи для удаления строки: ')
    # with open('temp.csv', 'w', encoding='utf-8') as f:
    #     with open('base_rows.csv', 'r', encoding='utf-8') as f1:
    #         for line in f1:
    #             if line.startswith(delete_id): # добавить переменную для ввода с клавиатуры
    #                 continue
    #             f.write(line)
    # f = open('base_rows.scv', 'w')
    # f.close()
    # with open('base_rows.csv', 'w', encoding='utf-8') as f:
    #     with open('temp.csv', 'r', encoding='utf-8') as f1:
    #         for line in f1:
    #             f.write(line)
