# Задача 18. Задайте алгоритм перемешивания списка

import random
N = int(input('Ведите целое положительное число N для определения количества элементова массива: '))
mix_array = []
for i in range (N):
    mix_array.append(i)
print (f'Оригинальный массив: ', mix_array)
for i in range (len(mix_array)):
    temp = mix_array[i]
    temp_position = random.randrange(0, N)
    mix_array[i] = mix_array [temp_position]
    mix_array [temp_position] = temp
print (f'Перемешанный массив: ', mix_array)