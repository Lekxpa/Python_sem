# Игра против бота

# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг 
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего 
# конкурента?

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
print(f'\nПервый ход у игрока: \033[32m{currentTurn}\033[0m')
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
    if currentTurn == gamer12:
        turnofBot = 0
        if TotalBonbon > maxTakeBonbon and turnofBot in range(maxTakeBonbon + 1):
            turnofBot = random.randint(1,29)
            if turnofBot == 11 or turnofBot == 12 or turnofBot == 13 or turnofBot == 14:
                print(f'\033[32m{currentTurn}\033[0m: я беру себе {turnofBot} конфет')
            elif turnofBot == 1 or turnofBot % 10 == 1:
                print(f'\033[32m{currentTurn}\033[0m: я беру себе {turnofBot} конфету')
            elif turnofBot == 2 or turnofBot == 3 or turnofBot == 4 or turnofBot % 10 == 2 or turnofBot % 10 == 3 or turnofBot % 10 == 4:
                print(f'\033[32m{currentTurn}\033[0m: я беру себе {turnofBot} конфеты')
            elif turnofBot > 4:
                print(f'\033[32m{currentTurn}\033[0m: я беру себе {turnofBot} конфет')
        elif TotalBonbon < maxTakeBonbon + 1 and turnofBot < TotalBonbon:
            # turnofBot = random.randint(1,TotalBonbon)
            turnofBot = TotalBonbon
            if turnofBot == 11 or turnofBot == 12 or turnofBot == 13 or turnofBot == 14:
                print(f'\033[32m{currentTurn}\033[0m: я беру себе {turnofBot} конфет')
            elif turnofBot == 1 or turnofBot % 10 == 1:
                print(f'\033[32m{currentTurn}\033[0m: я беру себе {turnofBot} конфету')
            elif turnofBot == 2 or turnofBot == 3 or turnofBot == 4 or turnofBot % 10 == 2 or turnofBot % 10 == 3 or turnofBot % 10 == 4:
                print(f'\033[32m{currentTurn}\033[0m: я беру себе {turnofBot} конфеты')
            elif turnofBot > 4:
                print(f'\033[32m{currentTurn}\033[0m: я беру себе {turnofBot} конфет')
        # elif TotalBonbon < maxTakeBonbon + 1 and turnofBot > TotalBonbon:
        #     print(f'\033[32m{currentTurn}\033[0m: слишком много хотела взять конфет - {turnofBot} штук. Попробую еще раз!')
        #     continue
        takeBonbon = turnofBot
    else:
        takeBonbon = int(input(f'\033[32m{currentTurn}\033[0m, сколько конфет берете себе (от 1 до {maxTakeBonbon})? '))
        if takeBonbon not in range(1, maxTakeBonbon + 1):
            print(f'\nЭто слишком много! Можно взять не более {maxTakeBonbon} конфет! Попробуйте еще раз!')
            continue
        elif takeBonbon > TotalBonbon:
            print(f'\nЭто слишком много! Можно взять не более {TotalBonbon} конфет! Попробуйте еще раз!')
            continue
    TotalBonbon = TotalBonbon - takeBonbon
    if currentTurn == gamer11:
        currentTurn = gamer12
    else:
        currentTurn = gamer11
else:
    if currentTurn == gamer11:
        print(f'\nПобедил игрок: \033[32m{gamer12}\033[0m! Ура!')
    else:
        print(f'\nПобедил игрок: \033[32m{gamer11}\033[0m! Ура!')
print('\nGame over!\n')