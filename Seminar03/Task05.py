# Задайте число. Составьте список чисел Фибоначчи, в том числе 
# для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]





# def FibanachiNEgativeAndPositive(argFib):
#     """
#     Positive part
#     """
#     fibPosit = []
#     if argFib < 1:
#         print("Empty list")
#         return fibPosit
#     else:
#         fibPosit.append(1)
#     if argFib > 1:
#         fibPosit.append(1)
#     else:
#         return [1, 0, 1]  
#     if argFib > 2:
#         for i in range(2, argFib):
#             fibPosit.append(fibPosit[i - 1] + fibPosit[i - 2])
#         """
#         Positive part
#         """
#         fibNegat = fibPosit.copy()
#         for i in range(argFib):
#             fibNegat[i] = fibNegat[i] * (-1) ** i
#         fibNegat.reverse()
#         """
#         Concatination
#         """
#         fibFull = fibNegat + [0] + fibPosit
#         return fibFull
#     else:
#         return [-1, 1, 0, 1, 1]

# n = int(input('Enter the argument for Fibanachi \n'))
# print (FibanachiNEgativeAndPositive(n))