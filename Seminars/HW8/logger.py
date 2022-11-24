from datetime import datetime as dt

def general_log(a,b):
    time = dt.now().strftime('%H:%M')
    mode = {'1':'Просмотр', '2':'Поиск', '3':'Создание', '4':'Правка', '5':'Удаление'}
    with open ('log.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'Время операции: {time}, Операция: {mode[a]}, Результат операции: {b}\n')