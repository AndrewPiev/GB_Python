# Задача 10. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1_coordinate = int(input('Ведите координату X первой точки: '))
y1_coordinate = int(input('Ведите координату Y первой точки: '))
x2_coordinate = int(input('Ведите координату X второй точки: '))
y2_coordinate = int(input('Ведите координату Y второй точки: '))
L = ((x1_coordinate - x2_coordinate)**2 + (y1_coordinate - y2_coordinate)**2)**(1/2)
print (f'длина введенного отрезка составляет', L, 'координатных единиц')