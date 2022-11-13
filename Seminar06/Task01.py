# Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.

N = int(input("Введите число: "))
lst = list(filter(lambda x: N % x == 0, range(2,N + 1)))
# lst = [i for i in list(filter(lambda x: N % x == 0, range(2,N + 1)))]
print(f'Простые множители заданного числа: {lst}')

# #  предыдущее решение без лямбд и тп
# N = int(input("Введите число: "))
i = 2
lst = []
num = N
while i <= N:
    if N % i == 0:
        lst.append(i)
        N //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {num}: {lst}")