# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

lst = [randint(0,10) for i in range(int(input('Введите количество элементов в списке: ')))]
res_lst = [sum(lst[i] for i in filter(lambda x: x % 2 == 1, range(len(lst))))]
print(f'Исходный список: {lst}\
        \nСумма элементов нечетных позиций: {res_lst}')



# первое решение

# N = int(input('Введите количество элементов в списке: '))
# numbers = []
# for i in range(N):
#     numbers.append(random.randint(0,N))
# print(f'Список: {numbers}')

# res = 0
# index = 1
# while index < len(numbers):
#     res = res + numbers[index]
#     print(numbers[index], end = '  ')
#     index +=2
# print('\n' f'Сумма элементов нечетных позиций = {res}')