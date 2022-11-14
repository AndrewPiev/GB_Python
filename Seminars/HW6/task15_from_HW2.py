# Задача 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def factorial (x):
    factorial_i = 1
    for i in range (1, x+1):
        factorial_i = factorial_i * i
    return factorial_i

N = int(input('Ведите целое положительное число N для вывода на экран последовательности факториалов чисел от 1 до N: '))

print (f'Таблица факториалов чисел от 1 до',N,':',dict(enumerate(map (factorial, range (1, N+1)), 1)))