import random

afterplayerstep_phrases = ['Замечательно!', 'Ход сделан!', 'Неплохо..', 'Так-так..', 'Хорошо!', 'Ход сделан!', 'Прекрасно!', 'Так-так..']
botstep_phrases = ['Теперь', 'Сейчас', 'Настал', 'Вот и']

def multiplayer_game (player1, player2):
    candy_count = 150
    player_count = random.randrange (1, 3)
    if player_count % 2 != 0:
            player = player1
    else:
            player = player2
    print ('По счастливой случайности игру выпало начинать Вам, ', player)
    while candy_count >0:
        if player_count % 2 != 0:
            player = player1
        else:
            player = player2
        print (player, ', Ваш ход!')
        candy_count -= int (input ('Сколько конфет заберете?: '))
        player_count += 1
        print (random.choice(afterplayerstep_phrases))
        print ('На столе осталось конфет: ', candy_count)
        if candy_count == 0:
            print (player, ', это победа! Мои искренние поздравления! Забирайте свои конфеты!')
    return ()

def bot_game (player):
    candy_count = 150
    player_count = random.randrange (1, 3)
    if player_count % 2 != 0:            
            print ('По счастливой случайности игру выпало начинать Вам!')
    else:
            print ('По не очень счастливой для Вас случайности игру выпало начинать мне. Настройтесь серьезно, я обожаю конфеты!')
    while candy_count >0:
        if player_count % 2 != 0:
            print (player, ', Ваш ход!')
            candy_count -= int (input ('Сколько конфет заберете?: '))
            print (random.choice(afterplayerstep_phrases))
            print ('На столе осталось конфет: ', candy_count)
        else:
            if candy_count < 29:
                bot_step = candy_count
                candy_count = 0
            elif candy_count % 29 != 0:
                bot_step = candy_count % 29
                candy_count -= candy_count % 29
            elif candy_count % 29 == 0:
                bot_step = random.randrange (1, 29)
                candy_count -= bot_step
            print (random.choice(botstep_phrases), 'мой ход, и число конфет в этот раз - ', bot_step)
            print ('На столе осталось конфет: ', candy_count)
        if candy_count == 0:
            if player_count % 2 != 0:
                print (player, ', Ваша победа! Мои искренние поздравления! Забирайте свои конфеты!')
            else:
                print (player, ', к сожалению, в этот раз Вы проиграли! Не расстраивайтесь, открою секрет: я очень умный бот, при моем первом ходе или совершении Вами хотя бы одного неоптимального хода выиграть у меня невозможно, такова моя математика!')
        player_count += 1
    return ()

print()
print ('Привет! Меня зовут Ваcилий. Я бот-мастер игры в конфеты. Давайте сыграем в мою интересную игру!')
print()
print ('На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Вы можете играть как вдвоем друг против друга, так и один игрок может сыграть против меня.') 
print()
game_mode = int(input('Давайте выберем режим игры: нажимаете 1 - играете между собой вдвоем, жмете 2 - один игрок будет делить конфеты со мной. Ваш выбор?: '))

if game_mode == 1:
    print()
    print ('Отличный выбор! Надеюсь игра принесет вам только удовольствие и конфетами друг с другом вы в итоге все-же поделитесь)))')
    print()
    name1 = input('Игрок № 1, представьтесь, пожалуйста: ')
    print()
    name2 = input('Игрок № 2, представьтесь, пожалуйста: ')
    multiplayer_game (name1, name2)
else: 
    print()
    name1 = input('Мой многоуважаемый соперник, представьтесь, пожалуйста: ')
    print (name1, ', очень рад нашему знакомству!')
    bot_game (name1)
print()
