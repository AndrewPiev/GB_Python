# Задача 8. Напишите программу, которая принимает на вход координаты точки (X и Y),  и выдаёт номер четверти плоскости

x_coordinate = int(input('Ведите координату X: '))
y_coordinate = int(input('Ведите координату Y: '))
if x_coordinate == 0 and y_coordinate == 0:
    print ('Введенная точка лежит на пересечении оси координат')
elif x_coordinate == 0:
    print ('Введенная точка лежит на оси X')
elif y_coordinate == 0:
    print ('Введенная точка лежит на оси Y')
elif y_coordinate > 0 and x_coordinate > 0:
    print ('Введенная точка лежит в первой координатной четверти')
elif y_coordinate > 0 and x_coordinate < 0:
    print ('Введенная точка лежит во второй координатной четверти')
elif y_coordinate < 0 and x_coordinate < 0:
    print ('Введенная точка лежит в третьей координатной четверти')
elif y_coordinate < 0 and x_coordinate > 0:
    print ('Введенная точка лежит в четвертой координатной четверти')