# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# -23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# -6x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0

import re

f = open('Numb1.txt','r', encoding='utf-8')
e = open('Numb2.txt','r', encoding='utf-8')

ls1 = f.read() 
ls2 = e.read()
print(ls1)
print(ls2)


ls1 = ls1.replace(' = 0','')
ls2 = ls2.replace(' = 0','')
ls1 = ls1.replace(' ','')
ls2 = ls2.replace(' ','')
print(ls1)
print(ls2)

numbers = ['0','1','2','3','4','5','6','7','8','9']

lst1 = []
lst2 = []
dict1 = {}
dict2 = {}
ls1key = []
ls1Coef = []
ls2key = []
ls2Coef = []

if ls1[len(ls1)-1] != '^':
        ls1 = ls1 + 'x^0'
        print(ls1)

if ls2[len(ls2)-1] != '^':
        ls2 = ls2 + 'x^0'
        print(ls2)

for i in range(len(ls1)):
    if 'x' in ls1[i]:
        if '^' in ls1[i + 1]:
            m = ls1[i + 2]
        else:
            m = '1'
        ls1key.append(m)
print(f'Ключи 1 строка: {ls1key}')

for i in range(len(ls2)):
    if 'x' in ls2[i]:
        if '^' in ls2[i + 1]:
            m = ls2[i + 2]
        else:
            m = '1'
        ls2key.append(m)
print(f'Ключи 2 строка: {ls2key}')

int_ls1key = [int(x) for x in ls1key]
print (f'Ключи второго уравнения: {int_ls1key}')

int_ls2key = [int(x) for x in ls2key]
print (f'Ключи второго уравнения: {int_ls2key}')

if ls1[0] in numbers:
        if ls1[1] in numbers:
            lst1.append(ls1[0]+ls1[1])
        elif ls1[0] in numbers:
            lst1.append(ls1[0])
        else:
            lst1.append(1)
for i in range(len(ls1)):
    if '-' in ls1[i]:
        if ls1[i+1] in numbers and ls1[i+2] in numbers:
            lst1.append(ls1[i]+ls1[i+1]+ls1[i+2])
        elif ls1[i+1] in numbers:
            lst1.append(ls1[i]+ls1[i+1])
        else:
             lst1.append(-1)
    if '+' in ls1[i]:
        if ls1[i+1] in numbers and ls1[i+2] in numbers:
            lst1.append(ls1[i+1]+ls1[i+2])
        elif ls1[i+1] in numbers:
            lst1.append(ls1[i+1])
        else:
             lst1.append(1)
    
print(f'Коэффициенты 1 словаря: {lst1}')

if ls2[0] in numbers:
        if ls2[1] in numbers:
            lst2.append(ls2[0]+ls2[1])
        elif ls2[0] in numbers:
            lst2.append(ls2[0])
        else:
            lst2.append(1)
for i in range(len(ls2)):
    if '-' in ls2[i]:
        if ls2[i+1] in numbers and ls2[i+2] in numbers:
            lst2.append(ls2[i]+ls2[i+1]+ls2[i+2])
        elif ls2[i+1] in numbers:
            lst2.append(ls2[i]+ls2[i+1])
        else:
             lst2.append(-1)
    if '+' in ls2[i]:
        if ls2[i+1] in numbers and ls2[i+2] in numbers:
            lst2.append(ls2[i+1]+ls2[i+2])
        elif ls2[i+1] in numbers:
            lst2.append(ls2[i+1])
        else:
             lst2.append(1)
    
print(f'Коэффициенты 2 словаря: {lst2}')

int_lst1 = [int(x) for x in lst1]
print (f'Коэффициенты первого уравнения: {int_lst1}')

int_lst2 = [int(x) for x in lst2]
print (f'Коэффициенты второго уравнения: {int_lst2}')

dict1 = dict(zip(int_ls1key, int_lst1))
dict2 = dict(zip(int_ls2key, int_lst2))
print(f'Словарь1: {dict1}')
print(f'Словарь2: {dict2}')

d = dict1

for key, value in dict2.items():
    if key in dict1:
        d[key] += (value)
    else:
        d.update({key: value})

print(f'Сумма словарей: {d}')
print(d[0])

sorted_d = sorted(d.items())
print(f'Сумма словарей-кортежи: {sorted_d}')
b = dict(sorted_d)
print(f'Sorted: {b}')

items = list(b.items())
w = {k: v for k, v in reversed(items)}
print(f'перевернули итоговый словарь: {w}')

s = ''
for key, value in w.items():
    if key == 1 and value > 1:
        s += ' +' + str(value) + 'x'
    if key == 1 and value < -1:
        s += ' ' + str(value) + 'x'
    elif key == 0 and value > 1:
        s += ' +' + str(value)
    elif key == 0 and value < -1:
        s += '  ' + str(value)
    elif value > 1:
        s += ' +' + str(value) + 'x' + '^' + str(key)
    elif value < -1:
            s += ' ' + str(value) + 'x' + '^' + str(key)
    elif value == 1:
        s += ' +' + 'x' + '^' + str(key)
    elif value == -1:
        s += ' -' + 'x' + '^' + str(key)
    elif value == 0:
        s += ' +' + str(key)
s += ' = 0'
    
print(f'Сумма многочленов: {s}')

t = open('ResPoly)04_4.txt','w', encoding='utf-8')
t.write(s)

f.close()
e.close()
t.close()