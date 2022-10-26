import random

game_desk = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

afterplayerstep_phrases = ['Замечательно!', 'Ход сделан!', 'Неплохо..', 'Так-так..', 'Хорошо!', 'Ход сделан!', 'Прекрасно!', 'Так-так..', 'Ход сделан!']

def print_desk (desk):
    print (desk[0:3])
    print (desk[3:6])
    print (desk[6:10])

def check_win (desk, a):
    if desk[0:3] == [a,a,a] or desk[3:6] == [a,a,a] or desk[6:9] == [a,a,a] or desk[0]+desk[3]+desk[6] == a*3 or desk[1]+desk[4]+desk[7] == a*3 or desk[2]+desk[5]+desk[8] == a*3 or desk[0]+desk[4]+desk[8] == a*3 or desk[2]+desk[4]+desk[6] == a*3:
        return True
    else:
        return False

def multiplayer_game (player1, player2):    
    player_count = random.randrange (1, 3)
    if player_count % 2 != 0:
            player = player1
    else:
        player1, player2 = player2, player1
        player = player1
    print ('По счастливой случайности игру выпало начинать Вам, ', player)
    player_count = 1
    print_desk (game_desk)
    for i in range (9):        
        if player_count % 2 != 0:
            player = player1
            step_figure = 'X'
        else:
            player = player2
            step_figure = '0'
        print (player, ', Ваш ход!')        
        step = int (input('На какую позицию ставим?'))
        game_desk [step-1] = step_figure
        print_desk (game_desk)
        print (random.choice(afterplayerstep_phrases))
        if check_win (game_desk, step_figure) == True:
            print (player, ', это победа! Искренние поздравления!')
            exit ()
        player_count += 1
    print ('Ничья! В этот раз победила дружба!')
    return ()

print ('Привет! Давайте сыграем в крестики-нолики! Выигрывает тот игрок, кто первый соберет линию из трех своих знаков. Для выбора места постановки своего знака необходимо выбрать цифру позиции, не занятой свом знаком или знаком соперника.')
name1 = input('Игрок № 1, представьтесь, пожалуйста: ')
print()
name2 = input('Игрок № 2, представьтесь, пожалуйста: ')
print ()
multiplayer_game (name1, name2)
