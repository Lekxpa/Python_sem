# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import string
import re

f = open('Numb4_5.txt','r', encoding='utf-8')
ls = f.read() 
print(f'Исходный файл:   {ls}')
lst=[]
for l in ls:
    lst.append(l)
# print(f'исходные данные в списке: {lst}')

lstkey = []
lstcoeff = []

a = lst[0]
lstcoeff.append(a)
for i in range(len(lst) - 1):
    if lst[i + 1] != lst[i]:
        lstcoeff.append(lst[i + 1])
# print(lstcoeff)

x=1
for i in range(len(lst) - 2):
    if lst[i + 1] == lst [i]:
        x += 1
        i += 1
    else:
        lstkey.append(x)
        x = 1
        if lst[i + 2] == lst[i]:
            x += 1
            i += 1
lstkey.append(x)

for i in range(len(lst) - 1, len(lst)):
    if lst[len(lst) - 1] == lst[len(lst) - 2]:
        b = lstkey[len(lstkey)-1]
        lstkey.pop(len(lstkey)-1)
        b = b + 1
        lstkey.append(b)
    else:
        lstkey.append(1)
# print(lstkey)

s = ''
i = 0
j = 0
while i < len(lstkey) and j < len(lstcoeff):
    s += str(lstkey[i]) + str(lstcoeff[j])
    j += 1
    i += 1
print(f'Сжатые данные:   {s}')

t = open('Res_compress_04_5.txt','w', encoding='utf-8')
t.write(s)

srt = [s]
# print(srt)

num = ''
nub = []
res = ''

for i in range(0,len(s) - 2):
    if not s[i].isalpha() and not s[i + 1].isalpha() and not s[i + 2].isalpha():
        num = s[i]
        res += s[i + 1] * int(num)
        i += 3
    elif not s[i].isalpha() and s[i + 1].isalpha():
        num = s[i]
        res += s[i + 1] * int(num)
        i += 3
    elif not s[i].isalpha() and not s[i + 1].isalpha() and s[i + 2].isalpha():
        nub.append(s[i] + s[i +1])
        int_nub = [int(x) for x in nub]
        p = int_nub[0]
        res += str(s[i + 2]) * p
        i += 3
    elif not s[i].isalpha() and not s[i - 1].isalpha() and not s[i + 1].isalpha():
        i += 2

if s[len(s) - 3].isalpha() and not s[len(s) - 2].isalpha():
    num = s[len(s) - 2]
    res += str(s[len(s) - 1]) * int(num)

print(f'Разжатые данные: {res}')

e = open('Res_recall_04_5.txt','w', encoding='utf-8')
e.write(res)

f.close()
t.close()
e.close()