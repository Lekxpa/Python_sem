# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг 
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего 
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
print('\n\033[1m\033[6m\033[36mПриветствуем вас в самой вкусной игре - игра с конфетами!\n')
print('\033[1m\033[4m\033[37m\033[45mПравила игры: \033[0m\
    \n\033[0mИграют два игрока, делая ход друг после друга.\
    \nПервый ход определяется жеребьёвкой.\
    \nЗа один ход можно забрать не более 28 конфет.\
    \nВ итоге все конфеты достаются игроку, сделавшему последний ход.\n')

gamer1 = input('\033[3mВведите имя первого игрока ')
gamer2 = input('\033[3mВведите имя второго игрока ')
gamer11 = (f'\033[1m\033[3\033[32m{gamer1}')
gamer12 = (f'\033[1m\033[3\033[32m{gamer2}')

TotalBonbon = 100

maxTakeBonbon = 28
firstTurn = random.randint(1,2)
if firstTurn == 1:
    currentTurn = gamer11
else:
    currentTurn = gamer12
print(f'\nПервый ход у игрока: \033[32m{currentTurn}\033[0m')

while TotalBonbon > 0:
    if TotalBonbon == 1 or TotalBonbon == 21:
        print(f'\nНа столе \033[34m{TotalBonbon}\033[0m конфета')
    elif TotalBonbon == 2 or TotalBonbon == 3 or TotalBonbon == 4 or TotalBonbon == 22 or TotalBonbon == 23 or TotalBonbon == 24:
        print(f'\nНа столе \033[34m{TotalBonbon}\033[0m конфеты')
    elif TotalBonbon > 4:
        print(f'\nНа столе \033[34m{TotalBonbon}\033[0m конфет')
    takeBonbon = int(input(f'\033[32m{currentTurn}\033[0m, сколько конфет берете себе (от 1 до {maxTakeBonbon})? '))
    if TotalBonbon > 28:
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
        print(f'\nПобедил игрок: \033[32m{gamer2}\033[0m! Ура!')
    else:
        print(f'\nПобедил игрок: \033[32m{gamer1}\033[0m! Ура!')
print('\nGame over!\n')