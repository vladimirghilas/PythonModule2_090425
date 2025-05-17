# Задача "Генератор случайных целых чисел"
# Напишите генераторную функцию random_integers(n), которая генерирует n случайных целых чисел
# в диапазоне от 1 до 100 (используйте модуль random).
import random
<<<<<<< HEAD
def random_integers(n):
    for _ in range(n):
        m = random.randint(1,100)
        yield m

for num in random_integers(10):
    print(num)
=======

def random_integers(n):
    for _ in range(n):
        yield random.randint(1, 100)


print(list(random_integers(6)))
>>>>>>> cfc7a9b39710a1b574d089247f0f41f4336dc744
