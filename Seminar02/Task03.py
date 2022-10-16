# Задайте список из n чисел последовательности (1 + 1/n)^n 
#и выведите на экран их сумму.

#*Пример:*

    # Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
    # Сумма 9.06

n = int(input('Введите число n: '))
sumn = 0
a = 1
for i in range(n):
    a = (1 + 1 / a) ** a
    sumn = a + sumn
    print(round ((a),8), end = ' ')
print('\n' 'Сумма чисел равна', round((sumn), 2))

# sequence = [((1 + 1 / i) ** i) for i in range(1, num+1)]

# def numbers(n):
#     summ = 0
#     for i in range(n):
#         a = int(input(f'Введи число {i + 1} '))
#         a = (1+1/a)**a
#         summ = a + summ
#         i += 1
#     return summ

# print('Сумма чисел равна',round((numbers(n)), 2))

# import decimal
# import random
# import re

# def test3():
#     num = int(entertext('введите натуральное число ', r'\d{0,}[1-9]{1}\d{0,}'))
#     sequence = [((1 + 1 / i) ** i) for i in range(1, num+1)]
#     print(sequence, sum(sequence))