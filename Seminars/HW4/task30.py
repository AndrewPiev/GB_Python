
# users_hobby = {}
# file_1 = open('users.txt', 'r', encoding='utf8')
# paragraphs = file_1.readlines()
# print(paragraphs)
# file_1.close()

path = 'users.txt'
data = open(path, 'r', encoding='utf8')
for line in data:
    print(line)
data.close()