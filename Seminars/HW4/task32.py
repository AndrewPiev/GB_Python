# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

my_list = [1, 1, 2 ,5 ,5 ,7]
unrepeated = []
for i in my_list:
    if my_list.count(i) == 1:
        unrepeated.append (i)
print ('Изначальный список: ', my_list)
print ('Неповторяющиеся элементы: ', sorted(unrepeated))
