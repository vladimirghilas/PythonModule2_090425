# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

n = int(input("enter your positive number "))
i = 0
k = 0
sum = 0
while i < n:
    k = random.randint(-100, 100)
    if k > 0 and k % 2 == 0:
        sum = sum + k
    i += 1
print(sum)
