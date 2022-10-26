# Задача 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def in_RLE (a):
    temp = a + ' '
    count = 1
    c = ''
    b = ''
    for i in range (len(temp)-1):
        if a[i] == temp[i+1]:
            count +=1
            b = str(count) + temp[i]
        else:
            b = str(count) + a[i]
            c += b
            count = 1
    return c

def out_RLE (a):
    count = 0
    b = ''
    for i in range (0, len (a)-1, 2):
        b += a[i+1]*int (a[i])
    return b

a1 = 'CAABBBBGFR'
print (a1)

a2 = in_RLE(a1)
print (a2)

a3 = out_RLE(a2)
print (a3)

print (a1==a3)       

with open('for_RLE.txt','r') as firstfile, open('RLE.txt','w') as secondfile:
    for line in firstfile:
             secondfile.write(in_RLE(line))


with open('RLE.txt','r') as thirdfile, open('unpacked_RLE.txt','w') as fourthfile:
    for line in thirdfile:
             fourthfile.write(out_RLE(line))
