# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

import math

N = int(input('Введите число N: '))

power = [i for i in range(N) if pow(2,i) < N]
print(power)
