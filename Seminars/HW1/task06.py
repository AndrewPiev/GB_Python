# Задача 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day_number = int(input('Ведите номер дня недели: '))
if day_number > 7 or day_number < 1:
    print ('Такого дня недели не существует')
elif day_number == 6 or day_number == 7:
    print ('Введеный день недели является выходным')
else:
    print ('Введеный день недели не является выходным')