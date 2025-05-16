# Задача "Генератор случайных целых чисел"
# Напишите генераторную функцию random_integers(n), которая генерирует n случайных целых чисел
# в диапазоне от 1 до 100 (используйте модуль random).
import random
def random_integers(n):
    for _ in range(n):
        m = random.randint(1,100)
        yield m

for num in random_integers(10):
    print(num)
