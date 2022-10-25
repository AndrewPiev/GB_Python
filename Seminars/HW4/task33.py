# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.


import random

def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans("".join(normal), "".join(super_s))
    return x.translate(res)


N = int(input('Задайте степень многочлена не менее 2: '))

factors = []
for i in range (N+1):
    factors.append (random.randrange(-10, 10))
print (f'Коэффициенты многочлена: ', factors)

if factors[0] == -1:
    polynom = '-x' + get_super (str(N))
elif factors[0] == 1:
    polynom = 'x' + get_super (str(N))
elif factors[0] == 0:
    polynom = ''
elif factors[0] > 0 or factors[0] <0:
    polynom = str (factors[0]) + 'x' + get_super (str(N)) 

if N > 2:
    for i in range (1, N-1):
        if factors [i] == 1:
            polynom += '+' + 'x' + get_super(str(N-i))
        elif factors [i] == -1:
            polynom += '-' + 'x' + get_super(str(N-i))
        elif factors [i] >0:
            polynom += '+' + str (factors[i]) + 'x' + get_super(str(N-i)) 
        elif factors [i] < 0:
            polynom += str (factors[i]) + 'x' + get_super(str(N-i))

if factors [-2] == 1:
    polynom += '+x'
elif factors [-2] == -1:
    polynom += '-x'
elif factors [-2] > 0:
    polynom += '+' + str (factors[-2]) + 'x'
elif factors [-2] < 0:
    polynom += str (factors[-2]) + 'x' 

if factors [-1] == 0:
    polynom += '=0'
elif factors [-1] > 0:
    polynom += '+' + str (factors[-1]) + '=0'
elif factors [-1] < 0:
    polynom += str (factors[-1]) + '=0'

data = open('polynom.txt', 'w', encoding='utf8')
data.writelines(polynom)
data.close()

print (polynom)
