# Задача 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

numbers = ['0','1','2','3','4','5','6','7','8','9']
input_number = input('Ведите вещественное число: ')
sum_numbers = 0
for i in input_number:
    if i in numbers:
        sum_numbers = sum_numbers + int (i)
print ()
print (f'Сумма цифр введенного числа равняется', sum_numbers)
print ()