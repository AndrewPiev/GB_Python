# Задача 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на введенных пользователем позициях.

import random
from turtle import position
N = int(input('Ведите целое число N для наполнения массива случайными числами: '))
array_rand = []
for i in range (0, N):
    array_rand.append (random.randrange(-N, N+1))
print (f'Сгенерирован следующий массив: ', array_rand)
number_for_multiply = int(input('Сколько элементов массива будем перемножать между сосбой? '))
multiplication = 1
for i in range (number_for_multiply):
    position = int(input('Ведите номер элемента для влючения в перемножениe: '))
    multiplication = multiplication * array_rand [position-1]    
print (f'Произведение элементов с введенными номерами составило: ', multiplication)