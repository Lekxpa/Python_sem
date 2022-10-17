# Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.
# *Пример:*
#- 6782 -> 23
#- 0,56 -> 11

# n = input('Ведите число: ')
# print(lenght)
# res = 0
# # if n < 0:
# #     n *= (-1)
# for i in n:
#     if i != ',' and i != '.':
#         res += int(i)
# print(res)


n = input('Ведите число: ')
res = 0
if n == ',' and n == '.':
    lenght = len(str(n))
    print(lenght)
    n = n * (10 ** lenght)
elif n < 0:
    n *= (-1)
while n != 0:
    res = res + (int(n) % 10)
    n = int(n) // 10
print(res)