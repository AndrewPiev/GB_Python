# Задача дополнительная №2  Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Например:  >>> num_translate("one") "один" >>> num_translate("eight") "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую
# для перевода: какой тип данных выбрать, в теле функции или снаружи.
# Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One") "Один" >>> num_translate_adv("two") "два"

def translation (vocabulary, word):
    b = ''
    if word.istitle () == True:
        b = word.lower()
        if b in numbers_vocabulary:
            print ((numbers_vocabulary.get(b)).title())
        else:
            print ('None')
    else:
        print (numbers_vocabulary.get(word))

numbers_vocabulary = {'one': 'один', 'two': 'два'}
eng_word = input('Введите число на аглийском для перевода: ')

translation (numbers_vocabulary, eng_word)
