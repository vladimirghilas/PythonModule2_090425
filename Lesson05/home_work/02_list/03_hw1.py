# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
n = int(input("enter number "))
numbers = []
for i in range(n):
    number = random.randint(-100,100)
    if number > 0:
        numbers.append(number/2)
print(numbers)
