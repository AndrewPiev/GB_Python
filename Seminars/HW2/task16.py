# Задача 16. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

N = int(input('Ведите целое число N для вывода на экран чисел последовательности (1+1/n)^n: '))
sequence = {}
sequence_sum = 0
for i in range (1, N+1):
   sequence [i]= round (float ((1+1/i)**i), 2) 
   sequence_sum = sequence_sum + round (float ((1+1/i)**i), 2)
print ()
print (f'Последовательность (1+1/n)^n для',N, ':', sequence, 'и сумма ее элементов составила', round(sequence_sum, 2))
print ()