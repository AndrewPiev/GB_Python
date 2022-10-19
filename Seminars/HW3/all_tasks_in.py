# Задача 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# import random

# def array_forming (n):
#     array_rand = []
#     for i in range (0, n):
#         array_rand.append (random.randrange(10))
#     print (f'Сгенерирован следующий массив: ', array_rand)
#     return array_rand

# N = int(input('Ведите целое число N для наполнения массива N случайными числами: '))
# array = array_forming (N)

# sum = 0
# for i in range (0, N, 2):
#     sum += array [i]    

# print (f'Сумма нечетных элементов массива составила: ', sum)

# Задача 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# import random

# def array_forming (n):
#     array_rand = []
#     for i in range (0, n):
#         array_rand.append (random.randrange(10))
#     print (f'Сгенерирован следующий массив: ', array_rand)
#     return array_rand

# N = int(input('Ведите целое число N для наполнения массива N случайными числами: '))
# array = array_forming (N)

# array_couples_multiplication = []
# for i in range (int(N/2+0.5)):
#     array_couples_multiplication.append (array[i]*array[-1-i])

# print (f'Массив произведения пар элементов: ', array_couples_multiplication)


# Задача 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# import random

# N = int(input('Ведите целое число N для наполнения массива случайными вещественными числами: '))
# # Генерация массива
# array_float = []
# for i in range (0, N):
#     array_float.append (round (random.uniform(-N, N+1), 2))
# print (f'Сгенерирован следующий массив: ', array_float)
# print()
# # Получения массива дробных частей
# array_string_into_fraction = []
# for j in range (N):
#     array_string_into_fraction.append (str(array_float[j]))
#     temp_string =  array_string_into_fraction [j]
#     for k in range (len(temp_string)):
#         if temp_string [k] == '.':
#             array_string_into_fraction [j] = float (temp_string[k:])

# array_string_into_fraction.sort()
# print (f'Массив дробных частей по возрастанию: ', array_string_into_fraction)    
# print()      
# print (f'Разница между максильной и минимальной  дробными частями: ', round(array_string_into_fraction[len(array_string_into_fraction)-1] - array_string_into_fraction[0], 3))

# Задача 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# def tenth_into_binary (n):
#     if n == 0:
#         print (n)
#         exit()

#     b = ''
    
#     while n > 0:
#         b = str(n % 2) + b
#         n = n // 2
    
#     print(b)

# N = int(input('Введите десятичное число для преобразования в двоичное: '))
# tenth_into_binary (N)

# Задача 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def fibonachi(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return fibonachi(n-1)+fibonachi(n-2)

# def nofibonachi(n):
#     if n == -1: return 1
#     elif n == -2: return -1
#     else: return nofibonachi(n+2)-nofibonachi(n+1)

# N = int(input('Ведите целое число N для построения ряда чисел негафибоначчи и фибоначчи (-N,N): '))

# fibonachi_array = []
# for i in range (N+1):
#     fibonachi_array.append (fibonachi(i))

# nofibonachi_array = []
# for i in range (-N,0,1):
#     nofibonachi_array.append (nofibonachi(i))

# print (nofibonachi_array+fibonachi_array)

# Задача дополнительная №1 Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

# stuff_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# N = int(input('Ведите номер работника от 1 до 4 для приветствия: '))
# temp = stuff_list [N-1]
# name = temp[temp.rfind(' '):]
# name.lower
# greeting = 'Привет,'+name.title()+'!'
# print (greeting)

# Задача дополнительная №2  Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Например:  >>> num_translate("one") "один" >>> num_translate("eight") "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую
# для перевода: какой тип данных выбрать, в теле функции или снаружи.
# Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One") "Один" >>> num_translate_adv("two") "два"

# def translation (vocabulary, word):
#     b = ''
#     if word.istitle () == True:
#         b = word.lower()
#         if b in numbers_vocabulary:
#             print ((numbers_vocabulary.get(b)).title())
#         else:
#             print ('None')
#     else:
#         print (numbers_vocabulary.get(word))

# numbers_vocabulary = {'one': 'один', 'two': 'два'}
# eng_word = input('Введите число на аглийском для перевода: ')

# translation (numbers_vocabulary, eng_word)