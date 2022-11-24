# colors = ['red', 'greenAAA', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#  print(line)
# data.close()

# import temp
# tenth_into_binary.f(5)

# def check_sorted(somelist):
#     if sorted(set(somelist)) == somelist:
#         return 1
#     elif sorted(set(somelist), reverse=True) == somelist:
#         return -1
#     return 0
# s_dict = {
#     1: 'Возрастает',
#     -1: 'Убывает',
#     0: 'Ни то, ни то'
#           }

# print(s_dict[check_sorted([1, 2, 3])])
# print(s_dict[check_sorted([3, 2, 3])])
# print(s_dict[check_sorted([3, 2, 1])])
# print(check_sorted([1, 1, 2, 3]))

# a = [1,2]
# b = [3,4]
# print (a+b)


# a = [[1, 3, 2], [9, 7, 8], [4, 5, 6]]
# b = []
# for i in range (len (a)):
#     b += a [i]
# print (b)

# def simple_math(operation:list):
#     if operation[1] == '/':
#         return [str(float(operation[0]) / float(operation[2]))]
#     if operation[1] == '*':
#         return [str(float(operation[0]) * float(operation[2]))]
#     if operation[1] == '+':
#         return [str(float(operation[0]) + float(operation[2]))]
#     if operation[1] == '-':
#         return [str(float(operation[0]) - float(operation[2]))]
# string = '1+23*3-2*4'

# def list_from_string(string:str):

#     result = []
#     temp = 0
#     for i in range(0, len(string)):

#         if not string[i].isalnum():
#             result.append(string[temp:i])
#             result.append(string[i])
#             temp = i + 1

#     result.append(string[temp:])
#     print(result)

#     return result

# def simple_math(operation:list):
#     if operation[1] == '/':
#         return [str(float(operation[0]) / float(operation[2]))]
#     if operation[1] == '*':
#         return [str(float(operation[0]) * float(operation[2]))]
#     if operation[1] == '+':
#         return [str(float(operation[0]) + float(operation[2]))]
#     if operation[1] == '-':
#         return [str(float(operation[0]) - float(operation[2]))]
# def do_math(equation:list):

#     while len(equation) != 1:
#         for sign in '/*+-':
#             while sign in equation:
#                 idx = equation.index(sign)
#                 equation = equation[:idx-1] + simple_math(equation[idx-1:idx+2]) + equation[idx+2:]

#     return equation

# print(do_math(list_from_string(string)))


# print (list(map(lambda x,y : x*y, range (5), range (5))))

# print (complex (1,1) / complex (1,1))


# from datetime import datetime

# now = datetime.now()

# print(now)
# print(now.year)
# print(now.month)
# print(now.hour)
# print(type(now.second))

# print (now.year - 10)
# print (type(now))


# import random

# print (f'{random.randrange(1,29)}-{random.randrange(1,13)}-{random.randrange(1960,2000)}')



