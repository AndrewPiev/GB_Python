def get_mode():
    mod = input('Введите 1 для работы с рациональными числами или 2 для работы с комплексными: ')
    if mod == '1':
        return 1
    elif mod == '2':
        return 2
    else:
        print ('Неверный ввод данных')
        exit ()

mode = {1: 'Рациональные числа', 2:'Комплексные числа'}

def get_value_rational():
    value_a = float(input('Введите первое число: '))
    value_c = float(input('Введите второе число: '))
    return value_a, value_c

def get_value_comlex():
    print ('Введите коэффициенты для двух комлексных чисел (a+bj) и (c+dj):')
    value_a = float(input('a = '))
    value_b = float(input('b = '))
    value_c = float(input('c = '))
    value_d = float(input('d = '))
    return value_a, value_b, value_c, value_d

def get_operation():
    oper = input('Сделайте выбор операции: 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление: ')
    if oper == '1':
        return 1
    elif oper == '2':
        return 2
    elif oper == '3':
        return 3
    elif oper == '4':
        return 4
    else:
        print ('Неверный ввод данных')
        exit ()

operation = {1: 'сложение', 2: 'вычитание', 3: 'умножение', 4: 'деление'}

def return_result(res):
    return f'Результат равен {res}'
