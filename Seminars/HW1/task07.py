# Задача 7. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range (2):
    for y in range (2):
        for z in range (2):
            if (not (bool (x) or bool (y) or bool (z))) == (not bool (x) and not bool (y) and not bool(z)):
                a=1
                print (x, y, z)
                print (not (bool (x) or bool (y) or bool (z)))
                print (not x and not y and not z)
                print ()
            else:
                a=0
                print ('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z является ложным для тройки', x, y, z)
                break
if a > 0:
    print ('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z является истиным для любых булевых значений X, Y, Z')
    print()