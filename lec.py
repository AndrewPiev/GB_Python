# Задача 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# day_number = int(input('Ведите номер дня недели: '))
# if day_number > 7 or day_number < 1:
#     print ('Такого дня недели не существует')
# elif day_number == 6 or day_number == 7:
#     print ('Введеный день недели является выходным')
# else:
#     print ('Введеный день недели не является выходным')

# for x in range (2):
#     for y in range (2):
#         for z in range (2):
#             if (not (bool (x) or bool (y) or bool (z))) == (not bool (x) and not bool (y) and not bool(z)):
#                 a=1
#                 print (x, y, z)
#                 print (not (bool (x) or bool (y) or bool (z)))
#                 print (not x and not y and not z)
#                 print ()
#             else:
#                 a=0
#                 print ('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z является ложным для тройки', x, y, z)
#                 break
# if a > 0:
#     print ('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z является истиным для любых булевых значений X, Y, Z')
#     print()

# x_coordinate = int(input('Ведите координату X: '))
# y_coordinate = int(input('Ведите координату Y: '))
# if x_coordinate == 0 and y_coordinate == 0:
#     print ('Введенная точка лежит на пересечении оси координат')
# elif x_coordinate == 0:
#     print ('Введенная точка лежит на оси X')
# elif y_coordinate == 0:
#     print ('Введенная точка лежит на оси Y')
# elif y_coordinate > 0 and x_coordinate > 0:
#     print ('Введенная точка лежит в первой координатной четверти')
# elif y_coordinate > 0 and x_coordinate < 0:
#     print ('Введенная точка лежит во второй координатной четверти')
# elif y_coordinate < 0 and x_coordinate < 0:
#     print ('Введенная точка лежит в третьей координатной четверти')
# elif y_coordinate < 0 and x_coordinate > 0:
#     print ('Введенная точка лежит в четвертой координатной четверти')

# coordinate_quater = int(input('Ведите номер координатной четверти от 1 до 4: '))
# if coordinate_quater >4 or coordinate_quater <1:
#     print ('неверный ввод')
# elif coordinate_quater == 1:
#     print ('значения Х: (0, +∞) значения У: (0, +∞)')
# elif coordinate_quater == 2:
#     print ('значения Х: (0, -∞) значения У: (0, +∞)')
# elif coordinate_quater == 3:
#     print ('значения Х: (0, -∞) значения У: (0, -∞)')
# elif coordinate_quater == 4:
#     print ('значения Х: (0, +∞) значения У: (0, -∞)')


x1_coordinate = int(input('Ведите координату X первой точки: '))
y1_coordinate = int(input('Ведите координату Y первой точки: '))
x2_coordinate = int(input('Ведите координату X второй точки: '))
y2_coordinate = int(input('Ведите координату Y второй точки: '))
L = ((x1_coordinate - x2_coordinate)**2 + (y1_coordinate - y2_coordinate)**2)**(1/2)
print (f'длина введенного отрезка составляет', L, 'координатных единиц')