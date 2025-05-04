# Напишите функцию находящую n-ое число Фибоначчи.
def fibanaci(n):
    k = 0
    m = 1
    for i in range(n-2):
        c = k + m
        k = m
        m = c
    return print(f'{m}')

n = int(input("enter n "))
fibanaci(n)
