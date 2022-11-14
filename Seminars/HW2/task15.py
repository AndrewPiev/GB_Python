# Задача 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input('Ведите целое положительное число N для вывода на экран последовательности факториалов от 1 до N: '))
factorials_list = []
for i in range (1, N+1):
    factorial_i = 1
    for j in range (1,i+1):
        factorial_i = factorial_i * j
    factorials_list.append (factorial_i)
print ()
print (f'Последовательность факториалов от 1 до',N, ':', factorials_list)
print ()
