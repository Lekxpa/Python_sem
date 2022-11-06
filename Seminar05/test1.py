# Создайте программу для игры в 'Крестики-нолики'.

# import random

# print('\n\033[1m\033[4m\033[37m\033[45m\033[3mКрестики-нолики\033[0m\n\
#     \n\033[3mНеобходимо указать номер ячейки,\
#     \n\033[3mв которую хотите поставить крестик/нолик\033[0m\n')

# borders = list(range(1, 10))

# def print_borders(borders):
#     print('-  ' * 5)
#     for i in range(3):
#         print('|', borders[i * 3], '|', borders[i * 3 + 1], '|', borders[i * 3 + 2], '|')
#         print('-  ' * 5)

# print('Меня зовут\033[0m  \033[1m\033[6m\033[32mМаруся!\033[0m \nПоиграем вместе?\n')

# gamer1 = input('\033[3mВведите Ваше имя\033[0m ')
# gamer11 = (f'\033[1m\033[3\033[32m{gamer1}')
# gamer12 = 'Маруся'



# if currentTurn == gamer11:
#         currentTurn = gamer12
#     else:
#         currentTurn = gamer11
# else:
#     if currentTurn == gamer11:
#         print(f'\nПобедил игрок: \033[32m{gamer12}\033[0m! Ура!')
#     else:
#         print(f'\nПобедил игрок: \033[32m{gamer11}\033[0m! Ура!')

# def input_XO(sign):
#     # step_question = 0
#     firstTurn = random.randint(1,2)
#     if firstTurn == 1:
#         currentTurn = gamer11
#     else:
#         currentTurn = gamer12
#     # print(f'\nПервый ход у игрока: \033[32m{currentTurn}\033[0m')
#     print(f'\nПервый ход у игрока: \033[32m{currentTurn}\033[0m')
#     valid = False
#     while not valid:
#         if currentTurn == gamer12:
#             step_question = random.randint(1,10)
#             print(f'Маруся: я ставлю {sign} в ячейку - {step_question}')
#         # step_question = input(f'\n\033[3mУкажите номер ячейки, в которую хотите поставить {sign}? \033[0m')
#             # try:
#             #     step_question = int(step_question)
#             # except:
#             #     print('Неверное значение. Укажите номер ячейки (от 1 до 9)! ')
#             if step_question >= 1 and step_question <= 9:
#                 if (str(borders[step_question-1]) not in 'XO'):
#                     borders[step_question-1] = sign
#                     valid = True
#                 else:
#                     print('Эта ячейка занята!')
#             else:
#                 print('Неверное значение. Укажите номер свободной ячейки (от 1 до 9)! ')
#                 continue
#         elif currentTurn == gamer11:
#             step_question = input(f'\n\033[3mУкажите номер ячейки, в которую хотите поставить {sign}? \033[0m')
#             try:
#                 step_question = int(step_question)
#             except:
#                 print('Неверное значение. Укажите номер ячейки (от 1 до 9)! ')
#                 continue
#             if step_question >= 1 and step_question <= 9:
#                 if (str(borders[step_question-1]) not in 'XO'):
#                     borders[step_question-1] = sign
#                     valid = True
#                 else:
#                     print('Эта ячейка занята!')
#             else:
#                 print('Неверное значение. Укажите номер свободной ячейки (от 1 до 9)! ')
#             continue
#         if currentTurn == gamer11:
#             currentTurn = gamer12
#         else:
#             currentTurn = gamer11
# # else:
# #     if currentTurn == gamer11:
# #         print(f'\nПобедил игрок: \033[32m{gamer12}\033[0m! Ура!')
# #     else:
# #         print(f'\nПобедил игрок: \033[32m{gamer11}\033[0m! Ура!')


# def input_XO(sign):
    # step_question = 0

# firstTurn = random.randint(1,2)
# if firstTurn == 1:
#     currentTurn = gamer11
# else:
#     currentTurn = gamer12
    # print(f'\nПервый ход у игрока: \033[32m{currentTurn}\033[0m')
# print(f'\nПервый ход у игрока: \033[32m{currentTurn}\033[0m')
# valid = False
# while not valid:
#     step_question = random.randint(1,10)
#     if currentTurn == gamer12:
#         print(f'Маруся: я ставлю X в ячейку - {step_question}')
#     else:
#         step_question = input(f'\n\033[3mУкажите номер ячейки, в которую хотите поставить X? \033[0m')
#         try:
#             step_question = int(step_question)
#         except:
#             print('Неверное значение. Укажите номер ячейки (от 1 до 9)! ')
#         # print(f'Маруся: я ставлю O в ячейку - {step_question}')
#         if step_question >= 1 and step_question <= 9:
#             if (str(borders[step_question-1]) not in 'XO'):
#                 borders[step_question-1] = X
#                 valid = True
#             else:
#                  print('Эта ячейка занята!')
#         else:
#             print('Неверное значение. Укажите номер свободной ячейки (от 1 до 9)! ')
#             continue
#         # elif currentTurn == gamer11:
#         #     step_question = input(f'\n\033[3mУкажите номер ячейки, в которую хотите поставить {sign}? \033[0m')
#         #     try:
#         #         step_question = int(step_question)
#         #     except:
#         #         print('Неверное значение. Укажите номер ячейки (от 1 до 9)! ')
#         #         continue
#         if step_question >= 1 and step_question <= 9:
#             if (str(borders[step_question-1]) not in 'XO'):
#                 borders[step_question-1] = sign
#                 valid = True
#             else:
#                 print('Эта ячейка занята!')
#         else:
#             print('Неверное значение. Укажите номер свободной ячейки (от 1 до 9)! ')
#             continue
#     if currentTurn == gamer11:
#         currentTurn = gamer12
#     else:
#         currentTurn = gamer11
# else:
#     if currentTurn == gamer11:
#         print(f'\nПобедил игрок: \033[32m{gamer12}\033[0m! Ура!')
#     else:
#         print(f'\nПобедил игрок: \033[32m{gamer11}\033[0m! Ура!')

# def check_win(borders):
#     winline = [[0,1,2],
#                 [3,4,5],
#                 [6,7,8],
#                 [0,3,6],
#                 [1,4,7],
#                 [2,5,8],
#                 [0,4,8],
#                 [2,4,6]]
#     for i in winline:
#         if borders[i[0]] == borders[i[1]] == borders[i[2]]:
#             # def print_borders(borders):
#             #     # print(f'\033[32m{borders[i[0]]} {borders[i[1]]} {borders[i[2]]}\033[0m')
#             #     print(f'\033[32m{winline}\033[0m')
#             # print_borders(borders)
#             return borders[i[0]]
#     return False


# def play(borders):
#     count = 0
#     win = False
#     while not win:
#         print_borders(borders)
#         if count % 2 == 0:
#             input_XO('X')
#         else:
#            input_XO('O')
#         count += 1
#         if count > 4:
#             a = check_win(borders)
#             if a:
#                 print(f'\n\033[1m\033[4m\033[32m\033[3m{a} выиграл!\033[0m')
#                 win = True
#                 # print_borders(f'\n\033[32m{check_win(borders)}\033[0m')
#                 break
#         if count == 9:
#             print('Ничья!')
#             break
#     print_borders(borders)

# play(borders)

# print('\nGame over!\n')

# input(f'\nНажмите \033[3m\033[32mEnter\033[0m для выхода!\n')




import random

print('\n\033[1m\033[4m\033[37m\033[45m\033[3mКрестики-нолики\033[0m\n\
    \n\033[3mНеобходимо указать номер ячейки,\
    \n\033[3mв которую хотите поставить крестик/нолик\033[0m\n')

borders = list(range(1, 10))

def print_borders(borders):
    print('-  ' * 5)
    for i in range(3):
        print('|', borders[i * 3], '|', borders[i * 3 + 1], '|', borders[i * 3 + 2], '|')
        print('-  ' * 5)

print('Меня зовут\033[0m  \033[1m\033[6m\033[32mМаруся!\033[0m \nПоиграем вместе?\n')

gamer1 = input('\033[3mВведите Ваше имя\033[0m ')
gamer11 = (f'\033[1m\033[3\033[32m{gamer1}')
gamer12 = 'Маруся'

firstTurn = random.randint(1,2)
if firstTurn == 1:
    currentTurn = gamer11
else:
    currentTurn = gamer12

print(f'\nПервый ход у игрока: \033[32m{currentTurn}\033[0m')


firstTurn = random.randint(1,2)
if firstTurn == 1:
    currentTurn = gamer11
else:
    currentTurn = gamer12
print(f'\nПервый ход у игрока: \033[32m{currentTurn}\033[0m')

if currentTurn == gamer12:
    step = random.randint(1,10)
    print(f'Маруся: я ставлю X в ячейку - {step}')
    print_borders(borders)
#     else:
#         step_question = input(f'\n\033[3mУкажите номер ячейки, в которую хотите поставить X? \033[0m')
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




def check_win(borders):
    winline = [[0,1,2],
                [3,4,5],
                [6,7,8],
                [0,3,6],
                [1,4,7],
                [2,5,8],
                [0,4,8],
                [2,4,6]]
    for i in winline:
        if borders[i[0]] == borders[i[1]] == borders[i[2]]:
            return borders[i[0]]
    return False