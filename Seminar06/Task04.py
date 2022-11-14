# Задайте список из n чисел последовательности (1 + 1/n)^n 
#и выведите на экран их сумму.
#*Пример:*
    # Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
    # Сумма 9.06

n = int(input('Введите число n: '))
res_lst = [sum(i for i in list(map(lambda x: round((1 + 1 / x) ** x, 2), range (1, n + 1))))]
print(f'Сумма: {res_lst}')


#  первое решение
# def SummOfElements():
#     n = int(input('Введите число n: '))
#     sumN = 0
#     numbers = {}
#     for i in range (1, n + 1):
#         numbers[i] = round((1 + 1 / i) ** i, 2)
#         sumN = numbers[i] + sumN
#     print(numbers)
#     print('Сумма чисел равна: ', round((sumN), 2))
# SummOfElements()