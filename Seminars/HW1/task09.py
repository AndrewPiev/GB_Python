# Задача 9. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

coordinate_quater = int(input('Ведите номер координатной четверти от 1 до 4: '))
if coordinate_quater >4 or coordinate_quater <1:
    print ('неверный ввод')
elif coordinate_quater == 1:
    print ('значения Х: (0, +∞) значения У: (0, +∞)')
elif coordinate_quater == 2:
    print ('значения Х: (0, -∞) значения У: (0, +∞)')
elif coordinate_quater == 3:
    print ('значения Х: (0, -∞) значения У: (0, -∞)')
elif coordinate_quater == 4:
    print ('значения Х: (0, +∞) значения У: (0, -∞)')