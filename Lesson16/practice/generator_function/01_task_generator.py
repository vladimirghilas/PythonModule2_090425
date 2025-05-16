# Задача "Генератор четных чисел"
# Напишите генераторную функцию even_numbers(n), которая генерирует все четные числа от 0 до n включительно.

def even_numbers(n):
    for el in range(n + 1):
        if el%2 == 0:
            yield el

for num in even_numbers(13):
    print(num)
