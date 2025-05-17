# Задача "Генератор четных чисел"
# Напишите генераторную функцию even_numbers(n), которая генерирует все четные числа от 0 до n включительно.

def even_numbers(n):
<<<<<<< HEAD
    for el in range(n + 1):
        if el%2 == 0:
            yield el

for num in even_numbers(13):
    print(num)
=======
    for el in range(0, n + 1, 2):
        yield el



for el in even_numbers(13):
    print(el)
>>>>>>> cfc7a9b39710a1b574d089247f0f41f4336dc744
