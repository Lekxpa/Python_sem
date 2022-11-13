# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input("Введите число:"))
lst = list(map(lambda x: 0 if n % 2 == 0 else 1   , n))
# N = n
# b = ''
# i = 0
# while n > 0:
#     a = n % 2
#     b = str(a) + b
#     n = n // 2
print(f'Двоичное число из {n} -> {lst}')


def dec_bin(N):
    if N >= 2:
        dec_bin(N // 2)
    print(N % 2, end='')
 
 
dec_bin(8)
