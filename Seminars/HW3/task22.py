# Задача 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

def array_forming (n):
    array_rand = []
    for i in range (0, n):
        array_rand.append (random.randrange(10))
    print (f'Сгенерирован следующий массив: ', array_rand)
    return array_rand

N = int(input('Ведите целое число N для наполнения массива N случайными числами: '))
array = array_forming (N)

sum = 0
for i in range (0, N, 2):
    sum += array [i]    

print (f'Сумма нечетных элементов массива составила: ', sum)