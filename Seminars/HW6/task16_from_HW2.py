# Задача 16. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

N = int(input('Ведите целое число N для вывода на экран чисел последовательности (1+1/n)^n: '))

sequence = list(map(lambda n: round((1+1/n)**n, 2), range (1, N+1)))

print (f'Последовательность (1+1/n)^n для',N, ':', dict(enumerate(sequence, 1)))
print (f'Сумма элементов последовательности:', round(sum(sequence), 2))