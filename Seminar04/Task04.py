# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего 
# на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто 
# пропускаем данную итерацию степени
# Записываем результат в файл.

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0


from random import randint

k = int(input('Задайте максимальную натуральную степень '))
lstOfCoef = []
total_list = []
for i in range(k + 1):
    lstOfCoef.append(randint(-99, 100))
print(f'Список коэффициентов: {lstOfCoef}') 

polynomial = ''
l = len(polynomial)
for i in range(k-1):
    if lstOfCoef[i] == 0:
        polynomial = polynomial
    elif lstOfCoef[i] == 1:
        polynomial = polynomial + 'x' + '^' + str(k - i) + ' + '
    elif lstOfCoef[i] == -1:
        polynomial = polynomial + '- x' + '^' + str(k - i) + ' + '
    else:
        polynomial = polynomial + str(lstOfCoef[i]) + 'x' + '^' + str(k - i) + ' + '
if lstOfCoef[k-1] == 0:
    polynomial = polynomial
elif lstOfCoef[k-1] == 1:
    polynomial = polynomial + 'x' + ' + '
else:
    polynomial = polynomial + str(lstOfCoef[k-1]) + 'x' + ' + '
if lstOfCoef[k] == 0:
    polynomial = polynomial + ' = 0'
else:
    polynomial = polynomial + ' + ' + str(lstOfCoef[k]) + ' = 0'
if polynomial.find('+ -'):
    polynomial = polynomial.replace('+ -',' - ')
if polynomial.find('- 1x'):
    polynomial = polynomial.replace('- 1x',' - x')
if polynomial.find('+   -'):
    polynomial = polynomial.replace('+   -',' - ')
if polynomial.find('+  ='):
    polynomial = polynomial.replace('+  =',' = ')
if polynomial.find('+  ='):
    polynomial = polynomial.replace('+  =',' = ')
if polynomial.find('+  + '):
    polynomial = polynomial.replace('+  + ',' + ')

print(polynomial)

with open('Task04Sem04.txt', 'w') as f:
    f.write(polynomial)