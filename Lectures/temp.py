def tenth_into_binary (n):
    if n == 0:
        print (n)
        exit()

    b = ''
    
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    
    print(b)

N = int(input('Введите десятичное число для преобразования в двоичное: '))
tenth_into_binary (N)