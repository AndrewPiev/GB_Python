from datetime import datetime as dt
from view import mode, operation

def general_log(num1, num2, func1, func2, res):
    time = dt.now().strftime('%H:%M')
    with open ('log.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'Время внесения данных {time}, {mode[func1]}, Первое число: {num1}, Второе число: {num2}, Операция: {operation[func2]},  Результат: {res} \n')
