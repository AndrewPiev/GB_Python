# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple_number (x):
    for i in range (2, x):
        if x % i == 0:
            return False
            break
    return True

N = int(input('Введите натуральное число для определения его простых делителей: '))
print (f'Простые делители для введенного числа: ', list(filter(lambda i: N % i == 0 and simple_number (i), range (1, N+1)))) # - новое решение

# Старое решение (заменено на строку №11):
# N = int(input('Введите натуральное число для определения его простых делителей: '))
# simple_dividers = []

# for i in range (1, N+1):
#     if N % i == 0 and simple_number (i):
#         simple_dividers.append (i)


# print (f'Простые делители для введенного числа: ', simple_dividers)

