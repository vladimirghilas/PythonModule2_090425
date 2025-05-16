# Задача "Генератор обратного отсчета"
# Напишите генераторную функцию countdown(n), которая генерирует числа в обратном порядке от n до 1.

def countdown(n):
    for el in range(n,0,-1):
        yield el
for num in countdown(10):
    print(num)

print(list(countdown(10)))