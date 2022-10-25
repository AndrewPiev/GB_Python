# 34. *Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

data = open('polynom1.txt', 'r', encoding='utf8')
for line in data:
    polynom1 = line
    print (polynom1)
data.close()

data = open('polynom2.txt', 'r', encoding='utf8')
for line in data:
    polynom2 = line
    print (polynom2)
data.close()

factors1 = []
factors2 = []
numbers_plus = ['0','1','2','3','4','5','6','7','8','9', '+', '-']
numbers = ['0','1','2','3','4','5','6','7','8','9']

# if polynom1 [0] == 'x':
#     factors1.append ('1')
# elif polynom1 [0] == '-' and polynom1 [1] not in numbers:
#     factors1.append ('-1')
# elif polynom1 [0] == '-' and polynom1 [1] in numbers:
#     factors1.append (polynom1 [0] + polynom1 [1])
# elif polynom1 [0] in numbers:
#     factors1.append (polynom1 [0])

temp = ''
for i in range (0, len(polynom1)-1):
    if polynom1 [i] in numbers_plus:
        temp += polynom1 [i]
    else:
        factors1.append (temp)
        temp = ''
factors1.remove ('')


# if polynom2 [0] == 'x':
#     factors2.append ('1')
# elif polynom2 [0] == '-' and polynom2 [1] not in numbers:
#     factors2.append ('-1')
# elif polynom2 [0] == '-' and polynom2 [1] in numbers:
#     factors2.append (polynom2 [0] + polynom2 [1])
# elif polynom2 [0] in numbers:
#     factors2.append (polynom2 [0])

temp = ''
for i in range (0, len(polynom2)-1):
    if polynom2 [i] in numbers_plus:
        temp += polynom2 [i]
    else:
        factors2.append (temp)
        temp = ''
factors2.remove ('')


print (factors1)
print (factors2)

sum_factors = []
for i in range (len (factors1)):
    sum_factors.append (str (int (factors1[i]) + int (factors2[i])))

print (sum_factors)

sum_polynoms = sum_factors [0] + 'x²' + sum_factors [1] + 'x' + sum_factors [2]+ '=0'

print (sum_polynoms)

data = open('sum_polynoms.txt', 'w', encoding='utf8')
data.writelines(sum_polynoms)
data.close()