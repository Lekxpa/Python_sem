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

k = int(input('Задайте натуральную степень '))
# k = 10
ratiosList = []
for i in range(k + 1):
    ratiosList.append(randint(1, 100))
print(f'Список коэффициентов: {ratiosList}') 
formula = ''
for i in range(k-1):
    formula = formula + str(ratiosList[i]) + 'x' + '^' + str(k - i) + ' + '
formula = formula + str(ratiosList[k-1]) + 'x' + ' + '
formula = formula + str(ratiosList[k]) + ' = 0'

print(formula)
# print(type(formula))

with open('Task33 Polnominal.txt', 'w') as p:
    p.write(formula)