from operations import view_base, search, new_record, cell_correction, delete_record
from logger import general_log

def execution ():
    choise = ''
    while choise != '6':
        choise = input('Введте цифру для выбора операции с записями: 1 - Посмотреть| 2 - Найти| 3 - Создать| 4 - Исправить| 5 - Удалить| 6 - Выход, \n :')
        if choise == '1':
            result = view_base()
            general_log (choise, result)
        elif choise == '2':
            result = search()
            general_log (choise, result)
        elif choise == '3':
            result = new_record()
            general_log (choise, result)
        elif choise == '4':
            result = cell_correction()
            general_log (choise, result)
        elif choise == '5':
            result = delete_record()
            general_log (choise, result)


