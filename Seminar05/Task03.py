# Создайте программу для игры в 'Крестики-нолики'.

print('\n\033[1m\033[4m\033[37m\033[45m\033[3mКрестики-нолики\033[0m\n\
    \n\033[3mНеобходимо указать номер ячейки,\
    \n\033[3mв которую хотите поставить крестик/нолик\033[0m\n')

borders = list(range(1, 10))

def print_borders(borders):
    print('-  ' * 5)
    for i in range(3):
        print('|', borders[i * 3], '|', borders[i * 3 + 1], '|', borders[i * 3 + 2], '|')
        print('-  ' * 5)

def input_XO(sign):
    valid = False
    while not valid:
        step_question = input(f'\n\033[3mУкажите номер ячейки, в которую хотите поставить {sign}? \033[0m')
        try:
            step_question = int(step_question)
        except:
            print('Неверное значение. Укажите номер ячейки (от 1 до 9)! ')
            continue
        if step_question >= 1 and step_question <= 9:
            if (str(borders[step_question-1]) not in 'XO'):
                borders[step_question-1] = sign
                valid = True
            else:
                print('Эта ячейка занята!')
        else:
            print('Неверное значение. Укажите номер свободной ячейки (от 1 до 9)! ')

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
            # def print_borders(borders):
            #     # print(f'\033[32m{borders[i[0]]} {borders[i[1]]} {borders[i[2]]}\033[0m')
            #     print(f'\033[32m{winline}\033[0m')
            # print_borders(borders)
            return borders[i[0]]
    return False


def play(borders):
    count = 0
    win = False
    while not win:
        print_borders(borders)
        if count % 2 == 0:
            input_XO('X')
        else:
           input_XO('O')
        count += 1
        if count > 4:
            a = check_win(borders)
            if a:
                print(f'\n\033[1m\033[4m\033[32m\033[3m{a} выиграл!\033[0m')
                win = True
                # print_borders(f'\n\033[32m{check_win(borders)}\033[0m')
                break
        if count == 9:
            print('Ничья!')
            break
    print_borders(borders)

play(borders)

input(f'\nНажмите \033[3m\033[32mEnter\033[0m для выхода!\n')