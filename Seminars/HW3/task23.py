# Задача 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

def array_forming (n):
    array_rand = []
    for i in range (0, n):
        array_rand.append (random.randrange(10))
    print (f'Сгенерирован следующий массив: ', array_rand)
    return array_rand

N = int(input('Ведите целое число N для наполнения массива N случайными числами: '))
array = array_forming (N)

array_couples_multiplication = []
for i in range (int(N/2+0.5)):
    array_couples_multiplication.append (array[i]*array[-1-i])

print (f'Массив произведения пар элементов: ', array_couples_multiplication)

