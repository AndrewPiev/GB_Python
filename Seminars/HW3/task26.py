# Задача 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonachi(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonachi(n-1)+fibonachi(n-2)

def nofibonachi(n):
    if n == -1: return 1
    elif n == -2: return -1
    else: return nofibonachi(n+2)-nofibonachi(n+1)

N = int(input('Ведите целое число N для построения ряда чисел негафибоначчи и фибоначчи (-N,N): '))

fibonachi_array = []
for i in range (N+1):
    fibonachi_array.append (fibonachi(i))

nofibonachi_array = []
for i in range (-N,0,1):
    nofibonachi_array.append (nofibonachi(i))

print (nofibonachi_array+fibonachi_array)

