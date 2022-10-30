# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

f = open('Numb1.txt','r', encoding='utf-8')
ls1 = f.read() 
print(ls1)

n = int(input('Задайте последовательность цифр: '))
strn = str(n)
lstend = []
for i in strn:
    if strn.count(i) == 1:
        lstend.append(i)
int_lstend = [int(x) for x in lstend]
print(f'Список неповторяющихся элементов: {int_lstend}')