# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0

import re

f = open('Numb1.txt','r', encoding='utf-8')
e = open('Numb2.txt','r', encoding='utf-8')

ls1 = f.read() #reading
ls2 = e.read()
print(ls1)
print(ls2)

ls1 = ls1.replace(' = 0','')
ls2 = ls2.replace(' = 0','')
# ls1 = ls1.replace('x','*x')
# ls2 = ls2.replace('x','*x')
# ls1 = ls1.replace(' - ','')
# ls2 = ls2.replace(' - ','')
# ls1 = ls1.replace('x^ + ','')
# ls2 = ls2.replace('^','')
print(ls1)
print(ls2)
print(len(ls1))
numbers_plus = ['0','1','2','3','4','5','6','7','8','9', '+', '-']
numbers = ['0','1','2','3','4','5','6','7','8','9']

lf = re.findall('\d+', ls1)
lf1 = re.findall('\d+', ls2)
print(lf)
print(lf1)

# ls1 = ls1.replace('x^numbers','')
# ls2 = ls2.replace('^','')
# print(ls1)
# print(ls2)

lst1 = []  # создаем пустой список
lst2 = []
dict1 = {}
dict2 = {}
ls1key = []
ls1Coef = []
ls2key = []
ls2Coef = []
ls1Coef1 = []
m = 0
n = 0

for i in range(len(ls1)):
    if ls1[i] == 'x' and ls1[i + 1] == '^':
        n = ls1[i + 2]
        ls1Coef1 = ls1Coef1.remove(n)
print(ls1Coef1)
 
for i in range(len(ls1)):
    if type(ls1[i]) is int and ls1[i + 1] == 'x':
        n = ls1[i]
        ls1Coef.append(n)
    elif 'x' in ls1[i]:
        if '^' in ls1[i + 1]:
            m = 'x' + '^' + ls1[i + 2]
        else:
            m = 'x^1'
        ls1key.append(m)
    # if ls1[i] in range(-100,100):
    # if ls1[i] in range(-100,100) and ls1[i + 1] in range(-100,100):
    # if ls1[i] is numbers and ls1[i + 1] is numbers:
    else:
        if type(ls1[i]) is int and type(ls1[i + 1]) is int:
        # n = ls1[i].split(ls1[i + 1])
            n = ls1[i] * 10 + ls1[i + 1]
        # n = ls1Coef.split(ls1[i] + ls1[i + 1])
            ls1Coef.append(n)
        # i += 1
print(ls1key)    
print(ls1Coef)




for i in range(len(ls2)):
    # if ls1[i] in range(-100,100):
    # if ls1[i] in range(-100,100) and ls1[i + 1] in range(-100,100):
    # if ls1[i] is numbers and ls1[i + 1] is numbers:
    if type(ls2[i]) is int and type(ls2[i + 1]) is int:
        # n = ls1[i].split(ls1[i + 1])
        n = ls2[i] * 10 + ls2[i + 1]
        # n = ls1Coef.split(ls1[i] + ls1[i + 1])
        ls2Coef.append(n)
        # i += 1
    else:
        if type(ls2[i]) is int and ls2[i + 1] == 'x':
            n = ls2[i]
            ls2Coef.append(n)
        # ls2Coef.append(',')
        elif 'x' in ls2[i]:
            if '^' in ls2[i + 1]:
                m = 'x' + '^' + ls2[i + 2]
            else:
                m = 'x^1'
            ls2key.append(m)

print(ls2Coef)
print(ls2key)

# for element in ls1:
#     if 'x' in element:
#         dict1.append(element.split('x'))
#     else:
#         absolute1 = element
# print(dict1)


# brc_open = {'(': ')', '[': ']', '{': '}'}  # делаем словарь - открывающиеся скобки - ключи, закрывающиеся - соответствующие значения

# for i in range(len(brc)):
#     if brc[i] in brc_open.keys():  # получаем список всех ключей - открывающихся скобок: если скобка открывающаяся с помощью метода append записываем ее в конец списка
#         stack.append(brc[i])
#     elif brc[i] in brc_open.values():   # получаем список всех значений - закрывающихся скобок. Если скобка закрывающая, проверяем:
#         if len(stack)>0: # есть ли в нашем списке такой элемент, устанавливаем, что длина списка больше нуля
#             b = stack.pop() # получаем с помощью метода pop последний элемент списка
#             if brc_open[b] != brc[i]:  #берем наш словарь, и по ключу открывающейся скобки, берем значение закрывающейся скобки
#                 return i  # если не совпали, возвращаем номер элемента
#         else:
#             return i
# if len(stack) == 0:
#     return 0
# else:
#     return len(brc)
# s = '([1+1]{{[3**5]}))-3})'
# print(s)
# pos = check_brackets(s)
# if pos > 0:
#     st = ' '*pos
#     print(f'{st}^')

# print(pol1)
# print(pol2)

# ls1_list = ls1.split(' + ')  #splitting 1
# # print(pol1_list)
# ls2_list = ls2.split(' + ')
# # print(pol2_list)

# my_dict1 = []  #splitting 2
# for element in ls1_list:
#     if 'x' in element:
#         my_dict1.append(element.split('x'))
#     else:
#         absolute1 = element

# my_dict2 = []
# for element in ls2_list:
#     if 'x' in element:
#         my_dict2.append(element.split('x'))
#     else:
#         absolute2 = element

# absoluteTotal = int(absolute1) + int(absolute2)

# my_dictFull = my_dict1 + my_dict2 #concatination dict

# for element in my_dictFull: #swithing places for values in incuding lists for sorting
#     elementTemp = element[0]
#     element[0] = element[1]
#     element[1] = elementTemp

# my_dictFull.sort(reverse=True) #sorting

# cutted_dictFull = [] #summarize values in same powers
# i = 0
# while i < (len(my_dictFull)): 
#     a = my_dictFull[i][0]
#     if my_dictFull[i][0] == my_dictFull[i + 1][0]:
#         b = int(my_dictFull[i][1]) + int(my_dictFull[i + 1][1])
#         i += 2
#     else:
#         b = int(my_dictFull[i][1])
#         i += 1
#     cutted_dictFull.append([a, b])

# formula = ''
# i = 0
# while i < (len(cutted_dictFull)- 1): #Creating formula string
#     formula += str(cutted_dictFull[i][1]) + 'x^' + str(cutted_dictFull[i][0]) + ' + '
#     i += 1


# if cutted_dictFull[len(cutted_dictFull)- 1][0] == '':
#     formula += str(cutted_dictFull[len(cutted_dictFull)- 1][1]) + 'x' 
# else:
#     formula += str(cutted_dictFull[len(cutted_dictFull)- 1][1]) + 'x^' + str(cutted_dictFull[len(cutted_dictFull)- 1][0]) + 'x' 

# if absoluteTotal != 0:
#     formula += ' + ' + str(absoluteTotal) + ' = 0'
# else:
#     formula += ' = 0'
# print(formula)

# with open('Res05Sem04.txt', 'x') as a:
#     a.write(formula)

# ls1 = ls1.replace(' = 0','')
# ls2 = ls2.replace(' = 0','')
# ls1 = ls1.replace(' + ','')
# ls2 = ls2.replace(' + ','')
# ls1 = ls1.replace(' - ','')
# ls2 = ls2.replace(' - ','')
# print(ls1)
# print(ls2)

# lst1 = []  # создаем пустой список
# lst2 = []
# dict1 = {}
# dict2 = {}
# ls1key = []
# ls1Coef = []
# ls2key = []
# ls2Coef = []

# for element in ls1:
#     if 'x' in element:
#         dict1.append(element.split('x'))
#     else:
#         absolute1 = element
# print(dict1)


# brc_open = {'(': ')', '[': ']', '{': '}'}  # делаем словарь - открывающиеся скобки - ключи, закрывающиеся - соответствующие значения

# for i in range(len(brc)):
#     if brc[i] in brc_open.keys():  # получаем список всех ключей - открывающихся скобок: если скобка открывающаяся с помощью метода append записываем ее в конец списка
#         stack.append(brc[i])
#     elif brc[i] in brc_open.values():   # получаем список всех значений - закрывающихся скобок. Если скобка закрывающая, проверяем:
#         if len(stack)>0: # есть ли в нашем списке такой элемент, устанавливаем, что длина списка больше нуля
#             b = stack.pop() # получаем с помощью метода pop последний элемент списка
#             if brc_open[b] != brc[i]:  #берем наш словарь, и по ключу открывающейся скобки, берем значение закрывающейся скобки
#                 return i  # если не совпали, возвращаем номер элемента
#         else:
#             return i
# if len(stack) == 0:
#     return 0
# else:
#     return len(brc)
# s = '([1+1]{{[3**5]}))-3})'
# print(s)
# pos = check_brackets(s)
# if pos > 0:
#     st = ' '*pos
#     print(f'{st}^')


# pol1 = pol1.replace('^','')
# pol2 = pol2.replace('^','')
# # print(pol1)
# # print(pol2)

# pol1_list = pol1.split(' + ')  #splitting 1
# # print(pol1_list)
# pol2_list = pol2.split(' + ')
# # print(pol2_list)

# my_dict1 = []  #splitting 2
# for element in pol1_list:
#     if 'x' in element:
#         my_dict1.append(element.split('x'))
#     else:
#         absolute1 = element

# my_dict2 = []
# for element in pol2_list:
#     if 'x' in element:
#         my_dict2.append(element.split('x'))
#     else:
#         absolute2 = element

# absoluteTotal = int(absolute1) + int(absolute2)

# my_dictFull = my_dict1 + my_dict2 #concatination dict

# for element in my_dictFull: #swithing places for values in incuding lists for sorting
#     elementTemp = element[0]
#     element[0] = element[1]
#     element[1] = elementTemp

# my_dictFull.sort(reverse=True) #sorting

# cutted_dictFull = [] #summarize values in same powers
# i = 0
# while i < (len(my_dictFull)): 
#     a = my_dictFull[i][0]
#     if my_dictFull[i][0] == my_dictFull[i + 1][0]:
#         b = int(my_dictFull[i][1]) + int(my_dictFull[i + 1][1])
#         i += 2
#     else:
#         b = int(my_dictFull[i][1])
#         i += 1
#     cutted_dictFull.append([a, b])

# formula = ''
# i = 0
# while i < (len(cutted_dictFull)- 1): #Creating formula string
#     formula += str(cutted_dictFull[i][1]) + 'x^' + str(cutted_dictFull[i][0]) + ' + '
#     i += 1


# if cutted_dictFull[len(cutted_dictFull)- 1][0] == '':
#     formula += str(cutted_dictFull[len(cutted_dictFull)- 1][1]) + 'x' 
# else:
#     formula += str(cutted_dictFull[len(cutted_dictFull)- 1][1]) + 'x^' + str(cutted_dictFull[len(cutted_dictFull)- 1][0]) + 'x' 

# if absoluteTotal != 0:
#     formula += ' + ' + str(absoluteTotal) + ' = 0'
# else:
#     formula += ' = 0'
# print(formula)

# with open('Task34 Sum of Polnominals.txt', 'x') as s:
#     s.write(formula)




#     with open('file_1.txt', 'w', encoding='utf-8') as data_1:
#     data_1.write('5x + 3x')
# with open('file_2.txt', 'w', encoding='utf-8') as data_2:
#     data_2.writelines('3x^2 + x + 8 + 6')

# with open('file_1.txt', 'r', encoding='utf-8') as data_1:
#     text_1 = data_1.read().split()
#     print(text_1)

# with open('file_2.txt', 'r', encoding='utf-8') as data_2:
#     text_2 = data_2.read().split()
#     # text_2 = set(text_2)
#     print(text_2)

# res = text_2 + text_1
# for i in res:
#     if i.isdigit():
#         print(i)

# print(res)

# f.close()
# e.close()