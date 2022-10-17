# Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.
# *Пример:*
#- 6782 -> 23
#- 0,56 -> 11

def SumOfNumbers():
    n = float(input('Ведите число: '))
    strn = str(n)
    changesymbol = strn.replace('-','')
    changesymbol = changesymbol.replace('.','')
    countnums = len(changesymbol)
    Sumofnums = 0
    for i in range(countnums):
        Sumofnums += int(changesymbol[i])
    print(f'Сумма цифр заданного числа: {Sumofnums}')
SumOfNumbers()