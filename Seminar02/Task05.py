# Реализуйте алгоритм перемешивания списка.

import random

N = int(input('Введите число: '))
numbers = []
for i in range(N):
    numbers.append(random.randint(-N,N))
print(f'Исходный список: {numbers}')

def shake(numbers):
    list = numbers[:]
    numbers_length = len(list)
    for i in range(numbers_length):
        index = random.randint(0, numbers_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list
print(f'Итоговый список: {shake(numbers)}')