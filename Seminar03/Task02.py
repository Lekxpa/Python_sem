# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

N = int(input('Введите количество элементов в списке: '))
numbers = []
for i in range(N):
    numbers.append(random.randint(1,N))
print(f'Список: {numbers}')

res = 1
index1 = 0
index2 = len(numbers) - 1
print('Произведения пары чисел списка: ')
while index1 <= index2:
    res = numbers[index1] * numbers[index2]
    print(res, end = '  ')
    index1 += 1
    index2 -= 1