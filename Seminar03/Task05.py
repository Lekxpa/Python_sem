# Задайте число. Составьте список чисел Фибоначчи, в том числе 
# для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]

k = int(input("Введите число:"))
listFibn = []
listFibn2 = []
listFibn.insert(0,0)
listFibn.insert(1,1)
for i in range(2,k + 1):
    # listFibn[i] = listFibn[i - 1] + listFibn[i - 2]
    m = listFibn[i - 1] + listFibn[i - 2]
    listFibn.append(m)
    j = (- 1) ** (i + 1) * listFibn[i]
    listFibn2.insert(0,j)
print(listFibn)
print(listFibn2)
listFibn2.extend(listFibn)
print(listFibn2)