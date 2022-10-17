# Задайте список из N элементов, заполненных числами из промежутка 
# [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции вводятся с клавиатуры .

# N = int(input('Введите число '))
# numbers = []
# for i in range(-N, N + 1):
#     #numbers(-N,N+1)
#     print(numbers[i], end = ' ')


N = int(input('Введите число '))
numbers = []
for i in range(N):
    numbers.append(-N,N+1)
print(numbers)


# N = int(input('Введите число: '))
# for i in range(-N, N + 1):
#     print(i, end=' ')
#     #print(numbers, end =' ')
# a = int(input('\n' 'Введите количество позиций элементов: '))
# if a < N ** 2:
#     b = 0
#     while b < a:
#         int(input(f'Введите значение {b + 1}-й позиции: ' ''))
#         print(sequence[i])
#         b+=1
#     else:
#         print(f'Неверно указано значение позиции')
# else:
#     print(f'Неверно указано значение. Количество позиций элементов не может быть больше {N**2}')
# res = 1
# res *= int(i)




# def my_list(n):
#     s = {}
#     for i in range(1, n+1):
#         s[i] = 3 * i + 1
#     return s
# num = int(input("Введите число N = "))
# st = my_list(num)
# print(st)


# from random import randint

# def list(n):
#     list = []
#     for i in range(n):
#         list.append(randint(-n, n))
#     return list

# n = int(input('Введите число N: '))
# numbers = list(n)
# print(numbers)
# x = open('file.txt','r')
# result = numbers[int(x.readline())] * numbers[int(x.readline(2))]
# print(result)

