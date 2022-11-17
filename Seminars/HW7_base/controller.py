from operations import view_base, search, new_record, cell_correction, delete_record

def execution ():
    choise = ''
    while choise != '6':
        choise = input('Введте цифру для выбора операции с записями: 1 - Посмотреть| 2 - Найти| 3 - Создать| 4 - Исправить| 5 - Удалить| 6 - Выход, \n :')
        if choise == '1':
            view_base()
        elif choise == '2':
            search()
        elif choise == '3':
            new_record()
        elif choise == '4':
            cell_correction()
        elif choise == '5':
            delete_record()

