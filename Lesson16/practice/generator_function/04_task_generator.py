# Задача "Генератор степеней двойки"
# Напишите генераторную функцию powers_of_two(n), которая генерирует первые n степеней двойки (2⁰, 2¹, 2², ... 2^(n-1)).

def powers_of_two(n):
    for el in range(n):
        m = 2**el
        yield m

for num in powers_of_two(10):
    print(num)
