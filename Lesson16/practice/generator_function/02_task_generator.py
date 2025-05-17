# Задача "Генератор обратного отсчета"
# Напишите генераторную функцию countdown(n), которая генерирует числа в обратном порядке от n до 1.

def countdown(n):
<<<<<<< HEAD
    for el in range(n,0,-1):
        yield el
for num in countdown(10):
    print(num)

print(list(countdown(10)))
=======
    for number in range(n, 0, -1):
        yield number


print(list(countdown(8)))

>>>>>>> cfc7a9b39710a1b574d089247f0f41f4336dc744
