# Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.
# *Пример:*
#- 6782 -> 23
#- 0,56 -> 11

def s(n):
    if n < 0:
        n *= (-1)
       
    s = str(n)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0
n = n * 10 ** a
couunt = 0
    while n > 0:
        count += n % 10
        n //= 10
    return count
n = float(input('Введите число: '))
print(s(n))

def num_after_point(x):
    s = str(x)
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1