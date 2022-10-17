# Задача 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# numbers = ['0','1','2','3','4','5','6','7','8','9']
# input_number = input('Ведите вещественное число: ')
# sum_numbers = 0
# for i in input_number:
#     if i in numbers:
#         sum_numbers = sum_numbers + int (i)
# print ()
# print (f'Сумма цифр введенного числа равняется', sum_numbers)
# print ()

# Задача 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# N = int(input('Ведите целое положительное число N для вывода на экран последовательности факториалов от 1 до N: '))
# factorials_list = []
# for i in range (1, N+1):
#     factorial_i = 1
#     for j in range (1,i+1):
#         factorial_i = factorial_i * j
#     factorials_list.append (factorial_i)
# print ()
# print (f'Последовательность факториалов от 1 до',N, ':', factorials_list)
# print ()

# Задача 16. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# N = int(input('Ведите целое число N для вывода на экран чисел последовательности (1+1/n)^n: '))
# sequence = {}
# sequence_sum = 0
# for i in range (1, N+1):
#    sequence [i]= round (float ((1+1/i)**i), 2) 
#    sequence_sum = sequence_sum + round (float ((1+1/i)**i), 2)
# print ()
# print (f'Последовательность (1+1/n)^n для',N, ':', sequence, 'и сумма ее элементов составила', round(sequence_sum, 2))
# print ()

# Задача 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на введенных пользователем позициях.

# import random
# from turtle import position
# N = int(input('Ведите целое число N для наполнения массива случайными числами: '))
# array_rand = []
# for i in range (0, N):
#     array_rand.append (random.randrange(-N, N+1))
# print (f'Сгенерирован следующий массив: ', array_rand)
# number_for_multiply = int(input('Сколько элементов массива будем перемножать между сосбой? '))
# multiplication = 1
# for i in range (number_for_multiply):
#     position = int(input('Ведите номер элемента для влючения в перемножениe: '))
#     multiplication = multiplication * array_rand [position-1]    
# print (f'Произведение элементов с введенными номерами составило: ', multiplication)

# Задача 18. Задайте алгоритм перемешивания списка

# import random
# N = int(input('Ведите целое положительное число N для определения количества элементова массива: '))
# mix_array = []
# for i in range (N):
#     mix_array.append(i)
# print (f'Оригинальный массив: ', mix_array)
# for i in range (len(mix_array)):
#     temp = mix_array[i]
#     temp_position = random.randrange(0, N)
#     mix_array[i] = mix_array [temp_position]
#     mix_array [temp_position] = temp
# print (f'Перемешанный массив: ', mix_array)