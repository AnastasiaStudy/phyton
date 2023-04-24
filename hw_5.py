# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# a = int(input("Введите число "))
# b = int(input("Введите степень числа(целое неотрицательно число) "))

# def func(a, b):
#     if b == 0:
#         return 1

#     return a * func(a, b - 1)


# print(func(a, b))

# Задача 6

# data = 'aaabbbccccddddd'
# seq = []
# r = None
# for d in data:
#     if d != r:
#         seq.append(d)
#         seq.append(str(1))
#         r = d
#     else:
#         seq[-1] = str(int(seq[-1]) + 1)
# print("".join(seq))


