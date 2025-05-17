# "Квадраты нечетных чисел"
# Напишите генераторное выражение, которое генерирует квадраты всех нечетных чисел в диапазоне от 1 до 10 включительно.

<<<<<<< HEAD
def square_num(n):
    for el in range(n):
        yield (el**2)

for num in square_num(10):
    print(num)
=======

result = (el ** 2 for el in range(1, 11) if el % 2 != 0)
print(result)
>>>>>>> cfc7a9b39710a1b574d089247f0f41f4336dc744
