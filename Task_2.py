# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

import random

n = int(input('Введите количество монет: '))
heads_or_tails = []
heads = 0
tails = 0

for i in range(n):
    heads_or_tails.append(random.randint(0,1))
    if heads_or_tails[i] == 1:
        heads += 1
    else:
        tails += 1

print('Количество орлов: {}'.format(heads))
print('Количество решек: {}'.format(tails))
if heads < tails:
    print('Нужно перевернуть {} орлов'.format(heads))
else:
    print('Нужно перевернуть {} решек'.format(tails))
