# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0

f = open('Numb1.txt','r')
f.close()
e = open('Numb2.txt','r')
e.close()


p1 = open('Task33 Polnominal.txt', 'r') # opening
p2 = open('Task34 Polnominal.txt', 'r') 

pol1 = p1.read() #reading
pol2 = p2.read()
print(pol1)
print(pol2)
pol1 = pol1.replace(' = 0','') #clearing data
pol2 = pol2.replace(' = 0','')
# print(pol1)
# print(pol2)
pol1 = pol1.replace('^','')
pol2 = pol2.replace('^','')
# print(pol1)
# print(pol2)

pol1_list = pol1.split(' + ')  #splitting 1
# print(pol1_list)
pol2_list = pol2.split(' + ')
# print(pol2_list)

my_dict1 = []  #splitting 2
for element in pol1_list:
    if 'x' in element:
        my_dict1.append(element.split('x'))
    else:
        absolute1 = element

my_dict2 = []
for element in pol2_list:
    if 'x' in element:
        my_dict2.append(element.split('x'))
    else:
        absolute2 = element

absoluteTotal = int(absolute1) + int(absolute2)

my_dictFull = my_dict1 + my_dict2 #concatination dict

for element in my_dictFull: #swithing places for values in incuding lists for sorting
    elementTemp = element[0]
    element[0] = element[1]
    element[1] = elementTemp

my_dictFull.sort(reverse=True) #sorting

cutted_dictFull = [] #summarize values in same powers
i = 0
while i < (len(my_dictFull)): 
    a = my_dictFull[i][0]
    if my_dictFull[i][0] == my_dictFull[i + 1][0]:
        b = int(my_dictFull[i][1]) + int(my_dictFull[i + 1][1])
        i += 2
    else:
        b = int(my_dictFull[i][1])
        i += 1
    cutted_dictFull.append([a, b])

formula = ''
i = 0
while i < (len(cutted_dictFull)- 1): #Creating formula string
    formula += str(cutted_dictFull[i][1]) + 'x^' + str(cutted_dictFull[i][0]) + ' + '
    i += 1


if cutted_dictFull[len(cutted_dictFull)- 1][0] == '':
    formula += str(cutted_dictFull[len(cutted_dictFull)- 1][1]) + 'x' 
else:
    formula += str(cutted_dictFull[len(cutted_dictFull)- 1][1]) + 'x^' + str(cutted_dictFull[len(cutted_dictFull)- 1][0]) + 'x' 

if absoluteTotal != 0:
    formula += ' + ' + str(absoluteTotal) + ' = 0'
else:
    formula += ' = 0'
print(formula)

with open('Task34 Sum of Polnominals.txt', 'x') as s:
    s.write(formula)




    with open('file_1.txt', 'w', encoding='utf-8') as data_1:
    data_1.write('5x + 3x')
with open('file_2.txt', 'w', encoding='utf-8') as data_2:
    data_2.writelines('3x^2 + x + 8 + 6')

with open('file_1.txt', 'r', encoding='utf-8') as data_1:
    text_1 = data_1.read().split()
    print(text_1)

with open('file_2.txt', 'r', encoding='utf-8') as data_2:
    text_2 = data_2.read().split()
    # text_2 = set(text_2)
    print(text_2)

res = text_2 + text_1
for i in res:
    if i.isdigit():
        print(i)

print(res)