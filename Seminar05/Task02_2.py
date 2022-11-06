# б) бот с интелектом

import random

print('\n\033[1m\033[6m\033[36mПриветствуем вас в самой вкусной игре - игра с конфетами!\n')
print('\033[1m\033[4m\033[37m\033[45mПравила игры: \033[0m\
    \nИграют два игрока, делая ход друг после друга.\
    \nПервый ход определяется жеребьёвкой.\
    \nЗа один ход можно забрать не более 28 конфет.\
    \nВ итоге все конфеты достаются игроку, сделавшему последний ход.\n')

print('Меня зовут\033[0m  \033[1m\033[6m\033[32mМаруся!\033[0m \nПоиграем вместе?\n')

gamer1 = input('\033[3mВведите Ваше имя\033[0m ')
gamer11 = (f'\033[1m\033[3\033[32m{gamer1}')
gamer12 = 'Маруся'

TotalBonbon = 100

maxTakeBonbon = 28
firstTurn = random.randint(1,2)
if firstTurn == 1:
    currentTurn = gamer11
else:
    currentTurn = gamer12
print(f'\nПервым ходит игрок - \033[32m{currentTurn}\033[0m')
takeBonbon = 0
while TotalBonbon > 0:
    if TotalBonbon == 11 or TotalBonbon == 12 or TotalBonbon == 13 or TotalBonbon == 14:
        print(f'\nНа столе \033[34m{TotalBonbon}\033[0m конфет')
    elif TotalBonbon == 1 or TotalBonbon % 10 == 1:
        print(f'\nНа столе \033[34m{TotalBonbon}\033[0m конфета')
    elif TotalBonbon == 2 or TotalBonbon == 3 or TotalBonbon == 4 or TotalBonbon % 10 == 2 or TotalBonbon % 10 == 3 or TotalBonbon % 10 == 4:
        print(f'\nНа столе \033[34m{TotalBonbon}\033[0m конфеты')
    elif TotalBonbon > 4:
        print(f'\nНа столе \033[34m{TotalBonbon}\033[0m конфет')
    if currentTurn == gamer11:
        turnofBot = int(input(f'\033[35m{currentTurn}\033[0m, сколько конфет вы забираете (от 1 до {maxTakeBonbon})? '))
        if turnofBot not in range(1, maxTakeBonbon + 1) or turnofBot > TotalBonbon:
            print('Увы,столько конфет взять нельзя.')
            continue
    else:
        if TotalBonbon > maxTakeBonbon:
            if TotalBonbon % (maxTakeBonbon + 1) == 0:
                turnofBot = random.randint(1, maxTakeBonbon)
            else:
                turnofBot = TotalBonbon % (maxTakeBonbon + 1)
        else: 
            turnofBot = TotalBonbon
        print(f'{gamer12} забралa \033[33m{turnofBot}\033[0m конфет')
    TotalBonbon = TotalBonbon - turnofBot
    if currentTurn == gamer11:
        currentTurn = gamer12
    else:
        currentTurn = gamer11
else:
    if currentTurn == gamer11:
        print(f'Победила: \033[32m\033[1m{gamer12}\033[0m\n')
    else:
        print(f'Победил: \033[32m\033[1m{gamer11}\033[0m\n')