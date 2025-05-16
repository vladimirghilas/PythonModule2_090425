# "Генерация простых множителей числа"
# Напишите генераторную функцию, которая принимает целое число n и генерирует его простые множители по одному.
# (Например, для 12 генератор должен выдавать 2, 2, 3

def prime_factors(n):
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            yield divisor
            n //= divisor
        divisor += 1
for el in prime_factors(20):
    print(el)
