# Задача 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random

N = int(input('Ведите целое число N для наполнения массива случайными вещественными числами: '))
# Генерация массива
array_float = []
for i in range (0, N):
    array_float.append (round (random.uniform(-N, N+1), 2))
print (f'Сгенерирован следующий массив: ', array_float)
print()
# Получения массива дробных частей
array_string_into_fraction = []
for j in range (N):
    array_string_into_fraction.append (str(array_float[j]))
    temp_string =  array_string_into_fraction [j]
    for k in range (len(temp_string)):
        if temp_string [k] == '.':
            array_string_into_fraction [j] = float (temp_string[k:])

array_string_into_fraction.sort()
print (f'Массив дробных частей по возрастанию: ', array_string_into_fraction)    
print()      
print (f'Разница между максильной и минимальной  дробными частями: ', round(array_string_into_fraction[len(array_string_into_fraction)-1] - array_string_into_fraction[0], 3))


